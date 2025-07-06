import subprocess
import sys
from unittest.mock import MagicMock, patch

from app.__main__ import main


def test_main_calls_uvicorn_run_correctly():
    """
    Garante que a função main() invoca uvicorn.run com os parâmetros corretos.
    """
    mock_settings = MagicMock()
    mock_settings.host = "127.0.0.1"
    mock_settings.fastapi_port = 8080
    mock_settings.log_level = "info"
    mock_settings.reload = True

    with (
        patch("app.__main__.uvicorn.run") as mock_uvicorn_run,
        patch("app.__main__.settings", mock_settings),
    ):
        main()

        mock_uvicorn_run.assert_called_once_with(
            "app.application:get_app",
            host="127.0.0.1",
            port=8080,
            reload=True,
            log_level="info",
            factory=True,
        )


def test_main_script_runs(monkeypatch):
    main_path = "app/__main__.py"
    result = subprocess.run([sys.executable, main_path], capture_output=True, text=True)
    assert result.returncode == 1
