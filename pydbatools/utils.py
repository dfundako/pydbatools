import urllib


def make_connection_string(client) -> str:
    """[summary]

    :param driver: [description]
    :type driver: [type]
    :param server: [description]
    :type server: [type]
    :param trusted_connection: [description]
    :type trusted_connection: [type]
    :param UID: [description]
    :type UID: [type]
    :param PWD: [description]
    :type PWD: [type]
    """

    params = urllib.parse.quote_plus(
        "DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={UID};PWD={PWD}".format(
            server=client.server,
            database=client.database,
            UID=client.UID,
            PWD=client.PWD,
        )
    )
    return params
