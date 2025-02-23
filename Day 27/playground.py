def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(1, 2, 3))


def calculate(n, **kwargs):
    n+=kwargs['add']
    n*=kwargs['multiply']
    return n

print(calculate(2, add=3, multiply=5))