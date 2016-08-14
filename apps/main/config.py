import os
import logging
from logging import StreamHandler
import uuid


log_handler = StreamHandler()
formatter = logging.Formatter('%(levelname)s:\t %(message)s')
log_handler.setFormatter(formatter)


class Config:
    X_LOG_HANDLER = log_handler
    X_LOG_LEVEL = logging.INFO

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = uuid.uuid4().hex

    X_ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL")

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_SUBJECT = "[Server notification]"
    MAIL_SENDER = "kirimakz@gmail.com"


class DebugConfig(Config):
    X_LOG_LEVEL = logging.DEBUG

    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"


class TestingConfig(DebugConfig):
    SERVER_NAME = "127.0.0.1:500"

confs = {
    "default": Config,
    "debug": DebugConfig,
    "testing": TestingConfig,
}
