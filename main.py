from PIL import Image

import paint_lib

# *Hatch 1x45
# first value   = angle
# second value  = starting line point X Coordinate
# third value   = starting line point Y Coordinate
# fourth value  = next line shift along the line direction (relative to X Y coordinates)
# fifth value   = next line shift perp. to line direction (angle +90°)
# sixth value   = mark length
# seventh value = gap length (usually negative)
# _pattern = [(45, 0, 0, 0, 1)]

# create an object-image
if __name__ == '__main__':
    # test variables/ must be inputted from console later on
    _pattern = [(45, 0, 0, 0, 1)]
    _img_size = (20, 20)

    # draw lines
    paint_lib.draw_by_pattern_JPEG(_pattern, _img_size)
    # paint_lib.draw_by_pattern_PNG()
