import pydbatools as pydba


instance_list = [
    {
        "server": "localhost",
        "UID": "sa",
        "PWD": "Password123",
        "driver": "ODBC Driver 17 for SQL Server",
    }
]

for i in instance_list:
    client = pydba.SQLClient(
        i["server"], UID=i["UID"], PWD=i["PWD"], driver=i["driver"]
    )

    pydba.api.dbcc_checkdb(client, db_type="system")
