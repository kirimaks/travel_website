from apps.main import db
from datetime import datetime


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(64), nullable=False)
    author_email = db.Column(db.String(64), nullable=False)
    text = db.Column(db.Text, nullable=False)
    posted_time = db.Column(db.DateTime, default=datetime.utcnow())
