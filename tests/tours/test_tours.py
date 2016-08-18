import unittest
from apps.tours.models import Tour
from apps.main import db
from faker import Factory
from random import randrange

faker = Factory().create()
tours_num = randrange(1, 500)


class CreateTrous(unittest.TestCase):
    def shortDescription(self):
        return "Create {} tours.".format(tours_num)

    def test_create_places(self):
        for _ in range(tours_num):
            tour = Tour(title=faker.address())
            db.session.add(tour)

        db.session.commit()
