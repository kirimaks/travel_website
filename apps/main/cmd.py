import unittest
from flask_script import Command, Option
from apps.main import db
from apps.auth.models import User, UserGroup
from flask import current_app
import sys


class CmdTest(Command):
    """
-t [client] (testing flask client)\n
[places]\n
[tours]\n
[auth]\n
[comments]\n
    """

    def __init__(self):
        self.test_type = "client"
        self.test_pattern = "test_*"

        self.test_path_dict = {
            "client": "tests/flask_client/",
            "places": "tests/places",
            "tours": "tests/tours",
            "auth": "tests/auth",
            "comments": "tests/comments"
        }

    def get_options(self):
        return [
            Option('-t', '--type', dest="test_type", default=self.test_type)
        ]

    def run(self, test_type):
        try:
            start_dir = self.test_path_dict[test_type]
        except KeyError:
            print("No tests for [{}]...".format(test_type))
            sys.exit(1)

        tests = unittest.TestLoader().discover(start_dir=start_dir,
                                               pattern=self.test_pattern)
        unittest.TextTestRunner(verbosity=2).run(tests)


def make_shell_context():
    context = {
        "db": db,
        "User": User,
        "UserGroup": UserGroup,
        "app": current_app
    }
    return context


class CmdAdmin(Command):
    def run(self):
        print("Create admin")

        from apps.auth.models import User
        admin = User(username="admin", password="1234",
                     email="kirimaks@yahoo.com",
                     confirmed=True)
        db.session.add(admin)
        db.session.commit()
