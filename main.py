import paint_lib


# class Args_struct:
#
#     def __init__(self, ):
#         self._angle
#
#     _angle = obj[0]  # first value   = angle
#     x1 = obj[1]  # second value  = starting line point X Coordinate
#     y1 = obj[2]  # third value   = starting line point Y Coordinate
#     horizontal_shift = obj[3]  # fourth value  = horizontal shift along line direction
#     vertical_shift = obj[4]  # fifth value   = next line shift perpendicular to line direction
#     mark_length = obj[5]  # sixth value   = mark length
#     gap_length = obj[6]  # gap length (usually negative)


# create an object-image
if __name__ == '__main__':
    # test variables/ must be inputted from console later on
    white_background = (255, 255, 255)
    pattern = [(45, 0, 0, 0, 1)]
    image_size = (10, 10)

    # draw lines
    paint_lib.draw_by_pattern_JPEG(pattern, image_size, white_background)

    # paint_lib.draw_by_pattern_PNG()
