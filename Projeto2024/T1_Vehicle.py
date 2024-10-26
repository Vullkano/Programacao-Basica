# imports
import random

# ============= T1: Classe Veículo ( Vehicle ) ============= #

class Vehicle:
    def __init__(self, matricula: str, tipo: str, marca: str, modelo: str, proprietario: str, ano: int):
        assert type(matricula) == str
        assert type(tipo) == str and (tipo == "ligeiro" or tipo == "pesado" or tipo == "motociclo")
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

# Exemplos de veiculos
V1 = Vehicle('AB-23-RF', 'ligeiro', 'BMW', 'e330', 'Nuno', 2020)
V2 = Vehicle('XY-45-UV', 'motociclo', 'Ford', 'Transit', 'Ana', 2019)
V3 = Vehicle('CD-67-WX', 'pesado', 'Mercedes', 'Actros', 'Carlos', 2021)

# =========== T2: Leitura do registo de veículos =========== #
# TODO -> só leitura do ficheiro?; não é preciso adicionar veiculos novos?

def RegistoVeiculos(ficheiro: str = 'VeiculosGuardados.txt') -> dict:
    veiculos = {}

    with open(ficheiro, 'r', encoding='utf-8') as file:
        linhas = file.read().splitlines()
        for idx, linha in enumerate(linhas):
            dados = linha.split(',')
            if len(dados) == 6:
                veiculos[idx + 1] = {
                    'matricula': dados[0],
                    'tipo': dados[1],
                    'marca': dados[2],
                    'modelo': dados[3],
                    'proprietario': dados[4],
                    'ano': int(dados[5])
                }
            else:
                print(f"Linha {idx + 1} no ficheiro não tem o formato correto: {linha}")

    return veiculos

# ================= EXTRA: Função para injetar vários veiculos nos parques ================= #

def criar_veiculos(veiculos_dict: dict) -> list:
    """Converte o dicionário de veículos em objetos Vehicle."""
    veiculos = []
    for dados in veiculos_dict.values():
        veiculo = Vehicle(
            matricula=dados['matricula'],
            tipo=dados['tipo'],
            marca=dados['marca'],
            modelo=dados['modelo'],
            proprietario=dados['proprietario'],
            ano=dados['ano']
        )
        veiculos.append(veiculo)
    return veiculos

def DistribuirVeiculosNosParques(veiculos: list, parques: list):
    for veiculo in veiculos:
        parque_aleatorio = random.choice(parques)

        if veiculo.tipo.lower() == 'pesado':
            print(f"Veículo {veiculo.matricula} é pesado e não pode ser adicionado a nenhum parque.")
            continue

        if parque_aleatorio.privado:
            if veiculo.matricula not in parque_aleatorio.listaVIP:
                parque_aleatorio.addVIP(veiculo.matricula)

        try:
            parque_aleatorio.addVeiculo(veiculo)
            print(f"Veículo {veiculo.matricula} adicionado ao {parque_aleatorio.nome}")
        except ValueError as e:
            print(f"Não foi possível adicionar {veiculo.matricula} ao {parque_aleatorio.nome}: {e}")