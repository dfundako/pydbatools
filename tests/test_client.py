from pydbatools import client


def test_client_attrs():
    testclient = client.SQLClient(server="localhost")
    assert testclient.initial_catalog == "master"
    assert testclient.UID is None
    assert testclient.PWD is None
