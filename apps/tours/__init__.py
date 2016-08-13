from apps.main.logging import register_app
register_app(__name__)

from importlib import import_module
from flask import Blueprint

tours_app = Blueprint('tours', __name__, template_folder="templates")

import_module(".views", package="apps.tours")
