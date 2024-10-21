## ParkGest ##

# ============= T1: Classe Veículo ( Vehicle ) ============= #

class Vehicle:
    def __init__(self, matricula: str, tipo: str, marca: str, modelo: str, proprietario: str, ano: int):
        self.__matricula = matricula
        self.__tipo = tipo
        self.__marca = marca
        self.__modelo = modelo
        self.__proprietario = proprietario
        self.__ano = ano

    @property
    def matricula(self):
        return self.__matricula

    @property
    def tipo(self):
        return self.__tipo

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def proprietario(self):
        return self.__proprietario

    @property
    def ano(self):
        return self.__ano

    def __str__(self):
        return f"{self.matricula}, {self.tipo}, {self.marca}, {self.modelo}, {self.proprietario}, {self.ano}"

    def __eq__(self, other):
        return isinstance(other, Vehicle) and other.matricula == self.matricula

V1 = Vehicle('1', '1', '1', '1', '1', 2020)

# =========== T2: Leitura do registo de veículos =========== #

def limpar_concluidas_para_iscte(self):
    f = open('historico.csv', 'a')
    mammamia = []
    for i in self.__lista_voltar_para_ISCTE_viagem:
        if not i.ativa:
            f.write(str(i) + '\n')
            mammamia.append(i)
    for i in mammamia:
        self.__lista_voltar_para_ISCTE_viagem.remove(i)
    f.close()