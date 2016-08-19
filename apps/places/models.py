from apps.main import db
from sqlalchemy import CheckConstraint
from apps.comments.models import Comment


comments2places = db.Table("comments2places", db.metadata,
                           db.Column("comment_id", db.Integer,
                                     db.ForeignKey("comments.id")),
                           db.Column("place_id", db.Integer,
                                     db.ForeignKey("places.id")))


class Place(db.Model):
    __tablename__ = "places"
    __table_args__ = (CheckConstraint('rating >= 0 and rating <= 5',
                                      name="rating_0_5"),)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    snippet = db.Column(db.Text, index=True)
    description = db.Column(db.Text, index=True)

    rating = db.Column(db.Integer, default=0)
    price = db.Column(db.String(64))
    schedule = db.Column(db.Text)
    info = db.Column(db.Text)
    address = db.Column(db.String(128))
    location = db.Column(db.String(64))

    comments = db.relationship(Comment, secondary=comments2places)
    images = db.relationship("PlaceImage", backref="place")

    def __repr__(self):
        return self.title


class PlaceImage(db.Model):
    __tablename__ = "place_images"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    path = db.Column(db.String(256), unique=True)

    place_id = db.Column(db.Integer, db.ForeignKey("places.id"))

    def __repr__(self):
        return "{} | {}".format(self.name, self.path)
