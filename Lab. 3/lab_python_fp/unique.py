class Unique:
    """Итератор, оставляющий только уникальные значения."""

    def __init__(self, data, **kwargs):
        self.used_elements = set()
        self.data = data
        self.index = 0
        if 'ignore_case' not in kwargs:
            self.ignore_case = False
        else:
            self.ignore_case = kwargs['ignore_case']

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]
                self.index = self.index + 1
                if self.ignore_case:
                    if current.lower() not in self.used_elements:
                        self.used_elements.add(current.lower())
                        return current
                    else:
                        if current not in self.used_elements:
                            # Добавление в множество производится
                            # с помощью метода add
                            self.used_elements.add(current)
                            return current


lst2 = [1, 3, 2, 3, 2, 1, 4, 3, 3, 3]
data2 = ['a', 'A', 'c', 'C', 'C', 'B', 'b', 'b']
for i in Unique(lst2):
    print(i)
print("_____________")
for d2 in Unique(data2, ignore_case=False):
    print(d2)
print("_____________")
for d3 in Unique(data2, ignore_case=True):
    print(d3)
