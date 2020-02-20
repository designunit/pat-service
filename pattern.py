class Pattern:
    def __init__(self, angle = 0, x = 0, y = 0, along = 0, perpendicular = 0, length = 0, gap = 0):
        self.angle = angle
        self.x = x
        self.y = y
        self.line_shift_along = along
        self.line_shift_perp = perpendicular
        self.dash = [length]
        self.dash = [gap]
