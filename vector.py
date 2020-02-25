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
    
    def add(self, vector):
        """add vector"""
        self.x += vector.x
        self.y += vector.y
        return self
    
    def get_normal(self):
        """get right (or left) normal"""
        return Vector(-self.y, self.x)
#         return Vector(self.y, -self.x)

    def set_mag(self, value):
        pass
    
    def get_length(self):
        pass

    def perpendicular_shift(self, shift_value):
        """shifts another vector perpendicularly"""
        self.x += -shift_value
        self.y += shift_value
        return self

    def paint_image_out(self, jpeg_origin, length, shift_value, drawing_object):
        """paints the image"""
        origin = jpeg_origin
        self.multiply(length * 2)
        for i in range(0, length):
            drawing_object.line((origin.x, origin.y, self.x, self.y), fill=0, width=1)
            origin.perpendicular_shift(shift_value)
            self.perpendicular_shift(shift_value)
        return None

