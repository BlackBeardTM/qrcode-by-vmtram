try:
    from PIL import Image, ImageDraw
except ImportError:
    import Image
    import ImageDraw

import qrcode.image.base

class CustomImage(qrcode.image.base.BaseImage):
    """
    PIL image builder, default format is PNG
    """
    kind = "PNG"

    def new_image(self, **kwargs):
        back_color = kwargs.get("back_color", "white")
        fill_color = kwargs.get("fill_color", "black")
        self.body = kwargs.get("body", "square")
        self.version = kwargs.get("version", 3)
        self.eye = kwargs.get("eye", "eye0")
        self.eye_ball = kwargs.get("eye_ball", "ball0")

        if fill_color.lower() != "black" or back_color.lower() != "white":
            if back_color.lower() == "transparent":
                mode = "RGBA"
                back_color = None
            else:
                mode = "RGB"
        else:
            mode = "1"
            # L mode (1 mode) color = (r*299 + g*587 + b*114)//1000
            if fill_color.lower() == "black": fill_color = 0
            if back_color.lower() == "white": back_color = 255
        img = Image.new(mode, (self.pixel_size, self.pixel_size), back_color)
        self.fill_color = fill_color
        self._idr = ImageDraw.Draw(img)
        return img
    def drawrect(self, row, col):
        #print row, col
        
        # Eye ball
        if (row == 3 and col == 3) or (row == 3 and col == (17 + self.version * 4 - 4)) or (row == (17 + self.version * 4 - 4) and col == 3):
            if self.eye_ball == 'ball0':
                x = (col + self.border) * self.box_size - self.box_size
                y = (row + self.border) * self.box_size - self.box_size
                self._idr.rectangle([(x, y), (x + self.box_size * 3, y + self.box_size * 3)],
                fill= self.fill_color)
            elif self.eye_ball == 'ball1':
                x = (col + self.border) * self.box_size - self.box_size
                y = (row + self.border) * self.box_size - self.box_size
                self._idr.ellipse([(x, y), (x + self.box_size * 3, y + self.box_size * 3)],
                fill= self.fill_color)

        #Arrow Eye TODO
        elif (row,col) in [(2, 2),(3, 2),(4, 2),
                           (2, 3), (2, 4), (4, 4),
                           (3, 4),(4, 3),
                           ((17 + self.version * 4) - 2, 2), ((17 + self.version * 4) - 3, 2),
                           ((17 + self.version * 4) - 4, 2),
                           ((17 + self.version * 4) - 2, 3), ((17 + self.version * 4) - 2, 4),
                           ((17 + self.version * 4) - 4, 4),
                           ((17 + self.version * 4) - 3, 4), ((17 + self.version * 4) - 4, 3),
                           ((17 + self.version * 4) - 5, 2), ((17 + self.version * 4) - 5, 3),
                           ((17 + self.version * 4) - 5, 4), ((17 + self.version * 4) - 3, 3),
                           (2, (17 + self.version * 4) - 2), (3, (17 + self.version * 4) - 2),
                           (4, (17 + self.version * 4) - 2),
                           (2, (17 + self.version * 4) - 3), (2, (17 + self.version * 4) - 4),
                           (4, (17 + self.version * 4) - 4),
                           (3, (17 + self.version * 4) - 2), (4, (17 + self.version * 4) - 3),
                           (2, (17 + self.version * 4) - 5), (3, (17 + self.version * 4) - 5),
                           (4, (17 + self.version * 4) - 5), (3, (17 + self.version * 4) - 3),
                           ]:
            pass
        # Eye
        elif (row < 7 and col < 7) or (row < 7 and col > (17 + self.version * 4 - 8)) or (row > (17 + self.version * 4 - 8) and col < 7):
            #print row, col
            if self.eye == "eye0":
                x = (col + self.border) * self.box_size
                y = (row + self.border) * self.box_size
                self._idr.rectangle([(x, y), (x + self.box_size, y + self.box_size)], fill= self.fill_color)
            elif self.eye == "eye1":
                x = (col + self.border) * self.box_size
                y = (row + self.border) * self.box_size
                self._idr.ellipse([(x, y), (x + self.box_size, y + self.box_size)],fill= self.fill_color)
        else:
            # Body
            if self.body == 'square':
                x = (col + self.border) * self.box_size
                y = (row + self.border) * self.box_size
                self._idr.rectangle([(x, y), (x + self.box_size, y + self.box_size)], fill= self.fill_color)
            elif self.body == 'point':
                x = (col + self.border) * self.box_size
                y = (row + self.border) * self.box_size
                self._idr.ellipse([(x, y), (x + self.box_size, y + self.box_size)],fill= self.fill_color)
    def save(self, stream, format=None, **kwargs):
        if format is None:
            format = kwargs.get("kind", self.kind)
        if "kind" in kwargs:
            del kwargs["kind"]
        self._img.save(stream, format=format, **kwargs)
    
    def __getattr__(self, name):
        return getattr(self._img, name)
    