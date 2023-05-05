def media(x):
    z = 0
    for i in x:
        z += i
    return z / len(x)


def maior(x):
    z = 0
    for i in x:
        if i > z:
            z = i
    return z


def vogais(x):
    freq = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for c in x:
        if c in freq:
            freq[c] += 1
    return freq


x = [1, 2, 3, 4]
y = (1, 4, 8, 12)
frase = "o tempo pergunta ao tempo quanto tempo o tempo tem"


class Contacto:
    def __init__(self, nome, telefone, email=''):
        self.__nome = nome
        self.telefone = telefone
        self.email = email

    @property
    def nome(self):
        return self.__nome

    def __str__(self):
        return f'({self.__nome} --> telefone: {self.telefone}; email: {self.email})'


class Agenda:
    def __init__(self):
        self.agenda = []

    def add_contacto(self, x):
        self.agenda.append(x)

    def listar_agenda(self):
        for i in self.agenda:
            print(i)

    def listar_pessoa(self, x):
        for i in self.agenda:
            if x in i.nome:
                return f'({i.nome} --> telefone: {i.telefone}; email: {i.email})'

    def remover_contacto(self, x):
        for i in self.agenda:
            if x in i.nome:
                self.agenda.remove(i)

    def substituir_telefone(self, nome, telefone):
        for i in self.agenda:
            if nome in i.nome:
                i.telefone = telefone

    def cont(self):
        x = input('Introduza a pesquisa')
        for i in self.agenda:
            if i.nome.find(x, 0) != -1:
                print(i)


def menu():
    print(''
          'Para realizar a opção pretendida, digite o número correspondente\n'
          '1 - Mostrar Todos os Contactos\n'
          '2 - Mostrar Contacto\n'
          '3 - Adicionar Contacto\n'
          '4 - Remover Contacto\n'
          '5 - Alterar Contacto\n'
          '6 - Pesquisar Contacto')
    y = int(input('Introduza aqui a sua Opção: '))
    while y != 0:
        if y == 1:
            a.listar_agenda()

        if y == 2:
            x = input('Insira o nome do contacto que pretende ver')
            a.listar_pessoa(x)

        if y == 3:
            Name = input('Introduza o nome do Contacto: ')
            Phone = input('Introduza o número de telemóvel do Contacto: ')
            Mail = input('Introduza o mail do Contacto: ')
            final = Contacto(Name, Phone, Mail)
            a.add_contacto(final)

        if y == 4:
            x = input('Insira o nome do contacto que pretende eliminar')
            a.remover_contacto(x)

        if y == 5:
            x = input('Insira o nome do contacto que pretende atualizar o número de telefone')
            y = input('Insira o novo número de telefone')
            a.substituir_telefone(x, y)

        if y == 6:
            a.cont()

        if y > 6:
            print('Essa opção não existe ;-; ')

        print('\n'
              'Para realizar a opção pretendida, digite o número correspondente\n'
              '1 - Mostrar Todos os Contactos\n'
              '2 - Mostrar Contacto\n'
              '3 - Adicionar Contacto\n'
              '4 - Remover Contacto\n'
              '5 - Alterar Contacto\n'
              '6 - Pesquisar Contacto')
        y = int(input('Introduza aqui a sua Opção: '))
    return


a = Agenda()
c1 = Contacto('Johnny Cash', '222222222', 'jc@email.com')
c2 = Contacto('Bueda fixe', '987654321', 'fixolas@gmail.com')
a.add_contacto(c1)
a.add_contacto(c2)


class Fila:

    def __init__(self):
        self.fila = []

    def add(self, BI):
        if len(self.fila) == 12:
            return 'Fila cheia'
        self.fila.append(BI)

    def atendimento(self):
        if len(self.fila) == 0:
            return 'Ningém na fila'
        else:
            del self.fila[0]

    def primeiro_fila(self):
        if len(self.fila) == 0:
            return 'Ningém na fila'
        else:
            return self.fila[0]


f = Fila()
f.add(3128739812)
f.add(93285932890)
f.add(35435)
f.add(936690)


class IntSet:

    def __init__(self):
        self.IntSet = []

    def cardinalidade(self):
        return len(self.IntSet)

    def conj_vazio(self):
        return len(self.IntSet) == 0

    def exist_number(self, numero):
        return numero in self.IntSet

    def listar(self):
        for i in self.IntSet:
            print(i)

    def adicionar_numero(self, x):
        if not self.exist_number(x):
            self.IntSet.append(x)

    def eliminar_numero(self, x):
        if self.exist_number(x):
            self.IntSet.remove(x)

    def uniao(self, other):
        x = []
        for i in self.IntSet:
            x.append(i)
        for i in other:
            if i not in x:
                x.append(i)
        self.IntSet = x
        self.listar()

    def intersecao(self, other):
        x = []
        for i in self.IntSet:
            if i in other:
                x.append(i)
        self.IntSet = x
        self.listar()

i = IntSet()
B = [3, 4, 5]
C = [2, 4, 5]
i.adicionar_numero(1)
i.adicionar_numero(2)
i.adicionar_numero(3)

def count_types(x):
    tipos = {int: 0, float: 0, tuple: 0, list: 0, str: 0}
    for i in x:
        if type(i) in tipos:
            tipos[type(i)] += 1
    return tipos

gg = [2, 1.0, 4.2, "Iscte", ["a", "b"], (1,2)]
count_types(gg)