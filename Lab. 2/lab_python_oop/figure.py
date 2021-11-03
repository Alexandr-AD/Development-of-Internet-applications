from abc import ABC, abstractmethod

class Figure(ABC):
    """
    Абстрактный класс геометрических фигур
    """

    @abstractmethod
    def square(self):
        """
        Виртуальный метод вычисления площади фигуры
        """
        pass