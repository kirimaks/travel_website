from importlib import import_module

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from apps.main.views import index

from apps.places import places_app
from apps.tours import tours_app


bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(conf):
    app = Flask(__name__)
    app.config.from_object(conf)

    app.logger.addHandler(conf.X_LOG_HANDLER)
    app.logger.setLevel(conf.X_LOG_LEVEL)

    bootstrap.init_app(app)
    db.init_app(app)

    app.add_url_rule('/', 'index', index)
    app.register_blueprint(places_app, url_prefix="/places")
    app.register_blueprint(tours_app, url_prefix="/tours")

    app.logger.debug("Main app is created using config: {}".format(conf))
    return app


def create_apps():
    import_module("apps.auth")
    import_module("apps.places")
    import_module("apps.tours")
