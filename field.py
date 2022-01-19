def field(items, *args):
    assert len(args) > 0
    for i in items:
        if len(args) == 1:  # если передан только один аргумент,то генератор выводит только значение поля
            if i.get(args[0]):  # метод get() возвращает значение для данного ключа
                yield i[args[0]]
        else:
            res = {}
            for a in args:
                res[a] = i.get(a)
            if len(res.items()) != 0:
                yield res
                # print(res)


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]
result = field(goods, 'title', 'color')
for r in result:
    print(r)
