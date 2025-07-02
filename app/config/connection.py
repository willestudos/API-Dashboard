from mongoengine import connect, disconnect

from app.config.settings import settings

connect_mongo = connect(settings.mongo_database, host=settings.host)
disconnect_mongo = disconnect


def on_appliction_startup():
    connect_mongo()


def on_appliction_shutdown():
    disconnect_mongo()
