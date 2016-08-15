import os.path
from flask import redirect, request, url_for
from flask_login import current_user

from flask_admin import expose, AdminIndexView
from flask_admin.menu import MenuLink
from flask_admin.contrib.fileadmin import FileAdmin

from apps.main.config import BASE_DIR


class ProtectedAdminView():
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))

    def is_visible(self):
        """ Every view is not visible in the menu by default """
        return False

    @property
    def display_home(self):
        """ Set to True in childrent to display on home page """
        return False


class MyAdminHomeView(ProtectedAdminView, AdminIndexView):
    @expose('/')
    def index(self):
        from apps.main import admin
        admin_views = [view for view in admin._views if view.display_home]
        return self.render("admin/admin-index.html",
                           user=current_user.username,
                           admin_views=admin_views)


class MyFileAdmin(ProtectedAdminView, FileAdmin):
    pass


def create_admin_menu():
    from apps.main import admin

    class MyMenuLink(MenuLink):
        def is_active(self, view):
            if request.path.rstrip('/') == self.url.rstrip('/'):
                return True

    admin.add_menu_item(MyMenuLink(name="Models", url='/admin'))
    admin.add_menu_item(MyMenuLink(name="Files", url="/admin/myfileadmin"))
    # admin.add_link(MyMenuLink(name="Api", url="/admin"))


def admin_files_managing():
    from apps.main import admin
    files_dir = os.path.join(BASE_DIR, "static")

    for view in admin._views:
        if isinstance(view, MyFileAdmin):
            break
    else:
        admin.add_view(MyFileAdmin(files_dir, endpoint="myfileadmin"))
