from . import exceptions, utils

from sqlalchemy import create_engine


class SQLClient:
    """Main client object needed for executing tasks."""

    def __init__(
        self,
        server,
        **kwargs,
    ):
        self.server = server
        self.initial_catalog = kwargs.get("database", "master")
        self.UID = kwargs.get("UID", None)
        self.PWD = kwargs.get("PWD", None)
        self.driver = kwargs.get("driver", None)

        self.params = utils.make_connection_string(self)

        self.engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % self.params)
