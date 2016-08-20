import os
from os.path import abspath
import logging
from logging import StreamHandler
import uuid


log_handler = StreamHandler()
formatter = logging.Formatter('%(levelname)s:\t %(message)s')
log_handler.setFormatter(formatter)

BASE_DIR = str.join("/", abspath(__file__).split("/")[:-3])
IMG_PATH = "images/"    # Directory inside static, need to keep training slash.


class Config:
    X_LOG_HANDLER = log_handler
    X_LOG_LEVEL = logging.INFO

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # SECRET_KEY = uuid.uuid4().hex
    SECRET_KEY = "c0db19f0-7083-11e6-95ba-88532eae9b6a"

    X_ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL")

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_SUBJECT = "[Server notification]"
    MAIL_SENDER = "kirimakz@gmail.com"

    def validate(self):
        assert self.X_ADMIN_EMAIL, "Admin email didn't set ( ADMIN_EMAIL )"
        assert self.MAIL_USERNAME, "No mail user ( MAIL_USERNAME )"
        assert self.MAIL_PASSWORD, "No mail password ( MAIL_PASSWORD )"


class ProductionConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")

    def validate(self):
        Config.validate(self)    # Validate basic config.
        assert self.SQLALCHEMY_DATABASE_URI, "( SQLALCHEMY_DATABASE_URI )"


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
