from lab_python_oop.figure import Figure
from lab_python_oop.fig_colour import fig_colour

class Rectangle(Figure):

    fig_type = "прямоугольник"

    @classmethod
    def gettype(cls):
        return cls.fig_type

    def __init__(self, wi, he, col):
        """
        Конструктор
        :param wi: ширина
        :param he: высота
        :param fc: объект класса цвета
        """
        self.width = wi
        self.height = he
        self.fc = fig_colour()
        self.fc.set_colour = col

    def square(self):
        """
        Метод для вычисления площади фигуры
        """
        return self.width * self.height

    def repr(self):
        return'{} {} высотой {}, шириной {}, площадью {}'.format(
            self.fc.colour,
            self.gettype(),
            self.height,
            self.width,
            self.square()
        )