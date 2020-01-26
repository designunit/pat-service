import math


def get_radians(degrees):
    """converts degrees to radians"""
    radians = math.radians(degrees)
    return radians


def get_coordinates(radians):
    """"""
    return math.sin(radians)


def test(obj, drawing_object):
    for i in obj[1::1]:
        for inc in obj:
            drawing_object.line((i, i, i, i), fill=0, width=1)
    return None
