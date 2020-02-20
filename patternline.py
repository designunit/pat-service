class PatternLine:
    def __init__(self, angle, x, y, along, perpendicular, length, gap):
        self.angle = angle
        self.origin = {x, y}
        self.line_shift_along = along
        self.line_shift_perp = perpendicular
        self.dash = [length, gap]

