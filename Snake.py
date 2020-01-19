import pygame
import math


class Dimensions:
    WIDTH = 500
    HEIGHT = 400

    @staticmethod
    def d(x0, y0, x1, y1):
        center0_x = x0 / 2
        center0_y = y0 / 2
        center1_x = x1 / 2
        center1_y = y1 / 2
        return math.floor(math.sqrt((center0_x - center1_x) ** 2 + (center0_y - center1_y) ** 2))


class Colors:
    RED = (239, 18, 18)
    TURQUOISE = (18, 231, 239)
    YELLOW = (224, 239, 18)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (30, 181, 25)


class Snake:
    def __init__(self, surface, head_x, head_y):
        self.head_x = head_x
        self.head_y = head_y
        self.tail = 0
        self.surface = surface
        pygame.draw.rect(self.surface, Colors.WHITE, (self.head_x, self.head_y, 10, 10))


class Fruit:
    def __init__(self, surface, x, y):
        self.x = x
        self.y = y
        self.surface = surface
        pygame.draw.rect(self.surface, Colors.GREEN, (self.x, self.y, 10, 10))


class Enemy:
    def __init__(self, surface, x, y, r, g, b):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
        pygame.draw.circle(surface, (self.r, self.g, self.b), (self.x, self.y), 12)
