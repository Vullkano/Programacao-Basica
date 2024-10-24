# Imports
from Vehicle import *
from Park import *

from Main_MenuT4 import *

# ================ T5: Gestão de um parque ================ #

def menuT5(parqueGerir: Park):
    print("\n")
    menuOptionsT4 = (
        f"{BOLD}{GREEN}1.{RESET} Registar entrada\n"
        f"{BOLD}{BLUE}2.{RESET} Registar saída\n"
        f"{BOLD}{YELLOW}3.{RESET} Listar veículos\n"
        f"{BOLD}{MAGENTA}4.{RESET} Exportar estado\n"
    )

    # Adicionar opções VIP apenas se o parque não for público
    if parqueGerir.listaVIP:
        menuOptionsT4 += (
            f"{BOLD}{CYAN}5.{RESET} Listar permissões\n"
            f"{BOLD}{WHITE}6.{RESET} Permitir acesso\n"
            f"{BOLD}{RED}7.{RESET} Revogar acesso\n"
        )

    # Adicionar a opção de Voltar
    menuOptionsT4 += f"{BOLD}{RED}0.{RESET} Voltar"

    print(menuOptionsT4)

    value = int(input("Insira a opção pretendida"))
    match value:
        case 1:
            VeiculosGuardados = RegistoVeiculos()
            print(f"{BOLD}Selecione o veículo que quer registar a entrada{RESET}\n")
            for i in VeiculosGuardados.values():
                print(i)
            VeiculoEscolhido = input("Matrícula: ")

            # Primeira condição
            for dados in VeiculosGuardados.values():
                if dados['matricula'] == VeiculoEscolhido:
                    VeiculoEscolhido = dados
                    break
                else:
                    raise ValueError('O veículo não existe')

            VeiculoEscolhido = Vehicle(
                matricula=VeiculoEscolhido['matricula'],
                tipo=VeiculoEscolhido['tipo'],
                marca=VeiculoEscolhido['marca'],
                modelo=VeiculoEscolhido['modelo'],
                proprietario=VeiculoEscolhido['proprietario'],
                ano=VeiculoEscolhido['ano']
            )


            # Segunda condição
            for i in lista_parques:
                pass

    print(f"\n{BOLD}A voltar ao menu principal{RESET}\n")