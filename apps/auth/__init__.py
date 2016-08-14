from apps.main.logging import register_app
register_app(__name__)

from flask import Blueprint

auth_app = Blueprint('auth', __name__, template_folder="templates")

from importlib import import_module
import_module(".admin", package="apps.auth")
import_module(".models", package="apps.auth")
import_module(".views", package="apps.auth")
