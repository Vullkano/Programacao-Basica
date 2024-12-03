# imports
import random
import re
from datetime import datetime

# ============= T1: Classe Veículo ( Vehicle ) ============= #

def validar_matricula(matricula: str) -> bool:
    """Valida o formato da matrícula (XX-XX-XX)."""
    padrao = r'^[A-Z0-9]{2}-[A-Z0-9]{2}-[A-Z0-9]{2}$'
    return bool(re.match(padrao, matricula))

class Vehicle:
    """
    Classe que representa um veículo.
    
    Attributes:
        matricula (str): Matrícula do veículo no formato XX-XX-XX
        tipo (str): Tipo do veículo ('ligeiro', 'pesado' ou 'motociclo')
        marca (str): Marca do veículo
        modelo (str): Modelo do veículo
        proprietario (str): Nome do proprietário
        ano (int): Ano do veículo
    """
    
    TIPOS_VALIDOS = {'ligeiro', 'pesado', 'motociclo'}
    
    def __init__(self, matricula: str, tipo: str, marca: str, modelo: str, proprietario: str, ano: int):
        # Validações melhoradas
        if not validar_matricula(matricula):
            raise ValueError("Formato de matrícula inválido. Use o formato XX-XX-XX")
        if tipo.lower() not in self.TIPOS_VALIDOS:
            raise ValueError(f"Tipo deve ser um dos seguintes: {', '.join(self.TIPOS_VALIDOS)}")
        if ano < 1900 or ano > 2024:  # Podemos ajustar os anos conforme necessário
            raise ValueError("Ano inválido")
            
        self.__matricula = matricula.upper()
        self.__tipo = tipo.lower()
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

    def to_dict(self) -> dict:
        """Converte o veículo para um dicionário."""
        return {
            'matricula': self.matricula,
            'tipo': self.tipo,
            'marca': self.marca,
            'modelo': self.modelo,
            'proprietario': self.proprietario,
            'ano': self.ano
        }

    def idade(self) -> int:
        """Retorna a idade do veículo em anos."""
        return datetime.now().year - self.ano

# Exemplos de veiculos
V1 = Vehicle('AB-23-RF', 'ligeiro', 'BMW', 'e330', 'Nuno', 2020)
V2 = Vehicle('XY-45-UV', 'motociclo', 'Ford', 'Transit', 'Ana', 2019)
V3 = Vehicle('CD-67-WX', 'pesado', 'Mercedes', 'Actros', 'Carlos', 2021)

# =========== T2: Leitura do registo de veículos =========== #
# TODO -> só leitura do ficheiro?; não é preciso adicionar veiculos novos?

def RegistoVeiculos(ficheiro: str = 'VeiculosGuardados.txt') -> dict:
    """
    Lê o registo de veículos de um ficheiro.
    
    Args:
        ficheiro (str): Caminho para o ficheiro de veículos
        
    Returns:
        dict: Dicionário com os veículos lidos
    """
    veiculos = {}
    
    try:
        with open(ficheiro, 'r', encoding='utf-8') as file:
            linhas = file.read().splitlines()
            for idx, linha in enumerate(linhas, 1):
                try:
                    dados = [d.strip() for d in linha.split(',')]
                    if len(dados) != 6:
                        print(f"Aviso: Linha {idx} ignorada - formato incorreto: {linha}")
                        continue
                        
                    veiculos[idx] = {
                        'matricula': dados[0],
                        'tipo': dados[1],
                        'marca': dados[2],
                        'modelo': dados[3],
                        'proprietario': dados[4],
                        'ano': int(dados[5])
                    }
                except ValueError as e:
                    print(f"Erro ao processar linha {idx}: {e}")
                    continue
                    
    except FileNotFoundError:
        print(f"Ficheiro {ficheiro} não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o ficheiro: {e}")
        
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