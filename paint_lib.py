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

    default_direction = (img_size[0], 0)
    rotated_direction = math_lib.get_coordinates(img_size[0], 45)

    origin = Vector(0, 0)
    local_vector = Vector(default_direction[0], rotated_direction)
    # basis local_vector
    drawing_object.line((origin.x, origin.y, local_vector.x, local_vector.y), fill = 255, width = 10)
    # opposite direction to the local_vector
    # drawing_object.line((local_vector.origin_x, local_vector.origin_y, -local_vector.i, -local_vector.j), fill = 255, width = 10)

    del drawing_object

    # save changes to object-image
    local_image.save("test.jpeg", "jpeg")

    return None
