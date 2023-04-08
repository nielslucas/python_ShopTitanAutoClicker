class RgbModel:

    def __init__(self, r, g, b, margin):
        self.r = r
        self.g = g
        self.b = b
        self.rRange = range(r - margin, r + margin)
        self.gRange = range(g - margin, g + margin)
        self.bRange = range(b - margin, b + margin)