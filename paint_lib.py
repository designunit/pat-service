import math

from PIL import Image, ImageDraw
from vector import Vector
from patternline import PatternLine


def draw_by_pattern_JPEG(parsed_pattern, img_size, background_color):
    """main function for drawing JPEG"""
    local_image = Image.new('RGB', img_size, background_color)
    drawing_object = ImageDraw.Draw(local_image)

    # tmshvs' point of view, why?
    jpeg_origin = Vector(parsed_pattern[1], parsed_pattern[2])

    # supposed to be parsed from file
    local_pattern = PatternLine(parsed_pattern[0], jpeg_origin, parsed_pattern[3],
                                parsed_pattern[4], parsed_pattern[5], parsed_pattern[6])

    # test value for simplicity
    shift = 15

    # draws from origin to bottom of the image
    # jpeg_origin = Vector(parsed_pattern[1], parsed_pattern[2])
    basis_vector = Vector.from_angle(math.radians(local_pattern.angle))
    basis_vector.paint_image_out(jpeg_origin, img_size[0], shift, drawing_object)

    # draws from origin to top of the image
    jpeg_origin = Vector(parsed_pattern[1], parsed_pattern[2])
    reverse_vector = Vector.from_angle(math.radians(local_pattern.angle))
    reverse_vector.paint_image_out(jpeg_origin, img_size[0], -shift, drawing_object)

    # save changes in image
    local_image.save("test.jpeg", "jpeg")

    return None
