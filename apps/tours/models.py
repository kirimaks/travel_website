from apps.main import db


class Tour(db.Model):
    __tablename__ = "tours"
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(64), unique=True)
    price = db.Column(db.String(64))

    duration = db.Column(db.String(64))
    min_people_number = db.Column(db.Integer)
    distance = db.Column(db.Integer)
