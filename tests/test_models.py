import unittest
from app.models import Rectangle
from app.database import db
from app import create_app
from app.utils import intersects
from config import TestConfig


class TestRectangleModel(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_class=TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_rectangle_creation(self):
        rect = Rectangle(x1=0, y1=0, x2=1, y2=1)
        db.session.add(rect)
        db.session.commit()
        self.assertEqual(Rectangle.query.count(), 1)
        self.assertEqual(rect.x1, 0)
        self.assertEqual(rect.y1, 0)

    def test_intersection(self):
        rect = Rectangle(x1=0, y1=0, x2=1, y2=1)
        db.session.add(rect)
        db.session.commit()

        segment = ((0.5, 0.5), (1.5, 1.5))
        self.assertTrue(intersects(segment, rect))

        segment = ((1.5, 1.5), (2.5, 2.5))
        self.assertFalse(intersects(segment, rect))


if __name__ == '__main__':
    unittest.main()
