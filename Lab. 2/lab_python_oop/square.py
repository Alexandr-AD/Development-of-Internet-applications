from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):

    fig_type = "квадрат"

    @classmethod
    def gettype(cls):
        return cls.fig_type

    def __init__(self, side_param, col):
        self.side = side_param
        super().__init__(self.side, self.side, col)

    def repr(self):
        return'{} {} со стороной {}, площадью {}'.format(
            self.fc.colour,
            self.gettype(),
            self.side,
            self.square()
        )