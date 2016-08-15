from apps.main.logging import register_app
register_app(__name__)

from flask import Blueprint
from importlib import import_module

places_app = Blueprint('places', __name__, template_folder="templates")
import_module(".views", package="apps.places")
import_module(".models", package="apps.places")
import_module(".admin", package="apps.places")
