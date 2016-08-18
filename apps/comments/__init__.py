from apps.main.logging import register_app
register_app(__name__)

from importlib import import_module
import_module(".models", package="apps.comments")
import_module(".admin", package="apps.comments")
