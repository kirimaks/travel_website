from flask_admin.contrib.sqla import ModelView
from apps.tours.models import Tour
from apps.main.admin import ProtectedAdminView
from apps.main import db, admin
from apps.places.models import Place
from apps.comments.models import Comment


class ModelViewSec(ProtectedAdminView, ModelView):
    @property
    def display_home(self):
        return True

    form_columns = ['title', 'slug', 'price', 'duration',
                    'min_people_number', 'distance']

    form_widget_args = {
        'slug': {
            'disabled': True
        }
    }

    form_ajax_refs = {
        'places': {
            'fields': [Place.title],
            'page_size': 10
        },
        'comments': {
            'fields': [Comment.author_name, Comment.author_email],
            'page_size': 5
        }
    }

admin.add_view(ModelViewSec(Tour, db.session))
