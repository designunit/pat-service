import math
from vector import Vector


def from_angle(radians):
    """rotates the vector"""
    return Vector(math.cos(radians), math.sin(radians))

