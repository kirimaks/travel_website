from flask_admin.contrib.sqla import ModelView
from apps.tours.models import Tour
from apps.main.admin import ProtectedAdminView
from apps.main import db, admin


class ModelViewSec(ProtectedAdminView, ModelView):
    @property
    def display_home(self):
        return True

admin.add_view(ModelViewSec(Tour, db.session))
