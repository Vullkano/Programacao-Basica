import numpy as np


def naturals(x):
    v = np.zeros(x, int)
    i = 0
    while i < len(v):
        v[i] = i + 1
        i += 1
    return v


def impar(x):
    return x % 2 == 1


def par(x):
    return x % 2 == 0


def sum_odd(x):
    i = 0
    soma = 0
    while i < len(x):
        z = x[i]
        if impar(z):
            soma += z
            i += 1
        else:
            i += 1
    return soma


def soma_linha(x):
    i = 0
    soma = 0
    while i < len(x):
        z = x[i]
        soma += z
        i += 1
    return soma


def mean(x):
    i = 0
    soma = 0
    while i < len(x):
        soma += x[i]
        i += 1
    return soma / len(x)


def exists(numero, x):
    i = 0
    while i < len(x):
        if numero == x[i]:
            return True
        else:
            i += 1
    return False


def count(numero, x):
    i = 0
    soma = 0
    while i < len(x):
        if numero == x[i]:
            soma += 1
            i += 1
        else:
            i += 1
    return soma


def min_of(x):
    i = 1
    minimo = x[0]
    while i < len(x):
        if minimo > x[i]:
            minimo = x[i]
            i += 1
        else:
            i += 1
    return minimo


def first_half(x, y):
    i = len(x) / 2
    z = int(i)
    if par(i):
        return x[:i]
    else:
        if y is True:
            return x[:z + 1]
        if y is False:
            return x[:z]


def second_half(x, y):
    i = len(x) / 2
    z = int(i)
    if par(i):
        return x[i:]
    else:
        if y == True:
            return x[z:]
        if y == False:
            return x[z + 1:]


def merge(x, y):
    z = np.zeros(len(x) + len(y), int)
    z[:x.size] = x
    z[y.size:] = y
    return z


def merge_2(x, y):
    z = np.zeros(len(x) + len(y), int)
    i = 0
    while i < len(x):
        z[i] = x[i]
        i += 1
    i = 0
    while i < len(y):
        z[i + len(x)] = y[i]
        i += 1
    return z


def invert(x):
    v = x[-1::-1]
    return v


def identity(n):
    x = np.zeros((n, n), int)
    y = 0
    for i in range(n):
        x[i][i] = 1
        y += 1
    return x


def multiply_by_scalar(matriz, escalar):
    return matriz * escalar


def sum_matriz(a, b):
    return a + b


def verificar_identity(m):
    x = identity(len(m))
    i = 0
    if not simetric(m):
        return False
    while i < len(m):
        if m[i][i] == x[i][i]:
            i += 1
        else:
            return False
    return True


def simetric(x):
    return x.shape[0] == x.shape[1]


def multiplicacao(x, y):
    if x.shape[0] != y.shape[1]:
        return 'Impossivel de realizar a multiplicação'
    else:
        matriz_nova = x.dot(y)
        print(matriz_nova)


v1 = np.array([2, 3, 2, 8, 5], int)
h = np.array([2, 9, 21, 8, 52], int)
m1 = np.array([[2, 3, 6], [7, 12, 2]])
m2 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m3 = np.array([[3, 2, 0], [0, 2, 0], [2, 1, 1]])
