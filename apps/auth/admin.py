from flask_admin.contrib.sqla import ModelView
from apps.auth.models import User, UserGroup
from apps.main.admin import ProtectedAdminView
from apps.main import db, admin


class UserView(ProtectedAdminView, ModelView):
    column_display_pk = True
    form_widget_args = {
        'password_hash': {
            'disabled': True
        },
        'confirmed': {
            'style': 'width: 20px'
        }
    }

    form_ajax_refs = {
        'groups': {
            'fields': (UserGroup.name,),
        }
    }

    @property
    def display_home(self):
        return True


class GroupView(ProtectedAdminView, ModelView):
    @property
    def display_home(self):
        return True

admin.add_view(UserView(User, db.session))
admin.add_view(GroupView(UserGroup, db.session))
