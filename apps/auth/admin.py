from flask import request, url_for, redirect
from flask_login import current_user
from apps.auth.models import User, UserGroup
from apps.main import db, admin
from flask_admin.contrib.sqla import ModelView


class ModelViewSec(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))

admin.add_view(ModelViewSec(User, db.session))
admin.add_view(ModelViewSec(UserGroup, db.session))
