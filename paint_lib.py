from PIL import Image, ImageDraw
import png


def draw_by_pattern_JPEG(pattern, img_size, color_background=(255, 255, 255)):
    """main function for drawing JPEG"""
    img_object = Image.new('RGB', img_size, color_background)
    drawing_object = ImageDraw.Draw(img_object)

    for obj in pattern:

        for i in obj[1::1]:
            for j in obj:
                drawing_object.line((i, i, i, i), fill=0, width=1)

    del drawing_object
    # save changes to object-image
    img_object.save("test.jpeg", "jpeg")

    return None

# def draw_by_pattern_PNG():
#     """main function for drawing PNG"""
#     image_object = open("test1.png", "wb")
#     writer = png.Writer(256, 256)
#     writer.write(image_object)
#     image_object.close()
#     for obj in pattern:
#         _radians = math_lib.get_radians(obj[0])
#         print(math_lib.get_coordinates(_radians))
#
#     for i in range(0, img_size[0], 1):
#         # x1, y1, x2, y2
#         drawing_object.line((i, i, i, i), fill=0, width=1)
#
#     del drawing_object
#     # save changes to object-image
#     image_object.save("test.jpeg", "jpeg")
#
#     return None
