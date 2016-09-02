import os
from os.path import abspath
import logging
from logging import StreamHandler


log_handler = StreamHandler()
formatter = logging.Formatter('%(levelname)s:\t %(message)s')
log_handler.setFormatter(formatter)

BASE_DIR = str.join("/", abspath(__file__).split("/")[:-3])
IMG_PATH = "images/"    # Directory inside static, need to keep training slash.


class Config:
    X_LOG_HANDLER = log_handler
    X_LOG_LEVEL = logging.INFO

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = "c0db19f0-7083-11e6-95ba-88532eae9b6a"

    X_ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL")

    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_SUBJECT = "[Server notification]"
    MAIL_SENDER = "79649436998@yandex.ru"

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
