from . import utils
from .client import SQLClient


@utils.extend_dbs
def dbcc_checkdb(client: SQLClient, **kwargs):
    """Executes DBCC CHECKDB

    :param SQLClient: [description]
    :type SQLClient: [type]
    """
    client.engine.execute("DBCC CHECKDB ({db_name})".format(db_name=kwargs["db"]))
    print(kwargs["db"])

    return None
