import os
from apps.main.config import confs
import logging

conf = confs[os.environ['FLASK_CONFIG']]

log = logging.Logger("auth")
log.addHandler(conf.X_LOG_HANDLER)
log.setLevel(conf.X_LOG_LEVEL)


def register_app(app_name):
    log.debug("New blueprint: [{}]".format(app_name))
