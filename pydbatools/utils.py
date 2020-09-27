import urllib


def make_connection_string(client) -> str:
    """Generate connection string to be used by SQLAlchemy."""

    params = urllib.parse.quote_plus(
        "DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={UID};PWD={PWD}".format(
            driver=client.driver,
            server=client.server,
            database=client.initial_catalog,
            UID=client.UID,
            PWD=client.PWD,
        )
    )
    return params


def extend_dbs(func):
    """Decorator to retrieve additional databases and run functions against each"""

    def wrapper_extend_dbs(client, *args, **kwargs):
        if not kwargs.get("db_type", ""):
            func(client, *args, db=client.initial_catalog)
            return None

        database_query = """
            SELECT [name]
            FROM sys.databases
            """
        if kwargs.get("db_type", "") == "user":
            database_query += " WHERE database_id > 4"
        elif kwargs.get("db_type", "") == "system":
            database_query += " WHERE database_id <= 4"
        else:
            pass

        output = client.engine.execute(database_query)
        for db in output:
            func(client, *args, db=db[0])
        return None

    return wrapper_extend_dbs