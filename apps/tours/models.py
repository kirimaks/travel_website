from apps.main import db
from apps.comments.models import Comment
from slugify import slugify_ru
from sqlalchemy import event


places2tours = db.Table("places2tours", db.Model.metadata,
                        db.Column("place_id", db.Integer,
                                  db.ForeignKey("places.id")),
                        db.Column("tour_id", db.Integer,
                                  db.ForeignKey("tours.id")))

comments2tours = db.Table("comments2tours", db.Model.metadata,
                          db.Column("comment_id", db.Integer,
                                    db.ForeignKey("comments.id")),
                          db.Column("tour_id", db.Integer,
                                    db.ForeignKey("tours.id")))


class Tour(db.Model):
    __tablename__ = "tours"
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(64), unique=True)
    price = db.Column(db.String(64))
    slug = db.Column(db.String(256), unique=True)

    duration = db.Column(db.String(64))
    min_people_number = db.Column(db.Integer)
    distance = db.Column(db.Integer)

    places = db.relationship("Place", secondary=places2tours,
                             backref="places")

    comments = db.relationship(Comment, secondary=comments2tours)

    def __repr__(self):
        return self.title

    def generate_slug(self, title):
        """ Generate slug by title """
        self.slug = slugify_ru(title, to_lower=True)


@event.listens_for(Tour.title, 'set')
def create_slug(target, value, oldvalue, initiator):
    target.generate_slug(value)
