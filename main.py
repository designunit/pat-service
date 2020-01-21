from PIL import Image, ImageDraw, ImageFont

# static test pattern
_pattern = [(60, 0, 0, 1.5, 0.8660254, 2, -2),
            (120, 1, 0, 0.5, 0.8660254, 2, -2)]


def draw_by_pattern():
    draw.line()
    return None


# create an object-image
base_image = Image.new('RGB', (300, 300), (255, 255, 255))

draw = ImageDraw.Draw(base_image)

print(base_image.size)

draw.line((0, 0) + base_image.size, fill=128)
draw.line((0, base_image.size[0], base_image.size[1], 0), fill=128)
del draw

# save changes to object-image
base_image.save("test.jpeg", "jpeg")
