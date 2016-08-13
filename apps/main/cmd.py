import unittest
from flask_script import Command, Option
from apps.main import db
from apps.auth.models import User, Group


class CmdTest(Command):
    """
    -t client (testing flask client)\n
       places\n
       tours\n
    """

    def __init__(self):
        self.test_type = "client"
        self.test_pattern = "test_*"

    def get_options(self):
        return [
            Option('-t', '--type', dest="test_type", default=self.test_type)
        ]

    def run(self, test_type):
        if test_type == "client":
            self.start_dir = "tests/flask_client/"
        elif test_type == "places":
            self.start_dir = "tests/places/"
        elif test_type == "tours":
            self.start_dir = "tests/tours/"

        tests = unittest.TestLoader().discover(start_dir=self.start_dir,
                                               pattern=self.test_pattern)
        if tests:
            unittest.TextTestRunner(verbosity=2).run(tests)
        else:
            print("No tests...")


def make_shell_context():
    context = {
        "db": db,
        "User": User,
        "Group": Group
    }
    return context
