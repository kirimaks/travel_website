from apps.main import db

places_to_tours = db.Table("places_to_tours", db.Model.metadata,
                           db.Column("place_id", db.Integer,
                                     db.ForeignKey("places.id")),
                           db.Column("tour_id", db.Integer,
                                     db.ForeignKey("tours.id")))


class Tour(db.Model):
    __tablename__ = "tours"
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(64), unique=True)
    price = db.Column(db.String(64))

    duration = db.Column(db.String(64))
    min_people_number = db.Column(db.Integer)
    distance = db.Column(db.Integer)

    places = db.relationship("Place", secondary=places_to_tours,
                             backref="places")
