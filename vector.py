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

    def paint_image_out(self, origin, length, shift_value, drawing_object):
        """paints the image"""
        __origin = origin
        self.multiply(length * 2)
        for i in range(0, length):
            drawing_object.line((__origin.x, __origin.y, self.x, self.y), fill=0, width=1)
            __origin.perpendicular_shift(shift_value)
            self.perpendicular_shift(shift_value)
        __origin = origin
        return None

