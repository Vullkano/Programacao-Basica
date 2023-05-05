def dobro(x):
    return 2 * x


def subtracao(x, y):
    return x - y


def percentagem(n, total):
    return f'{n * 100 / total}%'


def media(x, y):
    return (int(x) + int(y)) / 2


def arredondar(x):
    return int(float(x) + 0.5)


def negativo(x):
    return x < 0


def impar(x):
    return x % 2 == 1


def par(x):
    return x % 2 == 0


def divisao_inteira(x, y):
    return x % y == 0


def unidades(x):
    return 0 <= x <= 9


def is_included(x, min, max):
    return min <= x <= max


def is_excluded(x, min, max):
    return not min <= x <= max


def XOR(x, y):
    return x ^ y


def is_vowel(x):
    return x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'
