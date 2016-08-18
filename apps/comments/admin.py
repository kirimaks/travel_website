from flask_admin.contrib.sqla import ModelView
from apps.comments.models import Comment
from apps.main.admin import ProtectedAdminView
from apps.main import db, admin


class CommentView(ProtectedAdminView, ModelView):
    @property
    def display_home(self):
        return True


admin.add_view(CommentView(Comment, db.session))
