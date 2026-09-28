"""Mathematical Morphology Engine
100% Python Standard Library.
"""

class MorphologyDilationErosionEngine:
    """Morphological structuring element processor."""
    def __init__(self, struct_element=None):
        if struct_element is None:
            self.se = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        else:
            self.se = struct_element

    def erode(self, image):
        h, w = len(image), len(image[0])
        sh, sw = len(self.se), len(self.se[0])
        pad_h, pad_w = sh // 2, sw // 2
        out = [[0 for _ in range(w)] for _ in range(h)]
        for y in range(h):
            for x in range(w):
                fits = True
                for sy in range(sh):
                    for sx in range(sw):
                        if self.se[sy][sx] == 1:
                            iy = y + sy - pad_h
                            ix = x + sx - pad_w
                            if iy < 0 or iy >= h or ix < 0 or ix >= w or image[iy][ix] == 0:
                                fits = False
                                break
                    if not fits:
                        break
                out[y][x] = 255 if fits else 0
        return out

    def dilate(self, image):
        h, w = len(image), len(image[0])
        sh, sw = len(self.se), len(self.se[0])
        pad_h, pad_w = sh // 2, sw // 2
        out = [[0 for _ in range(w)] for _ in range(h)]
        for y in range(h):
            for x in range(w):
                hits = False
                for sy in range(sh):
                    for sx in range(sw):
                        if self.se[sy][sx] == 1:
                            iy = y + sy - pad_h
                            ix = x + sx - pad_w
                            if 0 <= iy < h and 0 <= ix < w and image[iy][ix] > 0:
                                hits = True
                                break
                    if hits:
                        break
                out[y][x] = 255 if hits else 0
        return out

    def opening(self, image):
        return self.dilate(self.erode(image))

    def closing(self, image):
        return self.erode(self.dilate(image))
