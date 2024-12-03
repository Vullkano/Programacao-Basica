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

def menuT5(parqueGerir: Park):
    # Função para ler o ficheiro que contem os veiculos
    VeiculosGuardados = RegistoVeiculos()

    while True:
        print(f"\n{BOLD}╔{'═' * 50}╗{RESET}")
        print(f"{BOLD}║{' ' * 15}Gestão do Parque: {parqueGerir.nome}{' ' * 15}║{RESET}")
        print(f"{BOLD}╚{'═' * 50}╝{RESET}")

        menuOptionsT5 = (
            f"\n{BOLD}┌{'─' * 30}┐{RESET}\n"
            f"{BOLD}│{RESET}    {BOLD}{GREEN}1.{RESET} Registar entrada{' ' * 8}{BOLD}│{RESET}\n"
            f"{BOLD}│{RESET}    {BOLD}{BLUE}2.{RESET} Registar saída{' ' * 10}{BOLD}│{RESET}\n"
            f"{BOLD}│{RESET}    {BOLD}{YELLOW}3.{RESET} Listar veículos{' ' * 9}{BOLD}│{RESET}\n"
            f"{BOLD}│{RESET}    {BOLD}{MAGENTA}4.{RESET} Exportar estado{' ' * 9}{BOLD}│{RESET}\n"
        )

        if parqueGerir.privado:
            menuOptionsT5 += (
                f"{BOLD}│{RESET}    {BOLD}{CYAN}5.{RESET} Listar permissões{' ' * 7}{BOLD}│{RESET}\n"
                f"{BOLD}│{RESET}    {BOLD}{WHITE}6.{RESET} Permitir acesso{' ' * 8}{BOLD}│{RESET}\n"
                f"{BOLD}│{RESET}    {BOLD}{RED}7.{RESET} Revogar acesso{' ' * 10}{BOLD}│{RESET}\n"
            )

        menuOptionsT5 += (
            f"{BOLD}│{RESET}    {BOLD}{RED}0.{RESET} Voltar{' ' * 17}{BOLD}│{RESET}\n"
            f"{BOLD}└{'─' * 30}┘{RESET}"
        )

        print(menuOptionsT5)

        try:
            value = int(input(f"\n{BOLD}Insira a opção pretendida:{RESET} "))

            match value:
                case 0:
                    print(f"\n{BOLD}A voltar ao menu principal...{RESET}")
                    return

                case 1:
                    print(f"\n{BOLD}╔{'═' * 40}╗{RESET}")
                    print(f"{BOLD}║{' ' * 8}Registar Entrada de Veículo{' ' * 8}║{RESET}")
                    print(f"{BOLD}╚{'═' * 40}╝{RESET}\n")
                    
                    print(f"{BOLD}Veículos Disponíveis:{RESET}")
                    for idx, veiculo in enumerate(VeiculosGuardados.values()):
                        print(f"{BOLD}{idx}.{RESET} {veiculo['matricula']} - {veiculo['modelo']} ({veiculo['proprietario']})")

                    VeiculoEscolhido = input(f"\n{BOLD}Matrícula:{RESET} ").strip().upper()

                    for dados in VeiculosGuardados.values():
                        if dados['matricula'] == VeiculoEscolhido:
                            VeiculoEscolhido = dados
                            break
                    if type(VeiculoEscolhido) == str:
                        print(f"\n{BOLD}{RED}Erro: O veículo não existe{RESET}")
                        continue

                    VeiculoEscolhido = CreateVehicle(VeiculoEscolhido)

                    for i in lista_parques:
                        if VeiculoEscolhido in i.listaVeiculos:
                            print(f"\n{BOLD}{RED}Erro: O veículo já está num parque{RESET}")
                            continue

                    if parqueGerir.privado and VeiculoEscolhido.matricula not in parqueGerir.listaVIP:
                        print(f"\n{BOLD}{RED}Erro: O veículo não tem permissão para entrar no parque{RESET}")
                        continue

                    parqueGerir.addVeiculo(VeiculoEscolhido)
                    print(f"\n{BOLD}{GREEN}✓ Veículo {VeiculoEscolhido.matricula} registado com sucesso{RESET}")

                case 2:
                    print(f"\n{BOLD}╔{'═' * 40}╗{RESET}")
                    print(f"{BOLD}║{' ' * 9}Registar Saída de Veículo{' ' * 8}║{RESET}")
                    print(f"{BOLD}╚{'═' * 40}╝{RESET}\n")

                    if not parqueGerir.listaVeiculos:
                        print(f"{BOLD}{YELLOW}⚠ Não existem veículos estacionados{RESET}")
                        continue

                    print(f"{BOLD}Veículos Estacionados:{RESET}")
                    for idx, veiculo in enumerate(parqueGerir.listaVeiculos):
                        print(f"{BOLD}{idx}.{RESET} {veiculo}")

                    VeiculoEscolhido = input(f"\n{BOLD}Matrícula:{RESET} ").strip().upper()

                    for veiculosEstacionados in parqueGerir.listaVeiculos:
                        if veiculosEstacionados.matricula == VeiculoEscolhido:
                            VeiculoEscolhido = veiculosEstacionados
                            break
                    if type(VeiculoEscolhido) == str:
                        print(f"\n{BOLD}{RED}Erro: O veículo não existe{RESET}")
                        continue

                    parqueGerir.removeVeiculo(VeiculoEscolhido)
                    print(f"\n{BOLD}{GREEN}✓ Veículo removido com sucesso{RESET}")

                case 3:
                    print(f"\n{BOLD}╔{'═' * 40}╗{RESET}")
                    print(f"{BOLD}║{' ' * 10}Veículos Estacionados{' ' * 10}║{RESET}")
                    print(f"{BOLD}╚{'═' * 40}╝{RESET}\n")
                    
                    if not parqueGerir.listaVeiculos:
                        print(f"{BOLD}{YELLOW}⚠ Não existem veículos estacionados{RESET}")
                    else:
                        parqueGerir.seeAllVeiculos()

                case 4:
                    print(f"\n{BOLD}╔{'═' * 40}╗{RESET}")
                    print(f"{BOLD}║{' ' * 12}Exportar Estado{' ' * 12}║{RESET}")
                    print(f"{BOLD}╚{'═' * 40}╝{RESET}")

                    nomeFicheiro = input(f"\n{BOLD}Nome do ficheiro:{RESET} ").strip()

                    if not nomeFicheiro.endswith('.txt'):
                        nomeFicheiro += '.txt'

                    with open(nomeFicheiro, 'w', encoding='utf-8') as file:
                        file.write(str(parqueGerir) + '\n')
                        for veiculo in parqueGerir.listaVeiculos:
                            file.write(str(veiculo) + '\n')
                    
                    print(f"\n{BOLD}{GREEN}✓ Estado exportado com sucesso para {nomeFicheiro}{RESET}")

                case 5:
                    if parqueGerir.privado:
                        print(f"\n{BOLD}╔{'═' * 40}╗{RESET}")
                        print(f"{BOLD}║{' ' * 13}Lista VIP{' ' * 16}║{RESET}")
                        print(f"{BOLD}╚{'═' * 40}╝{RESET}\n")
                        
                        if not parqueGerir.listaVIP:
                            print(f"{BOLD}{YELLOW}⚠ Não existem veículos VIP{RESET}")
                        else:
                            for idx, matricula in enumerate(parqueGerir.listaVIP):
                                print(f"{BOLD}{idx}.{RESET} {matricula}")

                case 6:
                    if parqueGerir.privado:
                        print(f"\n{BOLD}╔{'═' * 40}╗{RESET}")
                        print(f"{BOLD}║{' ' * 12}Adicionar VIP{' ' * 13}║{RESET}")
                        print(f"{BOLD}╚{'═' * 40}╝{RESET}")

                        matriculaVIP = input(f"\n{BOLD}Matrícula:{RESET} ").strip().upper()
                        parqueGerir.addVIP(matriculaVIP)
                        print(f"\n{BOLD}{GREEN}✓ Acesso VIP concedido{RESET}")

                case 7:
                    if parqueGerir.privado:
                        print(f"\n{BOLD}╔{'═' * 40}╗{RESET}")
                        print(f"{BOLD}║{' ' * 12}Remover VIP{' ' * 14}║{RESET}")
                        print(f"{BOLD}╚{'═' * 40}╝{RESET}")

                        matriculaVIP = input(f"\n{BOLD}Matrícula:{RESET} ").strip().upper()
                        parqueGerir.removeVIP(matriculaVIP)
                        print(f"\n{BOLD}{GREEN}✓ Acesso VIP revogado{RESET}")

                case _:
                    print(f"\n{BOLD}{RED}Erro: Opção inválida{RESET}")

        except ValueError:
            print(f"\n{BOLD}{RED}Erro: Por favor insira um número válido{RESET}")
            continue