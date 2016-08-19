from flask_admin.contrib.sqla import ModelView
from apps.places.models import Place, PlaceImage
from apps.main.admin import ProtectedAdminView
from apps.main import db, admin
from apps.comments.models import Comment

from flask_admin import form
from jinja2 import Markup
from flask import url_for
from apps.main.config import IMG_PATH, BASE_DIR
import os

from flask_admin.model.form import InlineFormAdmin


class PicUploadWithThumbnail:
    """ This class adds image uploads to the ViewModel """
    def show_thumbnail(view, context, model, name):
        if not model.path:
            return ""

        pic_path = url_for('static',
                           filename=form.thumbgen_filename(model.path))

        return Markup("<img src='{}'>".format(pic_path))

    column_formatters = {
        "path": show_thumbnail
    }

    base_path = os.path.join(BASE_DIR, 'static')

    form_extra_fields = {
        'path': form.ImageUploadField('Image',
                                      base_path=base_path,
                                      relative_path=IMG_PATH,
                                      thumbnail_size=(100, 100, True))
    }


class InlinePlacePic(PicUploadWithThumbnail, InlineFormAdmin):
    pass


class PlaceView(ProtectedAdminView, ModelView):
    @property
    def display_home(self):
        return True

    form_columns = ['title', 'slug', 'snippet', 'description',
                    'rating', 'price', 'schedule', 'info',
                    'address', 'location', 'comments', 'images']

    column_editable_list = ['location', 'price', 'rating']

    form_choices = {
        'rating': [
            ('0', 'one'),
            ('1', 'two'),
            ('2', 'tree'),
        ]
    }

    form_ajax_refs = {
        'comments': {
            'fields': [Comment.author_name, Comment.author_email],
            'page_size': 10
        }
    }
    form_widget_args = {
        'slug': {
            'disabled': True
        },
        'description': {
            'rows': 20
        }
    }

    inline_models = [InlinePlacePic(PlaceImage)]


class ImagesView(PicUploadWithThumbnail, ProtectedAdminView, ModelView):
    @property
    def display_home(self):
        return True


admin.add_view(PlaceView(Place, db.session))
admin.add_view(ImagesView(PlaceImage, db.session))
