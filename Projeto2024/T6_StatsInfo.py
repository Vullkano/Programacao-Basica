# Imports

from T3_Park import *
from T5_ParkManagement import *
from T4_MainMenu import *

import matplotlib.pyplot as plt
# Cores ANSI
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Funções de apoio

def filtro_raio(x:int) -> int:
    if x < 100:
        return 2
    if x < 1000:
        return 5
    else:
        return 10

def filtro_cor(x:float) -> str:
    if x < 0.75:
        return 'g'
    if x < 1:
        return 'y'
    else:
        return 'r'

# ============== T6: Estatísticas e informações ============== #

def menuT6():

    print("\n")

    menuOptionsT5 = (
        f"{BOLD}{GREEN}1.{RESET} Número total de lugares livres\n"
        f"{BOLD}{BLUE}2.{RESET} Taxa de ocupação média\n"
        f"{BOLD}{YELLOW}3.{RESET} Percentagem de parques privados\n"
        f"{BOLD}{MAGENTA}4.{RESET} Histograma por tipo de veículo\n"
        f"{BOLD}{CYAN}5.{RESET} Visualizar mapa de parques\n"
        f"{BOLD}{RED}0.{RESET} Voltar"
    )

    print(menuOptionsT5)

    value = int(input("Insira a opção pretendida: "))
    while value != 0:
        match value:
            case 1:
                SomaLugaresLivres = 0
                for i in lista_parques:
                    SomaLugaresLivres += i.lugaresDisponiveis()
                print(f"\n Existem, no total -> {BOLD}{SomaLugaresLivres}{RESET} lugares livres\n")
            case 2: # TODO é a tx. ocupacao media de todos, oude cada um individualmente?
                print(f"\n # === {BOLD}Tx. ocupação média{RESET} === # ")
                AllOcupados = 0
                AllLotacao = 0
                for i in lista_parques:
                    print(f"{BOLD}{i.nome}{RESET}: {i.lugaresOcupados() / i.lotacao}")
                    AllOcupados += i.lugaresOcupados()
                    AllLotacao += i.lotacao
                print(f"\n A taxa de ocupação média geral é -> {BOLD}{AllOcupados/AllLotacao}%{RESET}\n")
            case 3:
                privado = 0
                for i in lista_parques:
                    if i.privado:
                        privado += 1
                print(f"\n Percentagem de parques privados -> {BOLD}{privado/len(lista_parques)}%{RESET}\n")

            case 4: # TODO não devias ser um barplot?

                # Contagem de veículos
                ligeiros = 0
                motociclos = 0
                for i in lista_parques:
                    for j in i.listaVeiculos:
                        if j.tipo == 'ligeiro':
                            ligeiros += 1
                        elif j.tipo == 'motociclo':
                            motociclos += 1

                # Dados para o gráfico
                barplot = {
                    'Ligeiros': ligeiros,
                    'Motociclos': motociclos,
                }

                # Configuração do gráfico
                plt.figure(figsize=(8, 5))  # Tamanho da figura
                plt.bar(barplot.keys(), barplot.values(), color=['#1f77b4', '#ff7f0e'],
                        alpha=0.8)  # Cores personalizadas

                # Adicionando título e rótulos
                plt.title('Contagem de Veículos por Tipo', fontsize=16, fontweight='bold')
                plt.xlabel('Tipo de Veículo', fontsize=14)
                plt.ylabel('Número de Veículos', fontsize=14)

                # Adicionando grade
                plt.grid(axis='y', linestyle='--', alpha=0.7)

                # Adicionando rótulos nos valores das barras
                for index, value in enumerate(barplot.values()):
                    plt.text(index, value, str(value), ha='center', va='bottom', fontsize=12)

                # Mostrar o gráfico
                plt.tight_layout()  # Ajustar o layout
                plt.show(block=False)

            case 5:

                # Criar uma figura e um eixo
                fig, ax = plt.subplots(figsize=(10, 8))  # Tamanho da figura
                ax.set_xlim((-90, 90))  # Limites do eixo x
                ax.set_ylim((-180, 180))  # Limites do eixo y
                ax.set_box_aspect(1)  # Aspecto do gráfico

                # Adicionar título e rótulos
                ax.set_title('Distribuição dos Parques', fontsize=18, fontweight='bold')
                ax.set_xlabel('Latitude', fontsize=14)
                ax.set_ylabel('Longitude', fontsize=14)

                # Adicionar grade
                ax.grid(True, linestyle='--', alpha=0.7)

                # Criar e adicionar círculos para cada parque
                circles = []
                for i in lista_parques:
                    circles.append(
                        {
                            'position': i.localizacao,
                            'radius': filtro_raio(i.lotacao),
                            'color': filtro_cor(i.lugaresOcupados() / i.lotacao)
                        }
                    )

                # Adicionar os círculos ao gráfico
                for c in circles:
                    circle = plt.Circle(c['position'], c['radius'], color=c['color'], alpha=0.6,
                                        edgecolor='black')  # Adicionado edgecolor
                    ax.add_patch(circle)

                # Ajustar layout para evitar sobreposição
                plt.tight_layout()

                # Mostrar o gráfico
                plt.show(block=False)

        print(menuOptionsT5)
        value = int(input("Insira a opção pretendida: "))
    print(f"\n{BOLD}A voltar ao menu principal{RESET}\n")


