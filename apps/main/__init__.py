from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_admin import Admin

from apps.main.admin import MyHomeView


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protect = 'strong'
login_manager.login_view = 'auth.login'
mail = Mail()
admin = Admin(name="website", template_mode='bootstrap3', index_view=MyHomeView())


def create_app(conf):
    app = Flask(__name__, static_folder="../../static")
    app.config.from_object(conf)

    app.logger.addHandler(conf.X_LOG_HANDLER)
    app.logger.setLevel(conf.X_LOG_LEVEL)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    admin.init_app(app)

    ns = create_blueprints()
    app.add_url_rule('/', 'index', ns['index'])
    app.register_blueprint(ns['places_app'], url_prefix="/places")
    app.register_blueprint(ns['tours_app'], url_prefix="/tours")
    app.register_blueprint(ns['auth_app'], url_prefix="/auth")

    app.before_request(ns['before_app_req'])

    app.logger.debug("Main app is created using config: {}".format(conf))
    return app


def create_blueprints():
    from apps.main.views import index
    from apps.places import places_app
    from apps.tours import tours_app
    from apps.auth import auth_app
    from apps.main.rq_handlers import before_app_req

    return vars()
