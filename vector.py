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

    def paint_pattern(self, origin, img_size, shift, drawing_object):
        for i in range(0, img_size):
            drawing_object.line((origin.x, origin.y, self.x, self.y), fill=0, width=1)
            origin.perpendicular_shift(shift)
            self.perpendicular_shift(shift)
        return None
