import unittest
from apps.main import db
from apps.auth.models import User
from faker import Factory
from random import randrange


faker = Factory().create()
users_number = randrange(1, 1000)


class TestUser(unittest.TestCase):
    def shortDescription(self):
        return "[[ Generate %s users ]]\n" % (users_number,)

    def test_password_setter(self):
        for _ in range(users_number):
            u = User(password=faker.password())
            self.assertTrue(u.password_hash)

    def test_confirmation(self):
        for _ in range(users_number):
            u = User(password=faker.password())
            self.assertFalse(u.confirmed)


class CreateUsers(unittest.TestCase):
    def shortDescription(self):
        return "[[ Create %s users ]]" % (users_number)

    def test_create_users(self):
        for _ in range(users_number):

            username = "{}_{}".format(faker.user_name(), str(randrange(0, 99)))
            email = "{}{}".format(str(randrange(0, 99)), faker.email())

            user = User(username=username,
                        password=faker.password(),
                        email=email)
            db.session.add(user)
        db.session.commit()
