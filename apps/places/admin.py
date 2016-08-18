from flask_admin.contrib.sqla import ModelView
from apps.places.models import Place
from apps.main.admin import ProtectedAdminView
from apps.main import db, admin
from apps.comments.models import Comment


class ModelViewSec(ProtectedAdminView, ModelView):
    @property
    def display_home(self):
        return True

    form_ajax_refs = {
        'comments': {
            'fields': [Comment.author_name, Comment.author_email],
            'page_size': 10
        }
    }

admin.add_view(ModelViewSec(Place, db.session))
