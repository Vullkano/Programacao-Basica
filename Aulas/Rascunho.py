import numpy as np


def soma_elementos(t):
    soma = 0
    for v in t:
        if v > 0:
            soma += v
    return soma


def similar(a, b):
    if len(a) == len(b):
        if soma_elementos(a) == soma_elementos(b):
            return True
        else:
            return False
    else:
        return False


def soma_linha(x):
    i = 0
    soma = 0
    while i < len(x):
        z = x[i]
        soma += z
        i += 1
    return soma


def diagonal_difference(m):
    i = 0
    diagonal = 0
    total = 0
    while i < len(m):
        diagonal += m[i][i]
        i += 1
    i = 0
    while i < len(m):
        total += soma_linha(m[i])
        i += 1
    return 2 * diagonal - total


m = np.array([[3, 2, 0], [0, 2, 0], [2, 1, 1]])


# Parte 3

class Viatura:
    def __init__(self, matricula, descricao, custo, venda):
        self.__matricula = matricula
        self.descricao = descricao
        self.custo = custo
        self.venda = venda

    @property
    def matricula(self):
        return self.__matricula

    @property
    def lucro(self):
        return self.venda - self.custo

    def descricao(self):
        return self.descricao

    def custo(self):
        return self.custo

    def venda(self):
        return self.venda

    def __str__(self):
        return f'Matricula: {self.__matricula}\n' \
               f'Descricao: {self.descricao}\n' \
               f'Custo: {self.custo}\n' \
               f'Venda: {self.venda}\n' \
               f'Lucro: {self.lucro}\n'


class Loja:
    def __init__(self):
        self.loja = []

    def existe(self, x):
        for i in self.loja:
            if x == i.matricula:
                return True
        return False

    def adicionar(self, matricula, descricao, custo, venda):
        if self.existe(matricula):
            print('Esta matricula é repetida')
            return
        else:
            self.loja.append(Viatura(matricula, descricao, custo, venda))

    def adicionar_2(self, x):
        self.loja.append(x)

    def lucro_total(self):
        z = 0
        for i in self.loja:
            z += i.lucro
        return z

    def lucro_medio(self):
        if len(self.loja) == 0:
            return 0
        else:
            return self.lucro_total() / len(self.loja)

    def filtrar_por_preco(self, minimo, maximo):
        for i in self.loja:
            if minimo < i.lucro < maximo:
                print(i + '\n')

    def viatura_mais_cara(self):
        if len(self.loja) == 0:
            return None
        x = self.loja[0]
        for i in self.loja:
            if i.venda > x.venda:
                x = i
        print(x)

    def yha(self):
        x = self.loja[0]
        print(x)


f = Loja()
a1 = Viatura('Amadora', 'Sei lá', 5, 10)
a2 = Viatura('Ama', 'Sei lá', 9, 78)
a3 = Viatura('Amora', 'Sei lá', 8, 56)
a4 = Viatura('Amada', 'Sei lá', 7, 123)
f.adicionar_2(a1)
f.adicionar_2(a2)
f.adicionar_2(a3)
f.adicionar_2(a4)


def distance(x, y):
    if len(x) != len(y):
        return None
    i = 0
    maior = 0
    while i < len(x):
        distancia = x[i] - y[i]
        if distancia < 0:
            distancia *= -1
        if distancia > maior:
            maior = distancia
        i += 1
    return maior


# ou

def distancia_2(x, y):
    if len(x) != len(y):
        return None
    a1 = x.max() - y.min()
    a2 = y.max() - x.min()
    if a1 > a2:
        return a1
    else:
        return a2


def lower_triangular(m):
    if m.shape[0] != m.shape[1]:
        return None
    coluna = 1
    linha = 0
    while linha < m.shape[0]:
        while coluna < m.shape[1]:
            m[linha][coluna] = 0
            coluna += 1
        linha += 1
        coluna = linha + 1
    return m


n1 = np.array([1, 7, 3])
n2 = np.array([8, 2, 6])
m3 = np.array([[8, 2, 6], [1, 7, 3], [6, 5, 9]])
