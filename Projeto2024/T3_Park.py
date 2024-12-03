from T1_Vehicle import *
import random

# ============== T3: Classe Parque ( Park ) ============== #
# TODO -> O parque é suposto possuir uma lista base para guardar os veiculos, não era melhor referir?

class Park:
    """
    Classe que representa um parque de estacionamento.
    
    Attributes:
        nome (str): Nome do parque
        localizacao (tuple): Coordenadas (latitude, longitude)
        lotacao (int): Número máximo de lugares
        privado (bool): Se é um parque privado ou público
    """
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

        self.__listaVeiculos: list[Vehicle] = [] # TODO esta lista é suposto ter os objeto Vehicle?

        # Somente cria a lista VIP se o parque for privado
        # A lista VIP apenas possui as matriculas
        if self.__privado:
            self.__listaVIP: list[str] = [] # TODO esta lista é suposto ter só as matriculas?

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

    @property
    def listaVeiculos(self):
        return self.__listaVeiculos

    # Lista VIP acessível somente se o parque for privado
    @property
    def listaVIP(self):
        if self.__privado:
            return self.__listaVIP
        return None

    def addVIP(self, n: str):
        if self.__privado:
            self.listaVIP.append(n)
        return None

    def removeVIP(self, n: str):
        if self.__privado:
            self.listaVIP.remove(n)
        return None

    def addVeiculo(self, veiculo: 'Vehicle'):
        """
        Adiciona um veículo ao parque se houver espaço e respeitar as regras.
        
        Raises:
            ValueError: Se o parque estiver cheio, veículo for pesado,
                      não tiver permissão VIP (em parques privados) ou já estiver estacionado
        """
        if not isinstance(veiculo, Vehicle):
            raise TypeError("O objeto deve ser do tipo Vehicle")
            
        if veiculo.tipo == 'Pesado':
            raise ValueError("Não são permitidos veículos pesados neste parque")
            
        if len(self.__listaVeiculos) >= self.__lotacao:
            raise ValueError(f"O parque {self.nome} está cheio")
            
        if veiculo in self.__listaVeiculos:
            raise ValueError(f"O veículo {veiculo.matricula} já está estacionado neste parque")
            
        if self.__privado and veiculo.matricula not in self.__listaVIP:
            raise ValueError(f"O veículo {veiculo.matricula} não tem permissão VIP para este parque")
            
        self.__listaVeiculos.append(veiculo)
        return True

    def removeVeiculo(self, veiculo: 'Vehicle'):
        assert isinstance(veiculo, Vehicle)
        if veiculo in self.__listaVeiculos:
            self.__listaVeiculos.remove(veiculo)
            print(f"O veículo {veiculo.matricula} foi removido do parque.")
        else:
            raise ValueError(f"O veículo {veiculo.matricula} não está no parque.")

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

# Criar os parques
P1 = Park('Parque do ISCTE',(38.7478, -9.1534), 190, False)
P2 = Park('Parque Central', (random.uniform(-90, 90), random.uniform(-180, 180)), 75, False)
P3 = Park('Parque do Rio', (random.uniform(-90, 90), random.uniform(-180, 180)), 100, False)
P4 = Park('Parque do Estádio', (random.uniform(-90, 90), random.uniform(-180, 180)), 125, True)
P5 = Park('Parque do Museu', (random.uniform(-90, 90), random.uniform(-180, 180)), 150, True)
P6 = Park('Parque do Bairro', (random.uniform(-90, 90), random.uniform(-180, 180)), 50, False)
P7 = Park('Parque da Colina', (random.uniform(-90, 90), random.uniform(-180, 180)), 60, False)
P8 = Park('Parque da Avenida', (random.uniform(-90, 90), random.uniform(-180, 180)), 40, False)
P9 = Park('Parque Privado do Centro', (random.uniform(-90, 90), random.uniform(-180, 180)), 25, True)
P10 = Park('Parque do Jardim', (random.uniform(-90, 90), random.uniform(-180, 180)), 100, False)

# Lista dos parques que vão estar no menu
lista_parques = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10] # TODO é para criar uma lista que contem todos os parques?

# ========= Adicionar carros aos parques para teste ========= #

veiculos_dict = RegistoVeiculos('VeiculosGuardados.txt')
veiculos = criar_veiculos(veiculos_dict)
DistribuirVeiculosNosParques(veiculos, lista_parques)
