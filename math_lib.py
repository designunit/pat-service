import math


def rotate_vector_sin_cos(image_size, degrees):
    """rotates the vector"""
    x_y = [0, 0]
    length = image_size * 2
    angle = math.radians(degrees)
    x_y[0] = math.cos(angle) * length
    x_y[1] = math.sin(angle) * length
    return x_y

