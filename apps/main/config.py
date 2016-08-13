import os
import logging
from logging import StreamHandler


log_handler = StreamHandler()
formatter = logging.Formatter('%(levelname)s:\t %(message)s')
log_handler.setFormatter(formatter)

# CRITICAL    50
# ERROR   40
# WARNING 30
# INFO    20
# DEBUG   10
# NOTSET  0


class Config:
    X_LOG_HANDLER = log_handler
    X_LOG_LEVEL = logging.INFO

    SQLALCHEMY_TRACK_MODIFICATIONS = True


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
