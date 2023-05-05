def number_of_divisors(x):
    p = 1
    divisores = 0
    while p != x + 1:
        if x % p == 0:
            divisores += 1
            p += 1
        else:
            p += 1
    return divisores


def sum_of_divisors(x):
    p = 1
    divisores = 0
    while p != x:
        if x % p == 0:
            divisores += p
            p += 1
        else:
            p += 1
    return divisores


def is_prime(x):
    return number_of_divisors(x) == 2


def sum_of_primes_smaller_than(x):
    y = 1
    soma = 0
    while y != x:
        if is_prime(y):
            soma += y
        y += 1
    return soma


def number_of_primes_up_to(x):
    list = []
    y = 1
    while y != x + 1:
        if is_prime(y):
            list.append(y)
        y += 1
    return list


def fibonacci(x):
    if x <= 1:
        return x
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


def minimum(x, y):
    if x > y:
        return y
    if x < y:
        return x


def maximum(x, y):
    if x > y:
        return x
    if x < y:
        return y


def gcd(x, y):
    div = minimum(x, y)
    while div != 0:
        if x % div == y % div:
            return div
        else:
            div -= 1


def value_between(x, y):
    z = int(input('Insira um valor inteiro que esteja entre o intervalo'))
    while z < x or z > y:
        print('Esse valor está fora do intervalo')
        z = int(input('Insira um valor inteiro que esteja entre o intervalo'))


def print_ascending_between(x, y):
    for i in range(x, y + 1):
        print(i)


def print_units_in_roman(x):
    if x == 0:
        print('')
    if x == 1:
        print('I')
    if x == 2:
        print('II')
    if x == 3:
        print('III')
    if x == 4:
        print('IV')
    if x == 5:
        print('V')
    if x == 6:
        print('VI')
    if x == 7:
        print('VII')
    if x == 8:
        print('VIII')
    if x == 9:
        print('IX')


def print_tens_in_roman(x):
    if x == 1:
        print('X', end='')
    if x == 2:
        print('XX', end='')
    if x == 3:
        print('XXX', end='')
    if x == 4:
        print('XL', end='')
    if x == 5:
        print('L', end='')
    if x == 6:
        print('LX', end='')
    if x == 7:
        print('LXX', end='')
    if x == 8:
        print('LXXX', end='')
    if x == 9:
        print('XC', end='')


def print_in_roman(x):
    if x < 10:
        print_units_in_roman(x)
    if x >= 10:
        dezenas = int(x / 10)
        unidades = int(10 * (x / 10 - dezenas) + 0.5)
        print_tens_in_roman(dezenas)
        print_units_in_roman(unidades)


def print_decrescente_incluido(x, y):
    max = maximum(x, y)
    min = minimum(x, y)
    for i in reversed(range(min, max + 1)):
        print(i)


def print_decrescente_excluido(x, y):
    max = maximum(x, y)
    min = minimum(x, y)
    for i in reversed(range(min + 1, max)):
        print(i)


def print_ascending_between_in_h(x, y, h):
    max = maximum(x, y)
    min = minimum(x, y)
    while min < max - 1:
        print(min)
        min += h


def crescente_na_escrita():
    x = int(input('Insira um valor'))
    while x != 0:
        p = x
        x = int(input('Insira um valor'))
        if x == 0:
            return True
        if p > x:
            y = False
            while x != 0:
                x = int(input('Insira um valor'))
            return y
    return


def soma_impares():
    x = int(input('Insira um valor'))
    soma = 0
    while x != 0:
        p = x
        x = int(input('Insira um valor'))
        if p % 2 == 1:
            soma += 1
    return soma


def perfect_number(x):
    soma = 0
    y = 1
    while y != x:
        if x % y == 0:
            soma += y
            y += 1
        else:
            y += 1
    return soma == x


def number_of_perfect_numbers_up_to(x):
    i = 1
    soma = 0
    while i != x + 1:
        if perfect_number(i):
            soma += 1
            i += 1
        else:
            i += 1
    return soma


def exists_prime_between(x, y):
    i = x
    while i != y + 1:
        if is_prime(i):
            return True
        else:
            i += 1
    return False


def larger_difference_between_primes(x):
    a = 0
    b = 0
    c = x - 1
    while c != 0:
        if is_prime(c):
            if a == 0:
                a = c
                c -= 1
            elif b == 0:
                b = c
                c -= 1
            else:
                c -= 1
        else:
            c -= 1
    return a - b


def maior_numero():
    resultado = 0
    p = 0
    x = int(input('Insira um valor'))
    while x != 0:
        maior = x
        if p > maior:
            resultado = p
        if p < maior:
            resultado = maior
        if maior == p:
            resultado = maior
        p = maior
        x = int(input('Insira um valor'))
        if x == 0:
            return resultado
    return resultado
