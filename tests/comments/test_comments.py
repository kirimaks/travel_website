import unittest
from apps.comments.models import Comment
from apps.main import db
from random import randrange
from faker import Factory

faker = Factory().create()


comment_number = randrange(1, 10000)


class CreateTests(unittest.TestCase):
    def shortDescription(self):
        return "Create %s comments" % comment_number

    def test_createComments(self):
        for _ in range(comment_number):
            comment = Comment(author_name=faker.user_name(),
                              author_email=faker.email(),
                              text=faker.text())

            db.session.add(comment)
        db.session.commit()
