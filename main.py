from PIL import Image, ImageDraw
import math_lib


# *Hatch 1x45
# first value   = angle
# second value  = starting line point X Coordinate
# third value   = starting line point Y Coordinate
# fourth value  = next line shift along the line direction (relative to X Y coordinates)
# fifth value   = next line shift perp. to line direction (angle +90°)
# sixth value   = mark length
# seventh value = gap length (usually negative)

# _pattern = [(45, 0, 0, 0, 1)]

# main function for drawing
def draw_by_pattern(img_obj, pattern):
    drawing_object = ImageDraw.Draw(img_obj)

    for obj in pattern:
        _radians = math_lib.get_radians(obj[0])

        print(math_lib.get_coordinates(_radians))
        # x1, y1, x2, y2
        drawing_object.line((0, 0, 0, 1), fill=0, width=1)
        drawing_object.line((0, 300, 300, 0), fill=0, width=1)

    del drawing_object
    return None


# create an object-image
size = (20, 20)
white_color = (255, 255, 255)
image_object = Image.new('RGB', size, white_color)

# draw lines
_pattern = [(45, 0, 0, 0, 1)]
draw_by_pattern(image_object, _pattern)

# save changes to object-image
image_object.save("test.jpeg", "jpeg")
