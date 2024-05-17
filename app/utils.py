from typing import Tuple


def intersects(segment: Tuple[Tuple[float, float], Tuple[float, float]],
               rectangle: 'Rectangle') -> bool:
    """
    Determine if a line segment intersects any edge of a given rectangle,
    lies entirely within the rectangle, or passes through the rectangle.

    :param segment: A tuple containing two points (x1, y1) and (x2, y2) representing the line segment.
    :param rectangle: A Rectangle object with attributes (x1, y1, x2, y2) representing the rectangle.
    :return: True if the segment intersects the rectangle in any way, False otherwise.
    """
    (x1, y1), (x2, y2) = segment

    def line_intersects(p1: Tuple[float, float], p2: Tuple[float, float],
                        q1: Tuple[float, float], q2: Tuple[float, float]) -> bool:
        # Check if line segment p1-p2 intersects with line segment q1-q2
        def ccw(A: Tuple[float, float], B: Tuple[float, float], C: Tuple[float, float]) -> bool:
            return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

        return (ccw(p1, q1, q2) != ccw(p2, q1, q2)) and (ccw(p1, p2, q1) != ccw(p1, p2, q2))

    def point_inside_rectangle(px: float, py: float, rect: 'Rectangle') -> bool:
        # Check if point (px, py) is inside the rectangle
        return (rect.x1 <= px <= rect.x2) and (rect.y1 <= py <= rect.y2)

    # Edges of the rectangle
    edges = [
        ((rectangle.x1, rectangle.y1), (rectangle.x1, rectangle.y2)),
        ((rectangle.x1, rectangle.y2), (rectangle.x2, rectangle.y2)),
        ((rectangle.x2, rectangle.y2), (rectangle.x2, rectangle.y1)),
        ((rectangle.x2, rectangle.y1), (rectangle.x1, rectangle.y1))
    ]

    # Check if the segment intersects any of the rectangle's edges
    if any(line_intersects((x1, y1), (x2, y2), edge[0], edge[1]) for edge in edges):
        return True

    # Check if either end of the segment is inside the rectangle
    if point_inside_rectangle(x1, y1, rectangle) or point_inside_rectangle(x2, y2, rectangle):
        return True

    return False
