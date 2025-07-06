from unittest.mock import MagicMock

from app.config.connection import on_appliction_shutdown, on_appliction_startup


def test_on_appliction_startup_calls_connect(monkeypatch):
    mock_connect = MagicMock()
    monkeypatch.setattr("app.config.connection.connect_mongo", mock_connect)

    on_appliction_startup()

    mock_connect.assert_called_once()


def test_on_appliction_shutdown_calls_disconnect(monkeypatch):
    mock_disconnect = MagicMock()
    monkeypatch.setattr("app.config.connection.disconnect_mongo", mock_disconnect)

    on_appliction_shutdown()

    mock_disconnect.assert_called_once()
