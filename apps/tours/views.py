from flask import render_template
from apps.tours import tours_app


@tours_app.route("/")
def tours_list():
    return render_template("tours-list.html")
