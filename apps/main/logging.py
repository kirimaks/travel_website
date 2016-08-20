import os
from apps.main.config import confs
import logging
import sys

try:
    conf = confs[os.environ['FLASK_CONFIG']]
except KeyError:
    print("( FLASK_CONFIG ) didn't set")
    sys.exit(0)

log = logging.Logger("auth")
log.addHandler(conf.X_LOG_HANDLER)
log.setLevel(conf.X_LOG_LEVEL)


def register_app(app_name):
    log.debug("New blueprint: [{}]".format(app_name))
