import unittest
from app import create_app, db
from app.models import Rectangle
import json
from config import TestConfig


class TestApi(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_class=TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

        # Add some rectangles for testing
        rect1 = Rectangle(x1=0, y1=0, x2=1, y2=1)
        rect2 = Rectangle(x1=1, y1=1, x2=2, y2=2)
        db.session.add_all([rect1, rect2])
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_intersect_endpoint(self):
        response = self.client.post('/intersect', json={
            'x1': 0, 'y1': 0, 'x2': 1, 'y2': 1
        })
        data = json.loads(response.data)
        self.assertEqual(len(data), 2)
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/intersect', json={
            'x1': 1.5, 'y1': 1.5, 'x2': 2.5, 'y2': 2.5
        })
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
