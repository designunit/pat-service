from PIL import Image, ImageDraw
import png


def draw_by_pattern_JPEG(img_size, color_background=(255, 255, 255)):
    """main function for drawing"""
    image_object = Image.new('RGB', img_size, color_background)
    drawing_object = ImageDraw.Draw(image_object)

    # for obj in pattern:
    #     _radians = math_lib.get_radians(obj[0])
    #     print(math_lib.get_coordinates(_radians))

    for i in range(0, img_size[0], 1):
        # x1, y1, x2, y2
        drawing_object.line((i, i, i, i), fill=0, width=1)

    del drawing_object
    # save changes to object-image
    image_object.save("test.jpeg", "jpeg")

    return None


def draw_by_pattern_PNG():
    """main function for drawing"""
    image_object = open("test1.png", "w+")
    writer = png.Writer(256, 1, greyscale=True)
    writer.write(image_object, [range(256)])
    image_object.close()
    # for obj in pattern:
    #     _radians = math_lib.get_radians(obj[0])
    #     print(math_lib.get_coordinates(_radians))

    # for i in range(0, img_size[0], 1):
    #     # x1, y1, x2, y2
    #     drawing_object.line((i, i, i, i), fill=0, width=1)
    #
    # del drawing_object
    # # save changes to object-image
    # image_object.save("test.jpeg", "jpeg")

    return None
