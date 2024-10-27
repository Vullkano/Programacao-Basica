# Imports
from T1_Vehicle import *
from T3_Park import *

from T4_MainMenu import *

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

# Funções complementares
def CreateVehicle(VeiculoEscolhido):
    VeiculoCriado = Vehicle(
        matricula=VeiculoEscolhido['matricula'],
        tipo=VeiculoEscolhido['tipo'],
        marca=VeiculoEscolhido['marca'],
        modelo=VeiculoEscolhido['modelo'],
        proprietario=VeiculoEscolhido['proprietario'],
        ano=VeiculoEscolhido['ano']
    )
    return VeiculoCriado

# ================ T5: Gestão de um parque ================ #

def menuT5(parqueGerir: Park):

    print(f"\n # === {BOLD}{parqueGerir.nome}{RESET} === # ")

    # Função para ler o ficheiro que contem os veiculos
    VeiculosGuardados = RegistoVeiculos()

    menuOptionsT5 = (
        f"{BOLD}{GREEN}1.{RESET} Registar entrada\n"
        f"{BOLD}{BLUE}2.{RESET} Registar saída\n"
        f"{BOLD}{YELLOW}3.{RESET} Listar veículos\n"
        f"{BOLD}{MAGENTA}4.{RESET} Exportar estado\n"
    )

    # Adicionar opções VIP apenas se o parque não for público
    if parqueGerir.privado:
        menuOptionsT5 += (
            f"{BOLD}{CYAN}5.{RESET} Listar permissões\n"
            f"{BOLD}{WHITE}6.{RESET} Permitir acesso\n"
            f"{BOLD}{RED}7.{RESET} Revogar acesso\n"
        )

    # Adicionar a opção de Voltar
    menuOptionsT5 += f"{BOLD}{RED}0.{RESET} Voltar"

    print(menuOptionsT5)

    value = int(input("Insira a opção pretendida: "))
    while value != 0:
        match value:

            case 1: # TODO não era melhor mostrar os carros do ficheiro?
                print(f"{BOLD}Selecione a matrícula do veículo que quer registar a entrada{RESET}\n")
                j = 0
                for i in VeiculosGuardados.values():
                    print(f"{BOLD}{j}{RESET}. {i['matricula']}, {i['tipo']}, {i['modelo']},{i['proprietario']}, {i['ano']}")
                    j += 1

                VeiculoEscolhido = str(input("Matrícula: "))

                # Primeira condição
                for dados in VeiculosGuardados.values():
                    if dados['matricula'] == VeiculoEscolhido:
                        VeiculoEscolhido = dados
                        break
                if type(VeiculoEscolhido) == str:
                    raise ValueError('O veículo não existe')

                VeiculoEscolhido = CreateVehicle(VeiculoEscolhido)

                # Segunda condição
                for i in lista_parques:
                    if VeiculoEscolhido in i.listaVeiculos:
                        raise ValueError("O veículo já está num parque")

                # Segunda condição
                if parqueGerir.privado:
                    if VeiculoEscolhido.matricula not in parqueGerir.listaVIP:
                        raise ValueError("O veículo não tem permissão para entrar no parque.")

                print(f"Foi adicionado o veiculo correspondente à matrícula {VeiculoEscolhido.matricula}\n")
                parqueGerir.addVeiculo(VeiculoEscolhido)


            case 2: # TODO não era melhor mostrar os carros que estão no parque estacionados
                print(f"{BOLD}Selecione a matrícula do veículo que quer registar a saida{RESET}\n")
                j = 0
                for i in parqueGerir.listaVeiculos:
                    print(f"{BOLD}{j}{RESET}. {i}")
                    j += 1
                VeiculoEscolhido = input("Matrícula: ")

                # Primeira condição
                for veiculosEstacionados in parqueGerir.listaVeiculos:
                    if veiculosEstacionados.matricula == VeiculoEscolhido:
                        VeiculoEscolhido = veiculosEstacionados
                        break
                if type(VeiculoEscolhido) == str:
                    raise ValueError('O veículo não existe')

                parqueGerir.removeVeiculo(VeiculoEscolhido)

            case 3:
                print("\n # === Veículos estacionados === #")
                parqueGerir.seeAllVeiculos()
                print("\n")

            case 4:
                print(f"\n{BOLD}Insira o nome do ficheiro{RESET}")
                nomeFicheiro = input("Nome do ficheiro: ")

                if not nomeFicheiro.endswith('.txt'):
                    nomeFicheiro += '.txt'

                with open(nomeFicheiro, 'w', encoding='utf-8') as file:
                    # Escrever as caracteristicas do parque
                    file.write(str(parqueGerir) + '\n')

                    # escrever as caracteristicas dos carros
                    for veiculo in parqueGerir.listaVeiculos:
                        file.write(str(veiculo) + '\n')

        if parqueGerir.privado:
            match value:
                case 5:
                    j = 0
                    for i in parqueGerir.listaVIP:
                        print(f"{BOLD}{j}{RESET}. {i}")
                        j += 1

                case 6:
                    print(f"\n{BOLD}Insira a matricula do veiculo que quer permitir o acesso{RESET}")

                    matriculaVIP = input("Matricula: ")
                    parqueGerir.addVIP(matriculaVIP)

                case 7:
                    print(f"\n{BOLD}Insira a matricula do veiculo que quer retirar o acesso{RESET}")

                    matriculaVIP = input("Matricula: ")
                    parqueGerir.removeVIP(matriculaVIP)

        print(menuOptionsT5)
        value = int(input("Insira a opção pretendida"))

    print(f"\n{BOLD}A voltar ao menu principal{RESET}\n")