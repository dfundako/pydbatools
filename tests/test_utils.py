import urllib.parse
from pydbatools import utils
from pydbatools import client


def test_make_connection_string(monkeypatch):
    def mock_quote_plus(client):
        return "TestConnString"

    monkeypatch.setattr(urllib.parse, "quote_plus", mock_quote_plus)
    mock_client = client.SQLClient("localhost", driver="testdriver")
    output = utils.make_connection_string(mock_client)

    assert output is not None