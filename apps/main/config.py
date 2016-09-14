import os
from os.path import abspath
import logging
from logging import StreamHandler


log_handler = StreamHandler()
formatter = logging.Formatter('%(levelname)s:\t %(message)s')
log_handler.setFormatter(formatter)

BASE_DIR = str.join("/", abspath(__file__).split("/")[:-3])
IMG_PATH = "images/"    # Directory inside static, need to keep training slash.
STATIC_DIR = os.path.join(BASE_DIR, "static")


class Config:
    STATIC_DIR = STATIC_DIR
    X_LOG_HANDLER = log_handler
    X_LOG_LEVEL = logging.INFO
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "c0db19f0-7083-11e6-95ba-88532eae9b6a"

    X_ADMIN_EMAIL = os.environ["ADMIN_EMAIL"]
    MAIL_SUBJECT = "[Server notification]"
    MAIL_SENDER = "kirimakz@gmail.com"
    MJ_APIKEY_PUBLIC = os.environ['MJ_APIKEY_PUBLIC']
    MJ_APIKEY_PRIVATE = os.environ['MJ_APIKEY_PRIVATE']


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]


class DebugConfig(Config):
    DEBUG = True
    X_LOG_LEVEL = logging.DEBUG
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"


class TestingConfig(DebugConfig):
    SERVER_NAME = "127.0.0.1:5000"

confs = {
    "default": ProductionConfig(),
    "debug": DebugConfig(),
    "testing": TestingConfig(),
}
