from PIL import Image, ImageDraw
from Vector import Vector


def draw_by_pattern_JPEG(pattern, img_size, background_color):
    """main function for drawing JPEG"""
    local_image = Image.new('RGB', img_size, background_color)
    drawing_object = ImageDraw.Draw(local_image)

    for obj in pattern:
        width = img_size[0]
        height = img_size[1]

        vector = Vector(4, 4, 8, 8)
        # line to the right
        drawing_object.line((vector.origin_x, vector.origin_y, vector.i_scalar, vector.j_scalar), fill=255, width=1)
        # line to the left
        drawing_object.line((vector.origin_x, vector.origin_y, vector.i_scalar, vector.j_scalar), fill=255, width=1)

    del drawing_object
    # save changes to object-image
    local_image.save("test.jpeg", "jpeg")

    return None
