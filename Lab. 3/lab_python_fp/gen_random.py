from random import randint


def gen_random(n, mi, ma):
    for i in range(n):
        yield randint(mi, ma)


rand = gen_random(5, 3, 10)
for r in rand:
    print(r)
