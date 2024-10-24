## ParkGest ##

# Imports
from Vehicle import *
from Park import *
from MenuT5 import *

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

# ================ T4: Gestão de parques ================ #

def menu():

    menuOptionsT4 = (
        f"{BOLD}{GREEN}1.{RESET} Listar parques\n"
        f"{BOLD}{BLUE}2.{RESET} Gerir parque\n"
        f"{BOLD}{YELLOW}3.{RESET} Criar parque\n"
        f"{BOLD}{MAGENTA}4.{RESET} Remover parque\n"
        f"{BOLD}{CYAN}5.{RESET} Estatísticas e informações\n"
        f"{BOLD}{RED}0.{RESET} Sair"
    )

    print(menuOptionsT4)
    value = int(input("Insira a opção pretendida"))
    while value != 0:
        match value:
            case 1:
                j = 1
                if j <= len(lista_parques):
                    for i in lista_parques:
                        print(f"{BOLD}{j}{RESET}. {i}")
                        j += 1
                else:
                    print("Não existem parques no sistema")

            case 2:
                # ================ T5: Gestão de um parque ================ #
                parqueEscolhido = False
                j = 1
                if j <= len(lista_parques):
                    print(f"{BOLD}Escolha o nome parque que pretende gerir:{RESET}\n")
                    for i in lista_parques:
                        print(f"{j}. {BOLD}{i.nome}{RESET}")
                        j += 1

                    nome = input("Insira o nome do parque: ")
                    for i in lista_parques:
                        if i.nome == nome:
                            parqueEscolhido = i
                    if not parqueEscolhido:
                        raise ValueError("Não existe um parque com esse nome.")

                    menuT5(parqueEscolhido)

                else:
                    print("Não existem parques no sistema")

                # ============= Fim de T5: Gestão de um parque ============= #

            case 3:
                print("Porfavor, responda as questões seguintes sobre o parque")

                # Selecionar o nome
                NameStop = [i.nome for i in lista_parques]
                nome = input("Insira o nome do parque: ")
                if nome in NameStop:
                    raise ValueError(f"Já existe um parque com esse nome.")

                # Selecionar a localização
                localizacaoStop = [i.localizacao for i in lista_parques]
                latitude = float(input("Insira a latitude do parque: "))
                if abs(latitude) > 90:
                    raise ValueError(f"Coordenadas inválidas.")

                longitude = float(input("Insira a longitude do parque: "))
                if abs(longitude) > 180:
                    raise ValueError(f"Coordenadas inválidas.")

                localizacaoPark = (latitude, longitude)
                if localizacaoPark in localizacaoStop:
                    raise ValueError(f"Coordenadas inválidas.")

                # Selecionar a capacidade
                try:
                    capacidade = int(input("Insira a capacidade do parque: "))
                except ValueError:
                    print("Capacidade inválida.")
                    break

                # Selecionar a privacidade
                print("O parque é privado ?")
                print(
                    f"{BOLD}{RED}0.{RESET} Não\n"
                    f"{BOLD}{GREEN}1.{RESET} Sim"
                )
                VIP = input("Opção:")
                if VIP != "1" and VIP != "0":
                    raise ValueError("Opção inválida.")
                VIP = bool(VIP)

                lista_parques.append(Park(nome,localizacaoPark, capacidade, VIP))
                print(f"\n{BOLD}{GREEN}Parque Criado Com Sucesso!{RESET}\n")

            case 4:
                j = 1
                if j <= len(lista_parques):
                    for i in lista_parques:
                        print(f"{BOLD}{j}{RESET}. {i}")
                        j += 1

                    print(f"\nSelecione o {BOLD}Nome{RESET} do parque que pretende eliminar.\n")
                    ParkApagar = input("Nome:")
                    for i in range(len(lista_parques)):
                        if ParkApagar == lista_parques[i].nome:
                            lista_parques.pop(i)
                        else:
                            print("Não existe um parque com esse nome.")

                else:
                    print("Não existem parques no sistema")

            case 5:
                # ============== T6: Estatísticas e informações ============== #

                print("vitoria")

                # ============ Fim de T6: Estatísticas e informações ============ #

        print(menuOptionsT4)
        value = int(input("Insira a opção pretendida"))

if __name__ == "__main__":
    lista_parques = [P1, P2, P3, P4, P5, P6]
    menu()