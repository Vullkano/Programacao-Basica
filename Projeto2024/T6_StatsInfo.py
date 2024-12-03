# Imports
from T3_Park import *
from T5_ParkManagement import *
import matplotlib.pyplot as plt
import seaborn as sns
from T4_MainMenu import *

# Cores ANSI e configuração inicial
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Configuração do estilo dos gráficos
plt.style.use('default')

def filtro_raio(x: int) -> int:
    if x < 100: return 2
    if x < 1000: return 5
    return 10

def filtro_cor(x: float) -> str:
    if x < 0.75: return '#2ecc71'     # Verde
    if x < 1: return '#f1c40f'        # Amarelo
    return '#e74c3c'                  # Vermelho

def menuT6():
    while True:
        print(f"\n{BOLD}╔{'═' * 50}╗{RESET}")
        print(f"{BOLD}║{' ' * 15}Estatísticas e Informações{' ' * 14}║{RESET}")
        print(f"{BOLD}╚{'═' * 50}╝{RESET}")

        menuOptionsT6 = (
            f"\n{BOLD}┌{'─' * 40}┐{RESET}\n"
            f"{BOLD}│{RESET}  {BOLD}{GREEN}1.{RESET} Número total de lugares livres{' ' * 7}{BOLD}│{RESET}\n"
            f"{BOLD}│{RESET}  {BOLD}{BLUE}2.{RESET} Taxa de ocupação média{' ' * 13}{BOLD}│{RESET}\n"
            f"{BOLD}│{RESET}  {BOLD}{YELLOW}3.{RESET} Percentagem de parques privados{' ' * 6}{BOLD}│{RESET}\n"
            f"{BOLD}│{RESET}  {BOLD}{MAGENTA}4.{RESET} Histograma por tipo de veículo{' ' * 6}{BOLD}│{RESET}\n"
            f"{BOLD}│{RESET}  {BOLD}{CYAN}5.{RESET} Visualizar mapa de parques{' ' * 9}{BOLD}│{RESET}\n"
            f"{BOLD}│{RESET}  {BOLD}{RED}0.{RESET} Voltar{' ' * 27}{BOLD}│{RESET}\n"
            f"{BOLD}└{'─' * 40}┘{RESET}"
        )

        print(menuOptionsT6)

        try:
            value = int(input(f"\n{BOLD}Insira a opção pretendida:{RESET} "))

            match value:
                case 0:
                    print(f"\n{BOLD}A voltar ao menu principal...{RESET}")
                    return

                case 1:
                    print(f"\n{BOLD}╔{'═' * 40}╗{RESET}")
                    print(f"{BOLD}║{' ' * 10}Lugares Disponíveis{' ' * 11}║{RESET}")
                    print(f"{BOLD}╚{'═' * 40}╝{RESET}\n")

                    SomaLugaresLivres = sum(p.lugaresDisponiveis() for p in lista_parques)
                    print(f"{BOLD}Total de lugares livres:{RESET} {GREEN}{SomaLugaresLivres}{RESET}")

                case 2:
                    print(f"\n{BOLD}╔{'═' * 40}╗{RESET}")
                    print(f"{BOLD}║{' ' * 10}Taxa de Ocupação{' ' * 12}║{RESET}")
                    print(f"{BOLD}╚{'═' * 40}╝{RESET}\n")

                    for p in lista_parques:
                        taxa = round(p.lugaresOcupados() / p.lotacao * 100, 2)
                        cor = GREEN if taxa < 75 else YELLOW if taxa < 90 else RED
                        print(f"{BOLD}{p.nome}:{RESET} {cor}{taxa}%{RESET}")

                    total_ocupacao = sum(p.lugaresOcupados() for p in lista_parques)
                    total_lotacao = sum(p.lotacao for p in lista_parques)
                    taxa_media = round((total_ocupacao/total_lotacao)*100, 2)
                    
                    print(f"\n{BOLD}Taxa média global:{RESET} {GREEN if taxa_media < 75 else YELLOW if taxa_media < 90 else RED}{taxa_media}%{RESET}")

                case 3:
                    print(f"\n{BOLD}╔{'═' * 40}╗{RESET}")
                    print(f"{BOLD}║{' ' * 10}Parques Privados{' ' * 12}║{RESET}")
                    print(f"{BOLD}╚{'═' * 40}╝{RESET}\n")

                    privados = sum(1 for p in lista_parques if p.privado)
                    percentagem = round((privados/len(lista_parques))*100, 2)
                    print(f"{BOLD}Percentagem de parques privados:{RESET} {BLUE}{percentagem}%{RESET}")

                case 4:
                    # Contagem de veículos
                    contagem = {'Ligeiros': 0, 'Motociclos': 0}
                    for p in lista_parques:
                        for v in p.listaVeiculos:
                            if v.tipo == 'ligeiro':
                                contagem['Ligeiros'] += 1
                            elif v.tipo == 'motociclo':
                                contagem['Motociclos'] += 1

                    # Configuração do gráfico
                    plt.figure(figsize=(10, 6))
                    cores = ['#3498db', '#e67e22']
                    
                    # Criar barplot
                    ax = sns.barplot(x=list(contagem.keys()), y=list(contagem.values()), palette=cores)
                    
                    # Personalização
                    plt.title('Distribuição de Veículos por Tipo', fontsize=16, pad=20, fontweight='bold')
                    plt.xlabel('Tipo de Veículo', fontsize=12, labelpad=10)
                    plt.ylabel('Quantidade', fontsize=12, labelpad=10)
                    
                    # Adicionar valores nas barras
                    for i, v in enumerate(contagem.values()):
                        ax.text(i, v, str(v), ha='center', va='bottom', fontsize=12, fontweight='bold')
                    
                    # Estilo
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)
                    plt.grid(axis='y', linestyle='--', alpha=0.7)
                    
                    plt.tight_layout()
                    plt.show(block=False)

                case 5:
                    # Criar figura com fundo estilizado
                    fig, ax = plt.subplots(figsize=(12, 8), facecolor='#f0f0f0')
                    ax.set_facecolor('#f8f9fa')
                    
                    # Configurar limites e aspecto
                    ax.set_xlim((-90, 90))
                    ax.set_ylim((-180, 180))
                    ax.set_box_aspect(1)
                    
                    # Títulos e labels
                    plt.title('Mapa de Distribuição dos Parques', 
                            fontsize=18, pad=20, fontweight='bold')
                    plt.xlabel('Latitude', fontsize=14, labelpad=10)
                    plt.ylabel('Longitude', fontsize=14, labelpad=10)
                    
                    # Grade estilizada
                    ax.grid(True, linestyle='--', alpha=0.4, color='gray')
                    
                    # Criar círculos com efeito de sombra
                    for p in lista_parques:
                        # Círculo de sombra
                        shadow = plt.Circle(p.localizacao, 
                                         filtro_raio(p.lotacao), 
                                         color='gray', 
                                         alpha=0.3, 
                                         zorder=1)
                        ax.add_patch(shadow)
                        
                        # Círculo principal
                        circle = plt.Circle(p.localizacao, 
                                         filtro_raio(p.lotacao),
                                         color=filtro_cor(p.lugaresOcupados()/p.lotacao),
                                         alpha=0.6,
                                         zorder=2)
                        ax.add_patch(circle)
                        
                        # Adicionar rótulo
                        ax.annotate(p.nome, 
                                  p.localizacao, 
                                  fontsize=8,
                                  ha='center',
                                  va='center',
                                  weight='bold')
                    
                    # Legenda
                    legend_elements = [
                        plt.Line2D([0], [0], marker='o', color='w', 
                                 markerfacecolor='#2ecc71', label='< 75% Ocupação',
                                 markersize=10),
                        plt.Line2D([0], [0], marker='o', color='w',
                                 markerfacecolor='#f1c40f', label='75-100% Ocupação',
                                 markersize=10),
                        plt.Line2D([0], [0], marker='o', color='w',
                                 markerfacecolor='#e74c3c', label='100% Ocupação',
                                 markersize=10)
                    ]
                    ax.legend(handles=legend_elements, loc='upper right',
                            bbox_to_anchor=(1.15, 1))
                    
                    plt.tight_layout()
                    plt.show(block=False)

                case _:
                    print(f"\n{BOLD}{RED}Erro: Opção inválida{RESET}")

        except ValueError:
            print(f"\n{BOLD}{RED}Erro: Por favor insira um número válido{RESET}")
            continue


