import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def from_angle(radians):
        """rotates the vector"""
        return Vector(math.cos(radians), math.sin(radians))

    def multiply(self, length):
        self.x *= length
        self.y *= length
        return self
