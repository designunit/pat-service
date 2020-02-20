import math_lib

from PIL import Image, ImageDraw
from vector import Vector
from pattern import Pattern


def draw_by_pattern_JPEG(test_pattern, img_size, background_color):
    """main function for drawing JPEG"""
    local_image = Image.new('RGB', img_size, background_color)
    drawing_object = ImageDraw.Draw(local_image)

    local_pattern = Pattern(test_pattern[0], test_pattern[1], test_pattern[2], test_pattern[3],
                            test_pattern[4], test_pattern[5], test_pattern[6])

    x_y = math_lib.rotate_vector_sin_cos(img_size[0], local_pattern.angle)

    null_vector = Vector(0, 0)
    scaled_vector = Vector(x_y[0], x_y[1])
    # basis scaled_vector
    drawing_object.line((null_vector.x, null_vector.y, scaled_vector.x, scaled_vector.y), fill = 255, width = 10)
    # opposite direction to the scaled_vector
    drawing_object.line((null_vector.x, null_vector.y, -scaled_vector.x, -scaled_vector.y), fill = 255, width = 10)

    del drawing_object

    # save changes to object-image
    local_image.save("test.jpeg", "jpeg")

    return None
