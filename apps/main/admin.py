print("--lala--")
from flask import redirect, request, url_for
from flask_admin import BaseView, expose, AdminIndexView
from flask_login import current_user


class MyHomeView(AdminIndexView):
    @expose('/')
    def index(self):
        # arg1 = 'Hello'
        # return self.render('admin/myhome.html', arg1=arg1)
        return self.render("admin/index.html")

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('auth.login', next=request.url))
