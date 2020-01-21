import math


class Dimensions:
    WIDTH = 500
    HEIGHT = 400
    TILE_SIZE = 10

    @staticmethod
    def point_distance(x0, y0, x1, y1):
        return math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

    @staticmethod
    def square_square_collision_detection(x1, y1, x2, y2, a=TILE_SIZE):
        if x1 + a > x2 and x2 + a > x1 and y1 + a > y2 and y2 + a > y1:
            return True
        return False


class Colors:
    RED = (239, 18, 18)
    TURQUOISE = (18, 231, 239)
    YELLOW = (224, 239, 18)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (30, 181, 25)
