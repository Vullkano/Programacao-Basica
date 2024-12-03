## ParkGest ##

# Imports
from T1_Vehicle import *
from T3_Park import *
from T5_ParkManagement import *
from T6_StatsInfo import *
import sys
import os
from time import sleep

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

# Estilos adicionais
UNDERLINE = "\033[4m"
BG_BLUE = "\033[44m"
BG_GREEN = "\033[42m"
BG_RED = "\033[41m"
BRIGHT_WHITE = "\033[97m"

def clear_screen():
    """Limpa o ecrã do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Imprime o cabeçalho do programa."""
    clear_screen()
    print(f"""
{BG_BLUE}{BRIGHT_WHITE}{'═' * 60}{RESET}
{BG_BLUE}{BRIGHT_WHITE}║{' ' * 24}PARKGEST v1.0{' ' * 24}║{RESET}
{BG_BLUE}{BRIGHT_WHITE}{'═' * 60}{RESET}
""")

def print_footer():
    """Imprime o rodapé do menu."""
    print(f"\n{BOLD}{'═' * 60}{RESET}")
    print(f"{CYAN}Desenvolvido por [Diogo Freitas] © 2024{RESET}")

def print_menu_options():
    """Imprime as opções do menu principal."""
    print(f"\n{BOLD}{UNDERLINE}Menu Principal:{RESET}\n")
    options = [
        (f"{GREEN}1", "Listar parques"),
        (f"{BLUE}2", "Gerir parque"),
        (f"{YELLOW}3", "Criar parque"),
        (f"{MAGENTA}4", "Remover parque"),
        (f"{CYAN}5", "Estatísticas e informações"),
        (f"{RED}0", "Sair")
    ]
    
    for num, desc in options:
        print(f"  {BOLD}{num}{RESET} │ {desc}{RESET}")

def loading_animation(message="A processar"):
    """Mostra uma animação de carregamento."""
    for _ in range(3):
        for char in '⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏':
            print(f'\r{message} {char}', end='')
            sleep(0.1)
    print()

def menu(lista_parques: list[Park] = lista_parques):
    while True:
        print_header()
        print_menu_options()
        print_footer()

        try:
            value = input(f"\n{BOLD}Digite sua opção ➜ {RESET}")
            if not value.isdigit():
                raise ValueError("Por favor, insira um número válido.")
            value = int(value)

            if value == 0:
                clear_screen()
                print(f"\n{GREEN}Obrigado por usar o ParkGest!{RESET}")
                print(f"{BOLD}A encerrar...{RESET}")
                sleep(1)
                break

            clear_screen()
            loading_animation()

            match value:
                case 1:
                    print(f"\n{BG_GREEN}{BRIGHT_WHITE} LISTA DE PARQUES {RESET}\n")
                    if lista_parques:
                        for i, parque in enumerate(lista_parques, 1):
                            print(f"{BOLD}{i}.{RESET} {parque}")
                    else:
                        print(f"{RED}Não existem parques no sistema{RESET}")

                case 2:
                    print(f"\n{BG_BLUE}{BRIGHT_WHITE} GESTÃO DE PARQUE {RESET}\n")
                    if not lista_parques:
                        print(f"{RED}Não existem parques no sistema{RESET}")
                        continue

                    print(f"Escolha o {BOLD}nome{RESET} do parque que pretende gerir:\n")
                    for i, parque in enumerate(lista_parques, 1):
                        print(f"{i}. {BOLD}{parque.nome}{RESET}")

                    nome = input(f"\nNome do parque ➜ {RESET}")
                    parque_escolhido = next((p for p in lista_parques if p.nome == nome), None)
                    
                    if not parque_escolhido:
                        print(f"\n{RED}Erro: Parque não encontrado.{RESET}")
                        sleep(2)
                        continue

                    menuT5(parque_escolhido)

                case 3:
                    print(f"\n{BG_GREEN}{BRIGHT_WHITE} CRIAR PARQUE {RESET}\n")
                    nome = input(f"{BOLD}Nome do parque:{RESET} ")
                    
                    try:
                        lotacao = int(input(f"{BOLD}Lotação:{RESET} "))
                        if lotacao <= 0:
                            raise ValueError("A lotação deve ser maior que zero.")
                    except ValueError as e:
                        print(f"\n{RED}Erro: {str(e)}{RESET}")
                        continue
                    
                    try:
                        lat = float(input(f"{BOLD}Latitude:{RESET} "))
                        lon = float(input(f"{BOLD}Longitude:{RESET} "))
                    except ValueError:
                        print(f"\n{RED}Erro: Coordenadas inválidas.{RESET}")
                        continue

                    privado = input(f"{BOLD}Privado (s/n):{RESET} ").lower() == 's'
                    
                    novo_parque = Park(nome, lotacao, (lat, lon), privado)
                    lista_parques.append(novo_parque)
                    print(f"\n{GREEN}Parque criado com sucesso!{RESET}")

                case 4:
                    print(f"\n{BG_RED}{BRIGHT_WHITE} REMOVER PARQUE {RESET}\n")
                    if not lista_parques:
                        print(f"{RED}Não existem parques no sistema{RESET}")
                        continue

                    print("Parques disponíveis:\n")
                    for i, parque in enumerate(lista_parques, 1):
                        print(f"{BOLD}{i}.{RESET} {parque.nome}")

                    try:
                        nome = input(f"\n{BOLD}Nome do parque a remover:{RESET} ")
                        parque_remover = next((p for p in lista_parques if p.nome == nome), None)
                        
                        if not parque_remover:
                            print(f"\n{RED}Erro: Parque não encontrado.{RESET}")
                            continue

                        lista_parques.remove(parque_remover)
                        print(f"\n{GREEN}Parque removido com sucesso!{RESET}")
                    except Exception as e:
                        print(f"\n{RED}Erro ao remover parque: {str(e)}{RESET}")

                case 5:
                    menuT6()

        except ValueError as e:
            print(f"\n{RED}Erro: {str(e)}{RESET}")
            sleep(2)
        except Exception as e:
            print(f"\n{RED}Erro inesperado: {str(e)}{RESET}")
            sleep(2)

        input(f"\n{BOLD}Pressione ENTER para continuar...{RESET}")

if __name__ == "__main__":
    menu(lista_parques)