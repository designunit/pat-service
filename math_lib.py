import math


def get_radians(degrees):
    """converts degrees to radians"""
    radians = math.radians(degrees)
    return radians


def get_coordinates(radians):
    """"""
    return math.sin(radians)


def get_vector_origin(image_size):
    return image_size/2
