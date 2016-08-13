from flask import render_template
from apps.places import places_app


@places_app.route("/")
def places_list():
    return render_template("places-list.html")
