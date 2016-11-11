import unittest
from apps.places.models import Place
from apps.main import db
from faker import Factory
from random import randrange

faker = Factory().create()
places_num = randrange(1, 500)


class CreatePlaces(unittest.TestCase):
    def shortDescription(self):
        return "Create {} places.".format(places_num)

    def test_create_places(self):
        for _ in range(places_num):
            place = Place(title=faker.address(),
                          snippet=faker.paragraph(),
                          description=faker.text(1000),
                          address=faker.street_address())
            db.session.add(place)

        db.session.commit()
