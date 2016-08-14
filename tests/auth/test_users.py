import unittest
from apps.auth.models import User
from faker import Factory


faker = Factory().create()
users_number = 1000


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
