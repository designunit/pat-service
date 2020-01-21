from PIL import Image, ImageDraw

# static test pattern (*Rhombus (band) 1 [line 26])
# first value   = angle
# second value  = starting line point X Coordinate
# third value   = starting line point Y Coordinate
# fourth value  = next line shift along the line direction (relative to X Y coordinates)
# fifth value   = next line shift perp. to line direction (angle +90°)
# sixth value   = mark length
# seventh value = gap length (usually negative)
_pattern = [(60, 0, 0, 1.5, 0.8660254, 2, -2),
            (120, 1, 0, 0.5, 0.8660254, 2, -2)]


# main function for drawing
def draw_by_pattern(img_obj):
    drawing_object = ImageDraw.Draw(img_obj)
    #                   x1, y1, x2, y2
    drawing_object.line((0, 0, 300, 300), fill=128, width=1)
    drawing_object.line((0, 300, 300, 0), fill=128, width=1)

    del drawing_object
    return None


# create an object-image
image_object = Image.new('RGB', (300, 300), (255, 255, 255))

# draw lines
draw_by_pattern(image_object)

# save changes to object-image
image_object.save("test.jpeg", "jpeg")
