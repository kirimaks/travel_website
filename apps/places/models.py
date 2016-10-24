from apps.main import db
from sqlalchemy import CheckConstraint
from apps.comments.models import Comment
from sqlalchemy import event
from slugify import slugify_ru


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

    rating = db.Column(db.Integer)
    price = db.Column(db.String(64))
    schedule = db.Column(db.Text)
    info = db.Column(db.Text)
    address = db.Column(db.String(128))
    location = db.Column(db.String(64))

    slug = db.Column(db.String(128), unique=True)

    comments = db.relationship(Comment, secondary=comments2places)
    images = db.relationship("PlaceImage", backref="place")

    def __repr__(self):
        return self.title

    def generate_slug(self, title):
        """ Generate slug by title """
        self.slug = slugify_ru(title, to_lower=True)


@event.listens_for(Place, 'before_insert')
def create_slug(mapper, connection, target):
    target.generate_slug(target.title)


class PlaceImage(db.Model):
    __tablename__ = "place_images"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    path = db.Column(db.String(256), unique=True)

    place_id = db.Column(db.Integer, db.ForeignKey("places.id"))

    def __repr__(self):
        return "{} | {}".format(self.name, self.path)
