import math


def rotate_vector_sin_cos(image_size, degrees):
    """rotates the vector"""
    x_y = [0, 0]
    angle = math.radians(degrees)
    x_y[0] = math.cos(angle) * image_size
    x_y[1] = math.sin(angle) * image_size
    return x_y

