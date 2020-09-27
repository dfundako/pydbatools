from pydbatools.utils import make_connection_string
from . import exceptions, utils

from sqlalchemy import create_engine


class SQLClient:
    """[summary]
    """

    def __init__(
        self, server, **kwargs,
    ):
        self.server = server
        self.databases = kwargs.get("database", "master")
        self.UID = kwargs["UID", None]
        self.PWD = kwargs["PWD", None]

        self.params = make_connection_string(self)

        self.engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % self.params)

    # def gather_dbs(self, type="all"):
    #     """[summary]
    #     """
    #     if type not in ["all", "user", "system"]:
    #         raise ValueError("argument Type must be all, user, or system")
    #     if type == "system":
    #         where_clause = "WHERE database_id <= 4"
    #     elif type == "user":
    #         where_clause = "WHERE database_id > 4"
    #     else:
    #         where_clause = ""

    #     self.database

