def maximum(x, y):
    if x > y:
        return x
    else:
        return y


def is_multiple(x, y):
    p = x
    while p > 1:
        t = p / y
        p = t
    return p == 1


def absolute(x):
    if x >= 0:
        return x
    if x < 0:
        return x * -1


def divide(x, y):
    return int(x / y)


def power_of_two(x):
    p = 0
    a = 1
    while p != x:
        p += 1
        a *= 2
    return a


def sum_of_naturals_up_to(x):
    b = 0
    p = 0
    while p != x:
        p += 1
        b += p
    return b


def sum_of_even_numbers_between(min, max):
    b = min
    soma = 0
    while b < max + 1:
        if b % 2 == 0:
            soma += b
            b += 1
        else:
            b += 1
    return soma


def first_digit(x):
    a = str(x)
    divisor = len(a) - 1
    y = x / (10 ** divisor)
    return int(y)


def fibonacci(a):
    w = 1
    x = 0
    y = 1
    z = 1
    while w != a:
        z = x + y
        x = y
        y = z
        w += 1
    return z


def gcd(x, y):
    b = 2
    while x % b != y % b:
        b += 1
        if b > y:
            return 'Não existe'
    return b
