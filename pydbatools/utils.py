import urllib


def make_connection_string(client) -> str:
    """Generate connection string to be used by SQLAlchemy."""

    params = urllib.parse.quote_plus(
        "DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={UID};PWD={PWD};trusted_connection={trusted_connection};autocommit=True".format(
            driver=client.driver,
            server=client.server,
            database=client.database,
            UID=client.UID,
            PWD=client.PWD,
            trusted_connection=client.trusted_connection,
            autocommit=True,
        )
    )
    return params


def extend_dbs(func):
    """Decorator to retrieve additional databases and run functions against each"""

    def wrapper_extend_dbs(client, *args, **kwargs):
        if not client.target_dbs:
            func(client, *args, db=client.database)
            return None

        if isinstance(client.target_dbs, tuple):
            for db in client.target_dbs:
                func(client, *args, db=db)
            return None

        database_query = """
            SELECT [name]
            FROM sys.databases
            """
        if client.target_dbs == "user":
            database_query += " WHERE database_id > 4"
        elif client.target_dbs == "system":
            database_query += " WHERE database_id <= 4"
        else:
            pass

        output = client.engine.execute(database_query)
        for db in output:
            func(client, *args, **kwargs, db=db[0])
        return None

    return wrapper_extend_dbs