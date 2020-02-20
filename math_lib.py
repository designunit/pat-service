import math
from vector import Vector


def from_angle(image_size, degrees):
    """rotates the vector"""
    angle = math.radians(degrees)
    return Vector(math.cos(angle) * (image_size*2), math.sin(angle) * (image_size*2))

