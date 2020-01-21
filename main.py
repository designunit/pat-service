from PIL import Image, ImageDraw

# static test pattern (*Rhombus (band) 1 [line 26])
_pattern = [(60, 0, 0, 1.5, 0.8660254, 2, -2),
            (120, 1, 0, 0.5, 0.8660254, 2, -2)]


# main function for drawing
def draw_by_pattern(img_obj):
    drawing_object = ImageDraw.Draw(img_obj)
    #                   x1, y1, x2, y2
    drawing_object.line((0, 0, 300, 300), fill=128)
    drawing_object.line((0, 300, 300, 0), fill=128)

    del drawing_object
    return None


# create an object-image
image_object = Image.new('RGB', (300, 300), (255, 255, 255))

# draw lines
draw_by_pattern(image_object)

# save changes to object-image
image_object.save("test.jpeg", "jpeg")
