from PIL import Image, ImageDraw
import math


# *Hatch 1x45
# first value   = angle
# second value  = starting line point X Coordinate
# third value   = starting line point Y Coordinate
# fourth value  = next line shift along the line direction (relative to X Y coordinates)
# fifth value   = next line shift perp. to line direction (angle +90°)
# sixth value   = mark length
# seventh value = gap length (usually negative)

def get_rotation(angle):
    return angle


# main function for drawing
def draw_by_pattern(img_obj, pattern_list):
    drawing_object = ImageDraw.Draw(img_obj)

    for obj in pattern_list:
        # x1, y1, x2, y2
        print(get_rotation(obj[0]))
        # drawing_object.line((0, 0, 0, 1), fill=0, width=1)
        # drawing_object.line((0, 300, 300, 0), fill=0, width=1)

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
