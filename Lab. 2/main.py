from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square
from lab_python_oop.circle import Circle


def main():
    r = Rectangle(2, 4, "Синий")
    s = Square(8, "Синий")
    c = Circle(2, "Синий")
    print(r.repr())
    print(s.repr())
    print(c.repr())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
