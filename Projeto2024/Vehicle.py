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
                    'ano': dados[5]
                }
            else:
                print(f"Linha {idx + 1} no ficheiro não tem o formato correto: {linha}")

    return veiculos