from flask import Blueprint, request, jsonify
from .models import Rectangle

api_bp = Blueprint('api', __name__)


@api_bp.route('/intersect', methods=['POST'])
def intersect():
    data = request.get_json()
    segment = ((data['x1'], data['y1']), (data['x2'], data['y2']))
    rectangles = Rectangle.find_intersecting(segment)
    return jsonify([rect.serialize() for rect in rectangles])
