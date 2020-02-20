import paint_lib


if __name__ == '__main__':
    # test variables/ must be inputted from console later on
    white_background = (255, 255, 255)
    black_background = (0, 0, 0)
    test_pattern = (45, 0, 0, 0, 1)
    image_size = (500, 500)

    # draw lines
    # paint_lib.draw_by_pattern_JPEG(test_pattern, image_size, white_background)
    paint_lib.draw_by_pattern_JPEG(test_pattern, image_size, black_background)

    # paint_lib.draw_by_pattern_PNG()
