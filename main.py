from PIL import Image, ImageDraw
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
    _pattern = [(45, 0, 0, 0, 1)]
    _white_background = (255, 255, 255)

    img_size = (20, 20)  # this must be inputted within console
    image_object = Image.new('RGB', img_size, _white_background)

    # draw lines
    paint_lib.draw_by_pattern(image_object, _pattern, img_size)

    # save changes to object-image
    image_object.save("test.jpeg", "jpeg")

