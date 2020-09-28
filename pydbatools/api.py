from . import utils
import pyodbc


@utils.extend_dbs
def dbcc_checkdb(client, **kwargs):
    """Executes DBCC CHECKDB

    :param SQLClient: [description]
    :type SQLClient: [type]
    """
    client.engine.execute("DBCC CHECKDB ({db_name})".format(db_name=kwargs["db"]))
    print(kwargs["db"])

    return None


@utils.extend_dbs
def backup_db(client, **kwargs):
    """Executes database backup with options

    :param SQLClient: [description]
    :type SQLClient: [type]
    """
    if kwargs["db"] == "tempdb":
        return None
    backup_str = "BACKUP DATABASE [{db_name}] TO DISK = N'{to_disk_location}\{db_name}.bak' WITH INIT, NAME='{db_name}', NOSKIP, NOFORMAT".format(
        db_name=kwargs["db"], to_disk_location=kwargs["to_disk_location"]
    )
    if kwargs.get("differential", ""):
        backup_str += " WITH DIFFERENTIAL;"

    client.connection = pyodbc.connect(
        driver=client.driver,
        server=client.server,
        database=client.database,
        autocommit=True,
        UID=client.UID,
        PWD=client.PWD,
    )

    cursor = client.connection.cursor().execute(backup_str)
    while cursor.nextset():
        pass
    client.connection.close()
    print(kwargs["db"])

    return None
