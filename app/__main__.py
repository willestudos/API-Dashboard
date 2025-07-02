import uvicorn
from config.settings import settings


def main() -> None:
    """
    Main Function
    """
    uvicorn.run(
        "app.application:get_app",
        host=settings.host,
        port=settings.fastapi_port,
        reload=True,
        log_level=settings.log_level,
        factory=True,
    )


if __name__ == "__main__":
    main()
