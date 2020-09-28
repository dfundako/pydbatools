import pydbatools as pydba

instance_list = [
    {
        "server": "localhost",
        "UID": "sa",
        "PWD": "Password123",
        "driver": "ODBC Driver 17 for SQL Server",
        "autocommit": True,
        "target_dbs": "system",
    },
]

for i in instance_list:
    client = pydba.SQLClient(**i)
    print(client.engine)
    pydba.dbcc_checkdb(client)
    pydba.backup_db(client, to_disk_location="/var/opt/mssql/data/")