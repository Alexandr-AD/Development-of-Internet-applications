# используется для сортировки
from operator import itemgetter


class Pup:
    """Ученик"""

    def __init__(self, id, fio, age, cls_id):
        self.id = id
        self.fio = fio
        self.cls_id = cls_id
        self.age = age


class Cls:
    """Класс"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class ClsPup:
    """
    'Ученики класса' для реализации
    связи многие-ко-многим
    """

    def __init__(self, cls_id, pup_id):
        self.cls_id = cls_id
        self.pup_id = pup_id


# классы
classes = [
    Cls(1, '11 А'),
    Cls(2, '11 Б'),
    Cls(3, '10 А'),

    Cls(11, '1 А'),
    Cls(22, '1 Б'),
    Cls(33, '1 В'),
]

# ученики
pupils = [
    Pup(1, 'Артамонов', 18, 1),
    Pup(2, 'Петров', 17, 1),
    Pup(3, 'Иваненко', 16, 2),
    Pup(4, 'Иванов', 17, 2),
    Pup(5, 'Иванин', 16, 3),
    Pup(6, "Фёдоров", 15, 3)
]

cls_pups = [
    ClsPup(1, 1),
    ClsPup(1, 2),
    ClsPup(2, 3),
    ClsPup(2, 4),
    ClsPup(3, 5),
    ClsPup(3, 6),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(e.fio, e.age, d.name)
                   for d in classes
                   for e in pupils
                   if e.cls_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, ed.cls_id, ed.pup_id)
                         for d in classes
                         for ed in cls_pups
                         if d.id == ed.cls_id]

    many_to_many = [(e.fio, cls_name)
                    for cls_name, cls_id, pup_id in many_to_many_temp
                    for e in pupils if e.id == pup_id]

    sort = list(filter(lambda x: x[0].startswith('А'), one_to_many))
    print('Задание В1')
    res_11 = sorted(sort, key=itemgetter(1))
    print(res_11)

    print('\nЗадание В2')
    res_12_unsorted = []
    # Перебираем все отделы
    for d in classes:
        # Список учеников класса
        d_pups = list(filter(lambda i: i[2] == d.name, one_to_many))
        # Если класс не пустой
        if len(d_pups) > 0:
            # Возраст учеников класса
            d_age = [age for _, age, _ in d_pups]
            # Минимальный возраст учеников класса
            d_age_min = min(d_age)
            res_12_unsorted.append((d.name, d_age_min))

    # Сортировка по минимальному возрасту
    res_12 = sorted(res_12_unsorted, key=itemgetter(1))
    print(res_12)

    print('\nЗадание В3')
    res_13 = {}
    # Перебираем все
    print(sorted(many_to_many, key=itemgetter(0)))

if __name__ == '__main__':
    main()

