def backup_database(client, **kwargs):
    """[summary]

    :param SQLClient: [description]
    :type SQLClient: [type]
    """
    print("Hello!")


def dbcc_checkdb(client, **kwargs):
    """[summary]

    :param SQLClient: [description]
    :type SQLClient: [type]
    """

    output = client.engine.execute(
        """
        DBCC CHECKDB
        """
    )
    return output


def dbcc_checkfilegroup(client, **kwargs):
    """[summary]

    :param SQLClient: [description]
    :type SQLClient: [type]
    """

    output = client.engine.execute(
        """
        DBCC CHECKFILEGROUP
        """
    )
    return output


def dbcc_checktable(client, **kwargs):
    """[summary]

    :param SQLClient: [description]
    :type SQLClient: [type]
    """

    output = client.engine.execute(
        """
        DBCC CHECKTABLE
        """
    )
    return output


def dbcc_checkalloc(client, **kwargs):
    """[summary]

    :param SQLClient: [description]
    :type SQLClient: [type]
    """

    output = client.engine.execute(
        """
        DBCC CHECKALLOC
        """
    )
    return output


def dbcc_checkcatalog(client, **kwargs):
    """[summary]

    :param SQLClient: [description]
    :type SQLClient: [type]
    """

    output = client.engine.execute(
        """
        DBCC CHECKCATALOG
        """
    )
    return output
