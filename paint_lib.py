import math

from PIL import Image, ImageDraw
from vector import Vector
from patternline import PatternLine


def draw_by_pattern_JPEG(test_pattern, img_size, background_color):
    """main function for drawing JPEG"""
    local_image = Image.new('RGB', img_size, background_color)
    drawing_object = ImageDraw.Draw(local_image)

    origin = Vector(test_pattern[1], test_pattern[2])

    local_pattern = PatternLine(test_pattern[0], origin, test_pattern[3], test_pattern[4],
                                test_pattern[5], test_pattern[6])

    basis_vector = Vector.from_angle(math.radians(local_pattern.angle))
    basis_vector.multiply(img_size[0] * 2)

    shift = local_pattern.line_shift_perp
    basis_vector.paint_pattern(origin, img_size[0], shift, drawing_object)

    origin = Vector(test_pattern[1], test_pattern[2])

    reverse_vector = Vector.from_angle(math.radians(local_pattern.angle))
    reverse_vector.multiply(img_size[0] * 2)

    reverse_vector.paint_pattern(origin, img_size[0], -shift, drawing_object)

    # save changes to object-image
    local_image.save("test.jpeg", "jpeg")

    return None
