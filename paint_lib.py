from PIL import ImageDraw


def draw_by_pattern(img_obj, pattern, img_size):
    """main function for drawing"""
    drawing_object = ImageDraw.Draw(img_obj)

    # for obj in pattern:
    #     _radians = math_lib.get_radians(obj[0])
    #     print(math_lib.get_coordinates(_radians))

    for i in range(0, img_size[0], 1):
        # x1, y1, x2, y2
        drawing_object.line((0, i, i, 0), fill=0, width=1)
        print(i)

    del drawing_object
    return None
