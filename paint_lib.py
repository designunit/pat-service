from PIL import Image, ImageDraw
from Vector import Vector
import math_lib


def draw_by_pattern_JPEG(test_pattern, img_size, background_color):
    """main function for drawing JPEG"""
    local_image = Image.new('RGB', img_size, background_color)
    drawing_object = ImageDraw.Draw(local_image)

    angle = test_pattern[0]
    pattern_origin_x = test_pattern[1]
    pattern_origin_y = test_pattern[2]
    line_shift_along = test_pattern[3]
    # line_shift_perpendicular = test_pattern[4]
    # line_length = test_pattern[5]
    # gap_length = test_pattern[6]

    i_scalar = img_size[0]
    j_scalar = img_size[1]

    vector = Vector(i_scalar/2, j_scalar/2, pattern_origin_x, pattern_origin_y)

    drawing_object.line((vector.origin_x, vector.origin_y, vector.i_scalar, vector.j_scalar), fill = 255, width = 10)
    # line to the opposite side
    # drawing_object.line((vector.origin_x, vector.origin_y, -vector.i_scalar, -vector.j_scalar), fill = 0, width = 10)

    del drawing_object

    # save changes to object-image
    local_image.save("test.jpeg", "jpeg")

    return None
