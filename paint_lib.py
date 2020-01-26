from PIL import Image, ImageDraw
from main import vector


def draw_by_pattern_JPEG(pattern, img_size, color_background=(255, 255, 255)):
    """main function for drawing JPEG"""
    img_object = Image.new('RGB', img_size, color_background)
    drawing_object = ImageDraw.Draw(img_object)

    for obj in pattern:
        width = img_size[0]
        height = img_size[1]
        vector.x1 = obj[1]
        vector.y1 = obj[2]
        vector.x2 = obj[1]
        vector.y2 = obj[2]

        # line to the right
        drawing_object.line((vector.x1, vector.y1, width * 2, vector.y1), fill=255, width=1)
        # line to the left
        drawing_object.line((vector.x1, vector.y1, -width * 2, vector.y1), fill=0, width=1)

    del drawing_object
    # save changes to object-image
    img_object.save("test.jpeg", "jpeg")

    return None
