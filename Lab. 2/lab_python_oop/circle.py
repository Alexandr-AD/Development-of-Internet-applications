from lab_python_oop.figure import Figure
from lab_python_oop.fig_colour import fig_colour
import numpy as np
import math

class Circle(Figure):

    fig_type = "круг"

    @classmethod
    def gettype(cls):
        return cls.fig_type

    def __init__(self, r, col):
        """
        Конструктор
        :param radius: радиус
        :param fc: объект класса цвета
        """
        self.radius = r
        self.fc = fig_colour()
        self.fc.set_colour = col

    def square(self):
        """
        Метод для вычисления площади фигуры
        """
        return math.pi * np.power(self.radius, 2) #функция из пакета numpy, установленного через pip
       # return math.pi * (self.radius ** 2)

    def repr(self):
        return '{} {} радиуса {}, площадью {}'.format(
            self.fc.colour,
            self.gettype(),
            self.radius,
            self.square()
        )
