## ParkGest ##

# ============= T1: Classe Veículo ( Vehicle ) ============= #

class Vehicle:
    def __init__(self, matricula: str, tipo: str, marca: str, modelo: str, proprietario: str, ano: int):
        assert type(matricula) == str
        assert type(tipo) == str and (tipo == "Ligeiro" or tipo == "Pesado" or tipo == "Motociclo")
        assert type(marca) == str
        assert type(modelo) == str
        assert type(proprietario) == str
        assert type(ano) == int

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


V1 = Vehicle('AB-23-RF', 'Ligeiro', 'BMW', 'e330', 'Nuno', 2020)
V2 = Vehicle('XY-45-UV', 'Motociclo', 'Ford', 'Transit', 'Ana', 2019)
V3 = Vehicle('CD-67-WX', 'Pesado', 'Mercedes', 'Actros', 'Carlos', 2021)


# =========== T2: Leitura do registo de veículos =========== #
# TODO -> só leitura do ficheiro?; não é preciso adicionar veiculos novos?

def armazernarVeiculo(ficheiro: str = 'VeiculosGuardados.txt') -> dict:
    x = {}
    y = 0
    with open(ficheiro, 'r', encoding='utf-8') as file:
        leitura = file.read()
        linhas = leitura.splitlines()
        for linha in linhas:
            x[f'V{y}'] = {
                'matricula': linha.split(',')[0],
                'tipo': linha.split(',')[1],
                'marca': linha.split(',')[2],
                'modelo': linha.split(',')[3],
                'proprietario': linha.split(',')[4],
                'ano': linha.split(',')[5]
            }
            y += 1
    return x


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

lista_parques = [P1, P2, P3, P4, P5, P6]

# ================ T4: Gestão de parques ================ #

def menu():
    # Cores ANSI
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"

    menuOptions = (
        f"{BOLD}{GREEN}1.{RESET} Listar parques\n"
        f"{BOLD}{BLUE}2.{RESET} Gerir parque\n"
        f"{BOLD}{YELLOW}3.{RESET} Criar parque\n"
        f"{BOLD}{MAGENTA}4.{RESET} Remover parque\n"
        f"{BOLD}{CYAN}5.{RESET} Estatísticas e informações\n"
        f"{BOLD}{RED}0.{RESET} Sair"
    )

    print(menuOptions)
    value = int(input("Insira a opção pretendida"))
    while value != 0:
        match value:
            case 1:
                j = 1
                if j <= len(lista_parques):
                    for i in lista_parques:
                        print(f"{BOLD}{j}{RESET}. {i}")
                        j += 1
                    z = int(input("Escolha o parque que pretende pelo respetivo número"))
                    while z < 0 or z > len(lista_parques):
                        z = int(input("Valor incorreto! selecione o respetivo número do parque"))
                    parque_selecionado = lista_parques[z - 1]
                    print(f"Parque selecionado: {parque_selecionado.nome}\n")
                else:
                    print("Não existem parques no sistema")

            case 2:
                print("vitoria")


        print(menuOptions)
        value = int(input("Insira a opção pretendida"))
