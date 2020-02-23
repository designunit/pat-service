import math


class Vector:
    def __init__(self, x, y):
        """basic vector object"""
        self.x = x
        self.y = y

    @staticmethod
    def from_angle(radians):
        """rotates the vector"""
        return Vector(math.cos(radians), math.sin(radians))

    def multiply(self, length):
        """scales vector in two directions"""
        self.x *= length
        self.y *= length
        return self

    def perpendicular_shift(self, shift_value):
        """shifts another vector perpendicularly"""
        self.x += -shift_value
        self.y += shift_value
        return self

