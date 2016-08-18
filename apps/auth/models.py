from flask import current_app
from apps.main import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy.orm import relationship, backref


# Required by flask-login.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


user2group = db.Table('user2group', db.Model.metadata,
                      db.Column("user_id", db.Integer,
                                db.ForeignKey("users.id")),
                      db.Column("group_id", db.Integer,
                                db.ForeignKey("user_groups.id")))


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String(128), unique=True)
    confirmed = db.Column(db.Boolean, default=False)

    groups = relationship("UserGroup", secondary=user2group,
                          backref=backref('users', order_by=id))

    def __repr__(self):
        return "<{}>".format(self.username)

    @property
    def password(self):
        raise AttributeError("Password is not readable")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False

        if data.get("confirm") != self.id:
            return False

        self.confirmed = True
        current_app.logger.info("User {} confirmed".format(self.username))
        db.session.add(self)
        db.session.commit()
        return True


class UserGroup(db.Model):
    __tablename__ = "user_groups"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    def __repr__(self):
        return "<{}>".format(self.name)
