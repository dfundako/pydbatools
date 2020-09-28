# PyDBATools

A small library for running SQL Server tasks and maintenance

Features available:

- DBCC CheckDB
- Backup Database

## Quickstart

```Python
import pydbatools as pydba

instance_list = [
    {
        "server": "localhost",
        "UID": "sa",
        "PWD": "Password123",
        "driver": "ODBC Driver 17 for SQL Server",
        "target_dbs": "system"
    },
    {
        "server": "other_instance",
        "database": "my_database",
        "driver": "SQL Server Native Client 11.0",
        "trusted_connection": "true",
        "target_dbs": "user"
    }
]

for i in instance_list:
    client = pydba.SQLClient(**i)
    pydba.dbcc_checkdb(client)
```
