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

    def escrever_ficheiro(self):
        f = open('Contactos.txt', 'w')
        for c in self.agenda:
            f.write(str(c) + '\n')
        f.close()

    def ler_ficheiro(self):
        f = open('Contactos.txt', 'r')
        linha = f.readline()
        while linha != '':
            linha_clean = linha.strip()
            colunas = linha_clean.split(',')
            c = Contacto(colunas[0], colunas[1], colunas[2])
            self.agenda.append(c)
            linha = f.readline()
        f.close()


a = Agenda()
c1 = Contacto('Johnny Cash', '222222222', 'jc@email.com')
c2 = Contacto('Bueda fixe', '987654321', 'fixolas@gmail.com')
a.add_contacto(c1)
a.add_contacto(c2)


class Fila:

    def __init__(self, max):
        self.fila_max = max
        self.fila = []

    def add(self, BI):
        if len(self.fila) == self.fila_max:
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

    def escrever_ficheiro(self):
        f = open('Fila.txt', 'w')
        for c in self.fila:
            f.write(str(c) + '\n')
        f.close()

    def ler_ficheiro(self):
        f = open('Fila.txt', 'r')
        linha = f.readline()
        while linha != '':
            linha_clean = linha.strip()
            colunas = linha_clean.split(",")
            c = Fila(colunas[0])
            self.fila.append(c)
            linha = f.readline()
        f.close()


f = Fila(12)
f.add(3128739812)
f.add(93285932890)
f.add(35435)
f.add(936690)
