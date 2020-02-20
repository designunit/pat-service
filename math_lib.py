import math


def get_radians(degrees):
    """converts degrees to radians"""
    radians = math.radians(degrees)
    return radians


def get_coordinates(direction, radians):
    """gets direction for the vector"""
    print(math.tan(get_radians(radians)))
    return direction * math.tan(get_radians(radians))


def get_vector_origin(image_size):
    return image_size / 2

