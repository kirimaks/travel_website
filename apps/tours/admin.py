from flask_admin.contrib.sqla import ModelView
from apps.tours.models import Tour
from apps.main.admin import ProtectedAdminView
from apps.main import db, admin
from apps.places.models import Place


class ModelViewSec(ProtectedAdminView, ModelView):
    @property
    def display_home(self):
        return True

    form_ajax_refs = {
        'places': {
            'fields': [Place.title],
            'page_size': 10
        }
    }

admin.add_view(ModelViewSec(Tour, db.session))
