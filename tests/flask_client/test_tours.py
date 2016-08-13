import unittest
from flask import url_for

import os.path
import sys
base_dir = os.path.dirname(os.path.abspath(__name__))
sys.path.append(base_dir)

from apps.main import create_app
from apps.main.config import confs


class FlaskClient(unittest.TestCase):
    def shortDescription(self):
        return "<<< Testing tours >>>\n"

    def setUp(self):
        self.app = create_app(confs["testing"])
        self.app_context = self.app.app_context()

        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

    def test_tours(self):
        response = self.client.get(url_for('tours.tours_list'))
        self.assertTrue("Tours" in response.get_data(as_text=True))
