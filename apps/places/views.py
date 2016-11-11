from flask import render_template, request
from apps.places import places_app
from apps.places.models import Place


@places_app.route("/")
def places_list():
    page = request.args.get('page', 1, type=int)
    pagination = Place.query.order_by(Place.title)
    pagination = pagination.paginate(page, per_page=9, error_out=False)
    items = enumerate(pagination.items, start=1)
    return render_template("places-list.html", items=items,
                           pagination=pagination)


@places_app.route("/<slug>")
def show_place(slug):
    place = Place.query.filter(Place.slug == slug).first()

    if not place:
        return render_template("errors/404.html"), 404

    return render_template("place.html", place=place)
