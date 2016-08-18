from apps.main import db
from apps.comments.models import Comment


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

    duration = db.Column(db.String(64))
    min_people_number = db.Column(db.Integer)
    distance = db.Column(db.Integer)

    places = db.relationship("Place", secondary=places2tours,
                             backref="places")

    comments = db.relationship(Comment, secondary=comments2tours)
