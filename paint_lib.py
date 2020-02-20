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

    scaled_vector = Vector.from_angle(math.radians(local_pattern.angle))
    scaled_vector.multiply(img_size[0] * 2)

    # basis scaled_vector
    drawing_object.line((origin.x, origin.y, scaled_vector.x, scaled_vector.y), fill=255, width=10)
    # opposite direction to the scaled_vector
    # drawing_object.line((origin.x, origin.y, -scaled_vector.x, -scaled_vector.y), fill=255, width=10)

    # save changes to object-image
    local_image.save("test.jpeg", "jpeg")

    return None
