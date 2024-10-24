from Vehicle import *

# ============== T3: Classe Parque ( Park ) ============== #
# TODO -> O parque é suposto possuir uma lista base para guardar os veiculos, não era melhor referir?

class Park:
    def __init__(self, nome: str, localizacao: tuple[float, float], lotacao: int, privado: bool):
        assert type(nome) == str
        assert type(localizacao) == tuple and len(localizacao) == 2 and -90 <= localizacao[0] <= 90 and -180 <= \
               localizacao[1] <= 180
        assert type(lotacao) == int
        assert type(privado) == bool

        self.__nome = nome
        self.__localizacao = localizacao
        self.__lotacao = lotacao
        self.__privado = privado

        self.__listaVeiculos = []

        # Somente cria a lista VIP se o parque for privado
        if self.__privado:
            self.__listaVIP = []

    @property
    def nome(self):
        return self.__nome

    @property
    def localizacao(self):
        return self.__localizacao

    @property
    def lotacao(self):
        return self.__lotacao

    @property
    def privado(self):
        return self.__privado

    # Lista VIP acessível somente se o parque for privado
    @property
    def listaVIP(self):
        if self.__privado:
            return self.__listaVIP
        return None

    def addVeiculo(self, veiculo: 'Vehicle'):
        assert isinstance(veiculo, Vehicle)
        if self.__lotacao > len(self.__listaVeiculos):
            if self.__privado:
                if veiculo in self.__listaVIP and veiculo not in self.__listaVeiculos:
                    self.__listaVeiculos.append(veiculo)
                else:
                    print(f"Veículo {veiculo.matricula} não está autorizado a entrar no parque VIP.")
            else:
                if veiculo not in self.__listaVeiculos:
                    self.__listaVeiculos.append(veiculo)
                else:
                    print(f"O veículo {veiculo.matricula} já se encontra no parque de estacionamento.")
        else:
            print(f"O parque está cheio, o veículo {veiculo.matricula} não pode entrar.")

    def removeVeiculo(self, veiculo: 'Vehicle'):
        assert isinstance(veiculo, Vehicle)
        if veiculo in self.__listaVeiculos:
            self.__listaVeiculos.remove(veiculo)
        else:
            print(f"O veículo {veiculo.matricula} não se encontra no parque.")

    def inPark(self, veiculo: 'Vehicle'):
        assert isinstance(veiculo, Vehicle)
        return veiculo in self.__listaVeiculos

    def seeAllVeiculos(self):
        if len(self.__listaVeiculos) == 0:
            print("O parque está vazio")
        else:
            for i in self.__listaVeiculos:
                print(i)

    def lugaresOcupados(self):
        return len(self.__listaVeiculos)

    def lugaresDisponiveis(self):
        return self.__lotacao - self.lugaresOcupados()

    def __str__(self):
        return f"{self.nome} ({self.localizacao[0]}, {self.localizacao[1]}) {self.lugaresOcupados()}/{self.lotacao}"


P1 = Park('Parque do ISCTE',(38.7478, -9.1534), 380, False)
P2 = Park('Parque da Cidade', (38.7499, -9.1550), 50000, True)
P3 = Park('Parque Eduardo VII', (38.7275, -9.1519), 260000, True)
P4 = Park('Parque das Nações', (38.7660, -9.0983), 200000, True)
P5 = Park('Jardim Botânico', (38.7131, -9.1517), 30000, False)
P6 = Park('Parque Nacional da Peneda-Gerês', (41.7191, -8.1575), 730000, True)