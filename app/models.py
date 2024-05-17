from .database import db
from .utils import intersects


class Rectangle(db.Model):
    __tablename__ = 'rectangles'
    id = db.Column(db.Integer, primary_key=True)
    x1 = db.Column(db.Float)
    y1 = db.Column(db.Float)
    x2 = db.Column(db.Float)
    y2 = db.Column(db.Float)

    def serialize(self):
        return {
            'id': self.id,
            'x1': self.x1,
            'y1': self.y1,
            'x2': self.x2,
            'y2': self.y2
        }

    @classmethod
    def find_intersecting(cls, segment):
        all_rectangles = cls.query.all()
        print(f"Segment: {segment}")
        for rect in all_rectangles:
            print(f"Checking rectangle: {rect.serialize()}")
        return [rect for rect in all_rectangles if intersects(segment, rect)]
