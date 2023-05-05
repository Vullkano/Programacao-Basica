from datetime import time, datetime, timedelta
from time import sleep

import matplotlib.pyplot as plt
import numpy

# - - - - - - - - - - - - - - - Import - - - - - - - - - - - - - - -

print('\n------------------------------------------------------')
print('Bem vindo! Para abrir o menu principal digite: menu(g)')
print('------------------------------------------------------')


# - - - - - - - T1: Classes de objetos Utilizador e Viatura - - - - - - -

class Utilizador:
    def __init__(self, numero, nome, morada='', email='', telemovel=''):
        self.__numero = numero
        self.__nome = nome
        self.__morada = morada
        self.__email = email
        self.__telemovel = telemovel

    @property
    def numero_estudante(self):
        # **Campo Obrigatório**
        return self.__numero

    @property
    def nome(self):
        # **Campo Obrigatório**
        return self.__nome

    @property
    def morada(self):
        return self.__morada

    @property
    def email(self):
        return self.__email

    @property
    def telemovel(self):
        return self.__telemovel

    def mudar_morada(self):
        x = input('Insira o novo Concelho')
        y = input('Insira a nova Freguesia')
        z = x + ',' + y
        self.__morada = z

    def mudar_email(self):
        x = input('Insira o novo email')
        self.__email = x

    def mudar_telemovel(self):
        x = input('Insira o novo número de telemovel')
        self.__telemovel = x

    def __str__(self):
        return f'{self.__numero},{self.__nome},{self.__morada},{self.__email},{self.__telemovel}'


class Viatura:
    def __init__(self, matricula, num_condutor, descricao, num_lugares, viagens=0):
        self.__matricula = matricula
        self.__num_condutor = num_condutor
        self.__descricao = descricao
        self.__num_lugares = num_lugares
        self.__viagens = viagens

    @property
    def matricula(self):
        return self.__matricula

    @property
    def num_condutor(self):
        return self.__num_condutor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def num_lugares(self):
        return self.__num_lugares

    @property
    def viagens(self):
        return self.__viagens

    def add_new_trip(self):
        self.__viagens = self.__viagens + 1

    def alterar_descricao(self):
        x = input('Insira a nova marca')
        y = input('Insira o novo modelo')
        z = input('Insira a nova cor')
        a = 'Marca: ' + x + ', ' + 'Modelo: ' + y + ',' + 'Cor: ' + z
        self.__descricao = a

    def __str__(self):
        return f'{self.__matricula},{self.__num_condutor},{self.__descricao},{self.__num_lugares},{self.__viagens}'


# - - - - - - - - - - - - T2: Classe de objetos Viagem - - - - - - - - - - - -

class Viagem:
    def __init__(self, num_condutor, id_viagem, matricula, data_e_hora, morada, max_boleias):
        self.__num_condutor = num_condutor
        self.__id_viagem = id_viagem
        self.__matricula = matricula
        self.__date_time = get_datetime(data_e_hora).isoformat()
        self.__morada = morada  # title
        self.__max_boleias = max_boleias
        self.__list_passageiros = []

    @property
    def num_condutor(self):
        return self.__num_condutor

    @property
    def id_viagem(self):
        return self.__id_viagem

    @property
    def matricula(self):
        return self.__matricula

    @property
    def date_time(self):
        return datetime.fromisoformat(self.__date_time)

    @property
    def morada(self):
        return self.__morada

    @property
    def max_boleias(self):
        return self.__max_boleias

    @property
    def list_passageiros(self):
        return self.__list_passageiros

    @property
    def ativa(self):
        datatime = self.__date_time
        go_datetime = datetime.fromisoformat(datatime)
        print(go_datetime)
        return go_datetime > datetime.now()

    def boleias_disponiveis(self):
        max_boleias = int(self.max_boleias)
        list_passageiros = int(len(self.list_passageiros))
        boleias_disponiveis = max_boleias - list_passageiros
        if max_boleias - list_passageiros == 0:
            print('Os lugares estão todos cheios')
            return
        if max_boleias - list_passageiros > 0:
            print(f'Tens este número de boleias disponiveis: {boleias_disponiveis}')
            return

    def aceita_passageiros(self):
        max_boleias = int(self.max_boleias)
        list_passageiros = int(len(self.list_passageiros))
        boleias_disponiveis = max_boleias - list_passageiros
        if max_boleias - list_passageiros == 0:
            print('Não há mais espaço para passageiros')
        else:
            print(f'Ainda é possivel aceitar {boleias_disponiveis} passageiros')

    def adicionar_passageiros(self, passageiro):
        max_boleias = int(self.max_boleias)
        list_passageiros = int(len(self.list_passageiros))
        if list_passageiros < max_boleias:
            self.__list_passageiros.append(passageiro)
            self.__max_boleias -= 1
            return self.list_passageiros
        else:
            print('Viatura cheia')
            return

    def __str__(self):
        return f'{self.__id_viagem},{self.__matricula},{self.__date_time},{self.__morada},{self.__max_boleias},{self.__list_passageiros}'


# - - - - - - - - - - - - T3: Classe de objetos Gestor - - - - - - - - - - - -

class Gestor:
    def __init__(self):
        self.__lista_utilizador = []
        self.__lista_viatura = []
        self.__lista_sair_do_ISCTE_viagem = []
        self.__lista_voltar_para_ISCTE_viagem = []

    @property
    def list_utilizador(self):
        return self.__lista_utilizador

    @property
    def list_viatura(self):
        return self.__lista_viatura

    @property
    def list_sair_do_ISCTE_viagem(self):
        return self.__lista_sair_do_ISCTE_viagem

    @property
    def list_voltar_para_ISCTE_viagem(self):
        return self.__lista_voltar_para_ISCTE_viagem

    def exists_user(self, numero):
        for i in self.__lista_utilizador:
            if str(numero) in i.numero_estudante:
                return True
        return False

    # - - - - - - - Estas funções foram criadas com o objetivo de testar o código mais facilmente - - - - - - -

    def add_user(self, utilizador):
        self.__lista_utilizador.append(utilizador)

    def add_viatura(self, x):
        self.__lista_viatura.append(x)

    def bruh(self, x):
        self.__lista_voltar_para_ISCTE_viagem.append(x)

    def bruh_sai(self, x):
        self.__lista_sair_do_ISCTE_viagem.append(x)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def add_new_user(self):  # numero, nome, morada='', email='', telemovel=''
        print('--- Lista de Utilizadores ---\n')
        for j in self.__lista_utilizador:
            print(j)
        print('\nPara adicionar um utilizador é necessário adicionar-lhe um número !')
        print('- CAMPO OBRIGATÓRIO')
        numero = input()
        if numero.isnumeric():
            if not g.exists_user(numero):
                print('\n- Campo Obrigatório!')
                nome = input('Insira o nome do estudante: ')
                while len(nome) < 3 and nome.isalpha():
                    print('Nome inserido incorretamente!')
                    nome = input('Insira o nome do estudante: ')
                print('\n- Campo Opcional!')
                print('Insira a morada do utilizador:')
                concelho = input('\t- Insira o Concelho')
                freguesia = input('\t- Insira a Freguesia')
                if len(concelho) == len(freguesia) == 0:
                    morada = ''
                else:
                    morada = concelho + ',' + freguesia
                print('\n- Campo Opcional!')
                print('Insira a parte inicial do email institucional do utilizador, sem a parte do "@iscte-iul.pt":')
                email = input('Insira o email do utilizador')
                if len(email) != 0:
                    email = email + '@iscte-iul.pt'
                else:
                    email = ''
                print('\n- Campo opcional!')
                print('Insira o contacto telefónico do utilizador:')
                telemovel = input('Insira aqui o número de telemóvel')
                if len(telemovel) != 0:
                    while not telemovel.isnumeric():
                        print('Número inserido de forma errada')
                        telemovel = input('Insira aqui o número de telemóvel')
                else:
                    telemovel = ''
                u = Utilizador(numero, nome, morada, email, telemovel)
                self.__lista_utilizador.append(u)
                print('\n- - - Utilizador criado com sucesso - - -\n')

    def list_users(self):
        for i in self.__lista_utilizador:
            print(i)
        return

    def exists_viatura(self, matricula):
        for i in self.__lista_viatura:
            if str(matricula) in i.matricula:
                print('Esta Viatura existe')
                return True
        return False

    def add_viatura_correto(self):  # matricula, num_condutor, descricao, num_lugares, viagens=0)
        matricula_viatura = input('Insira a matricula da viatura')
        if len(matricula_viatura) == 8 and matricula_viatura[2] == matricula_viatura[5] == '-':
            for i in self.__lista_viatura:
                if matricula_viatura in i.matricula:
                    print('---ERRO--- Matricula Repetida')
                    return
                if matricula_viatura not in i.matricula:
                    print('\n---Lista de Utilizadores---\n')
                    for g in self.__lista_utilizador:
                        print(g)
                    y = input('\nAdicione um número de estudante para ser condutor')
                    if y.isnumeric():
                        for d in self.__lista_utilizador:  # resolver
                            if y in d.numero_estudante:
                                print('\nÉ necessário adicionar uma descrição do veiculo! ')
                                marca = input('Insira a marca do veiculo')
                                modelo = input('Insira o modelo do veiculo')
                                cor = input('Insira a cor do veiculo')
                                carro = marca + ' ' + modelo + ' ' + cor
                                print('\nInsira o número de lugares do veículo: ')
                                k = input()
                                if k.isnumeric():
                                    try:
                                        print('Este veiculo já realizou alguma viagem antes ?')
                                        print('\n'
                                              '\t1 - Sim\n'
                                              '\t2 - Não\n')
                                        numero = int(input('Insira o número da opção que pretende realizar'))
                                        if numero == 1:
                                            andar = input('Insira o número de viagens já realizados')
                                            if andar.isnumeric():
                                                u = Viatura(matricula_viatura, int(y), carro, int(k), int(andar))
                                                self.__lista_viatura.append(u)
                                                print('\n - - - Viatura adicionada com sucesso - - -\n')
                                                return
                                            else:
                                                print('--ERRO--\n'
                                                      '--ERRO--\n'
                                                      '--Tem de ser um número--')
                                                for c in '\nR-e-i-n-i-c-i-a-n-d-o\n':
                                                    print(c, end='')
                                                    sleep(0.1)
                                                self.add_viatura_correto()
                                        if int(numero) == 2:
                                            u = Viatura(matricula_viatura, int(y), carro, int(k))
                                            self.__lista_viatura.append(u)
                                            print('\n - - - Viatura adicionada com sucesso - - -\n')
                                            return
                                        else:
                                            print('--ERRO--\n'
                                                  '--ERRO--\n'
                                                  '--Tem de ser um número--')
                                            for c in '\nR-e-i-n-i-c-i-a-n-d-o\n':
                                                print(c, end='')
                                                sleep(0.1)
                                            self.add_viatura_correto()
                                    except ValueError:
                                        print('--ERRO--\n'
                                              '--ERRO--\n'
                                              '--Opção inválida--')
                                        for c in '\nR-e-i-n-i-c-i-a-n-d-o\n':
                                            print(c, end='')
                                            sleep(0.1)
                                        self.add_viatura_correto()
                                else:
                                    print('--ERRO--\n'
                                          '--ERRO--\n'
                                          '--Tem de ser um número--')
                                    for c in '\nR-e-i-n-i-c-i-a-n-d-o\n':
                                        print(c, end='')
                                        sleep(0.1)
                                    self.add_viatura_correto()
                        return
                    else:
                        print('--ERRO--\n'
                              '--ERRO--\n'
                              '--Tem de ser um número--')
                        for c in '\nR-e-i-n-i-c-i-a-n-d-o\n':
                            print(c, end='')
                            sleep(0.1)
                        self.add_viatura_correto()

            return

        else:
            print('--ERRO--\n'
                  '--ERRO--\n'
                  '--Matricula inserida de forma incorreta--')
            for c in '\nR-e-i-n-i-c-i-a-n-d-o\n':
                print(c, end='')
                sleep(0.1)
            self.add_viatura_correto()

    def list_viaturas(self):
        for i in self.__lista_viatura:
            print(i)

    def listar_viagens_volta_ISCTE(self):
        for i in self.__lista_voltar_para_ISCTE_viagem:
            print(i)

    def listar_viagens_sair_do_Iscte(self):
        for i in self.__lista_sair_do_ISCTE_viagem:
            print(i)

    def listar_viagens_morada_regressar_ISCTE(self, morada):
        for i in self.__lista_voltar_para_ISCTE_viagem:
            if morada == i.morada:
                print(i)
        return

    def listar_viagens_morada_comecar_no_ISCTE(self, morada):
        for i in self.__lista_sair_do_ISCTE_viagem:
            if morada == i.morada:
                print(i)
        return

    def adicionar_viagem(self):  # Corrigir o local tem erro
        x = input('Insira o número do estudante condutor que irá iniciar uma viagem')
        if x.isnumeric():
            for i in self.__lista_viatura:
                if str(x) in i.num_condutor:
                    try:
                        print('\n'
                              'Pretende adicionar uma viagem para:\n'
                              '1 - Iscte como ponto de partida\n'
                              '2 - Iscte como ponto de chegada\n'
                              '0 - Finalizar')
                        y = input('Insira a opção que pretende realizar')
                        while int(y) != 0:
                            if int(y) == 1:  # Viagem que começa no ISCTE
                                print('Insiras as horas, no formato 00:00')
                                Horas = input('Insira as horas da viagem')
                                if len(Horas) != 5 and Horas[2] != ':':
                                    print('--ERRO--\n'
                                          '--ERRO--\n'
                                          '--Horas inseridas de forma incorreta--')
                                    for c in '\nR-e-i-n-i-c-i-a-n-d-o\n':
                                        print(c, end='')
                                        sleep(0.1)
                                    self.adicionar_viagem()
                                else:
                                    boleia = str(int(i.num_lugares) - 1)
                                    print('Pretende inserir uma nova morada de destino - opcional\n'
                                          '1 - Sim\n'
                                          '2 - Não')
                                    confirmacao = int(input('Insira o número da opção que pretende fazer'))
                                    if confirmacao == 1:  # Mudar morada
                                        x = input('Insira o novo Concelho')
                                        y = input('Insira a nova Freguesia')
                                        z = f'{x},{y}'
                                        Nova_morada = z.title()
                                        idviagem = f'{i.matricula}-{i.viagens}'
                                        p = Viagem(i.num_condutor, idviagem, i.matricula, Horas, Nova_morada, boleia)
                                        self.__lista_sair_do_ISCTE_viagem.append(p)
                                        i.add_new_trip()
                                        print('\n - - - Viagem adicionada com sucesso - - -\n')
                                        return
                                    if confirmacao == 2:
                                        for T in self.__lista_utilizador:
                                            if T.numero_estudante in i.num_condutor:
                                                idviagem = f'{i.matricula}-{i.viagens}'
                                                U = Viagem(i.num_condutor, str(idviagem), i.matricula, Horas, T.morada,
                                                           boleia)
                                                self.__lista_sair_do_ISCTE_viagem.append(U)
                                                i.add_new_trip()
                                                print('\n- - - Viagem adicionada com sucesso - - -\n')
                                        return
                                    return
                            if int(y) == 2:  # Viagem para ir para ao ISCTE
                                print('Insiras as horas, no formato 00:00')
                                Horas = input('Insira as horas da viagem')
                                if len(Horas) != 5 or Horas[2] != ':':
                                    print('--ERRO--\n'
                                          '--ERRO--\n'
                                          '--Horas inseridas de forma incorreta--')
                                    for c in '\nR-e-i-n-i-c-i-a-n-d-o\n':
                                        print(c, end='')
                                        sleep(0.1)
                                    self.adicionar_viagem()
                                else:
                                    boleia = str(int(i.num_lugares) - 1)
                                    print('Pretende inserir uma nova morada de destino - opcional\n'
                                          '1 - Sim\n'
                                          '2 - Não')
                                    confirmacao = int(input('Insira o número da opção que pretende fazer'))
                                    if confirmacao == 1:
                                        x = input('Insira o novo Concelho')
                                        y = input('Insira a nova Freguesia')
                                        z = f'{x},{y}'
                                        idviagem = f'{i.matricula}-{i.viagens}'
                                        new = z.title
                                        U = Viagem(i.num_condutor, idviagem, i.matricula, Horas, new, boleia)
                                        self.__lista_voltar_para_ISCTE_viagem.append(U)
                                        i.add_new_trip()
                                        print('\n- - - Viagem adicionada com sucesso - - -\n')
                                        return
                                    if confirmacao == 2:
                                        for T in self.__lista_utilizador:
                                            if i.num_condutor in T.numero_estudante:
                                                idviagem = f'{i.matricula}-{i.viagens}'
                                                f = Viagem(i.num_condutor, str(idviagem), i.matricula, Horas, T.morada,
                                                           boleia)
                                                self.__lista_voltar_para_ISCTE_viagem.append(f)
                                                i.add_new_trip()
                                                print('\n- - - Viagem adicionada com sucesso - - -\n')
                                        return
                            else:
                                print('--ERRO--\n'
                                      '--ERRO--')
                                for c in '\nR-e-i-n-i-c-i-a-n-d-o\n':
                                    print(c, end='')
                                    sleep(0.1)
                                self.adicionar_viagem()
                        return
                    except ValueError:
                        print('--ERRO--\n'
                              '--ERRO--\n'
                              '--Opção inválida--')
                        for c in '\nR-e-i-n-i-c-i-a-n-d-o\n':
                            print(c, end='')
                            sleep(0.1)
                        self.adicionar_viagem()

            print('--ERRO--\n'
                  '--ERRO--\n'
                  '--Este Utilizador não tem Viatura--')
            self.adicionar_viagem()

        print('--ERRO--\n'
              '--ERRO--\n'
              '--Número inserido de forma incorreta--')
        for c in '\nR-e-i-n-i-c-i-a-n-d-o\n':
            print(c, end='')
            sleep(0.1)
        self.adicionar_viagem()

    def inscrever_passageiro_boleia(self):
        print('Lista de possiveis passageiros: \n')
        g.list_users()
        x = input('\n- Insira o número do aluno que vai apanhar boleia')
        if x.isnumeric():
            for i in self.__lista_utilizador:
                if x in i.numero_estudante:
                    print('\n'
                          'O utilizador vai realizar uma viagem para: \n'
                          '1 - Ir para o ISCTE\n'
                          '2 - Sair do ISCTE\n'
                          '0 - Finalizar o programa')
                    try:
                        y = int(input('\n- Insira o número da opção que pretende realizar\n'))
                        while y != 0:
                            if y == 1:
                                print('Viagens disponiveis para ir para o iscte: ')
                                g.listar_viagens_volta_ISCTE()
                                id = str(input('Insira o id da viagem'))
                                id_correto = id.upper()
                                for p in self.__lista_voltar_para_ISCTE_viagem:
                                    if id_correto == p.id_viagem:
                                        p.adicionar_passageiros(x)  # Função usada na classe viagem
                                        print('\n - - - Passageiro adicionada com sucesso - - -\n')
                                return
                            if y == 2:
                                print('Viagens disponiveis para ir para o iscte: ')
                                g.listar_viagens_sair_do_Iscte()
                                id = str(input('Insira o id da viagem'))
                                id_correto = id.upper()
                                for p in self.__lista_sair_do_ISCTE_viagem:
                                    if id_correto == p.id_viagem:
                                        p.adicionar_passageiros(x)  # Função usada na classe viagem
                                        print('\n - - - Passageiro adicionada com sucesso - - -\n')
                                return
                            else:
                                return

                        return
                    except ValueError:
                        print('--ERRO--\n'
                              '--ERRO--\n'
                              '--Tem de ser um número--')
                        for c in '\nR-e-i-n-i-c-i-a-n-d-o\n':
                            print(c, end='')
                            sleep(0.1)
                        return

            print('--ERRO--\n'
                  '--ERRO--\n'
                  '--Esse número de utilizador não existe--')
            for c in '\nR-e-i-n-i-c-i-a-n-d-o\n':
                print(c, end='')
                sleep(0.1)
            self.inscrever_passageiro_boleia()
        print('--ERRO--\n'
              '--ERRO--\n'
              '--Número inserido de forma incorreta--')
        for c in '\nR-e-i-n-i-c-i-a-n-d-o\n':
            print(c, end='')
            sleep(0.1)
        self.inscrever_passageiro_boleia()

    def limpar_concluidas_para_iscte(self):
        f = open('historico.csv', 'a')
        mammamia = []
        for i in self.__lista_voltar_para_ISCTE_viagem:
            if not i.ativa:
                f.write(str(i) + '\n')
                mammamia.append(i)
        for i in mammamia:
            self.__lista_voltar_para_ISCTE_viagem.remove(i)
        f.close()

    def limpar_concluidas_sair_iscte(self):
        f = open('historico.csv', 'a')
        mammamia_2 = []
        for i in self.__lista_sair_do_ISCTE_viagem:
            if not i.ativa:
                f.write(str(i) + '\n')
                mammamia_2.append(i)
        for i in mammamia_2:
            self.__lista_sair_do_ISCTE_viagem.remove(i)
        f.close()

    # Estatistica

    def top5(self):
        top5 = sorted(numpy.array(self.__lista_viatura), key=lambda viatura: viatura.viagens, reverse=True)
        # O sorted() irá ordenar a informação da lista do menor para o maior
        # O lambda é uma função anónima
        # reverse = True vai inverter a forma como vai ser ordenado
        top5 = top5[:5]
        # O top 5 vão ser as 5 primeiras viaturas que foram ordenadas pelo número de viagens
        ac = 1
        for i in top5:
            print('\t' + str(ac) + 'º: ' + i.matricula + ' --> ' + str(i.viagens) + ' Viagens')
            ac += 1

    def estatistica(self):
        print('Número de utilizadores registados na plataforma: ', end='')
        print(len(self.__lista_utilizador))
        print('Número de viaturas registadas na plataforma: ', end='')
        print(len(self.__lista_viatura))
        print('Número de viagens ativas: ')
        print('\t', 'Viagens de saida do ISCTE: ', end='')
        print(len(self.__lista_sair_do_ISCTE_viagem))
        print('\t', 'Viagens de regresso ao ISCTE: ', end='')
        print(len(self.__lista_voltar_para_ISCTE_viagem))
        print('Soma do número de viagens realizadas por viaturas registadas na plataforma: ', end='')
        total = 0
        for i in self.__lista_viatura:
            total += i.viagens
        print(total)
        print('Top 5 viaturas que realizaram mais viagens: ')
        self.top5()


# - - - - - - - - - - - - T4: LyftIUL - - - - - - - - - - - -

def menu(g):
    y = '\n--- Welcome to LyftIUL ---\n'
    s = 0
    while s != len(y):
        s = 0
        for i in y:
            print(i, end='')
            sleep(0.1)
            s += 1
    try:
        print('\n'
              '1 - Listar Utilizadores\n'
              '2 - Listar Viaturas\n'
              '3 - Listar viagens agendadas\n'
              '4 - Listar viagens agendadas com filtro por morada\n'
              '5 - Registar viagem (ida para o Iscte ou regresso a casa)\n'
              '6 - Inscrever passageiro em viagem\n'
              '7 - Registar e remover as viagens concluídas\n'
              '8 - Informações do sistema\n'
              '9 - Actividade por hora do dia\n'
              '10 - Adicionar Viatura\n'
              '11 - Adicionar Utilizador\n'
              '0 - Fechar programa')
        y = input('Insira o número da opção que pretende fazer')
        while int(y) != 0:
            if int(y) == 1:
                print('\n- - - Lista de Utilizadores - - -\n')
                g.list_users()
                print('\n')
            elif int(y) == 2:
                print('\n- - - Lista de Viaturas - - -\n')
                g.list_viaturas()
                print('\n')
            elif int(y) == 3:
                print('\n- - - Lista de Viagens - - -')
                print('\n- Lista de Viagens de ida ao ISCTE: ')
                g.listar_viagens_volta_ISCTE()
                print('\n- Lista de Viagens de saido do ISCTE: ')
                g.listar_viagens_sair_do_Iscte()
            elif int(y) == 4:
                morada = input('Insira a morada para filtrar as viagens')
                print('\n- - - Lista de Viagens Filtradas - - -')
                print('\n- Lista de Viagens de ida ao ISCTE: ')
                g.listar_viagens_morada_regressar_ISCTE(morada)
                print('\n- Lista de Viagens de saido do ISCTE: ')
                g.listar_viagens_morada_comecar_no_ISCTE(morada)
            elif int(y) == 5:
                print('\n- - - Lista de Utilizadores - - -')
                g.list_users()
                print()
                g.adicionar_viagem()
            elif int(y) == 6:
                g.inscrever_passageiro_boleia()
            elif int(y) == 7:
                g.limpar_concluidas_para_iscte()
                g.limpar_concluidas_sair_iscte()
                print('Procure pelo ficheiro "historico.csv"')
            elif int(y) == 8:
                g.estatistica()
            elif int(y) == 9:
                print('\n'
                      '1 - Ver a matriz\n'
                      '2 - Visionar gráfico (Esta opção fará com que o programa acabe)\n'
                      '3 - Dados sobre as viagens')
                opcao = input('Insira o número da opção que pretende realizar')
                if int(opcao) == 1:
                    matriz()
                    print_matriz()
                if int(opcao) == 2:
                    matriz()
                    grafico()
                    return
                if int(opcao) == 3:
                    print('\t- Média de viagens por hora: ', end='')
                    print(media())
                    print('\t- Hora do dia com maior número de boleias: ', end='')
                    print(boleias())
                    print('\t- Proporção de viagens ocorridas da parte da manhã: ', end='')
                    print(leite())
                    print('\t- Proporção de viagens ocorridas da parte de Tarde: ', end='')
                    print(100 - leite())
            elif int(y) == 10:
                g.add_viatura_correto()
            elif int(y) == 11:
                g.add_new_user()
            else:
                print('--ERRO--\n'
                      '--ERRO--\n'
                      '--Essa opção não existe--')
                for c in '\nR-e-i-n-i-c-i-a-n-d-o\n':
                    print(c, end='')
                    sleep(0.1)
                menu(g)

            print('\n'
                  '1 - Listar Utilizadores\n'
                  '2 - Listar Viaturas\n'
                  '3 - Listar viagens agendadas\n'
                  '4 - Listar viagens agendadas com filtro por morada\n'
                  '5 - Registar viagem (ida para o Iscte ou regresso a casa)\n'
                  '6 - Inscrever passageiro em viagem\n'
                  '7 - Registar e remover as viagens concluídas\n'
                  '8 - Informações do sistema\n'
                  '9 - Actividade por hora do dia\n'
                  '10 - Adicionar Viatura\n'
                  '11 - Adicionar Utilizadores\n'
                  '0 - Fechar programa')
            y = input('Insira o número da opção que pretende fazer')
    except ValueError:
        print('\nÉ necessário escolher um dos números!')
        for c in '\nR-e-i-n-i-c-i-a-n-d-o\n':
            print(c, end='')
            sleep(0.1)
        menu(g)


# - - - - - - - - - - - - T5: Actividade por hora do dia - - - - - - - - - - - - - - -
def matriz():
    mydata = numpy.zeros([24, 2], int)
    f = open('historico.csv', 'r')
    ler = f.readline()
    # ler as linhas do ficheiro 'historico'
    while ler != '':
        x = ler.split(',')
        # A variável x vai dividir por virgulas
        if x[2][11] == '0':
            horas = int(x[2][12])
        # se segunda virgula, elemento nº11, for zero, então o elemento nº12 é as horas, exemplo: 09:00
        else:
            horas = int(x[2][11:13])
        # As horas serão os elementos nºo 11 e 12, estando o 13 excluido, após segunda virgula, exemplo: 12:00
        mydata[horas, 0] += 1
        # ordena a linhas da matriz pelas horas
        v = ler[ler.find('['):-1]
        z = v.split(',')
        if z[0] == '[]':
            passageiros = 0
        # Se a lista tiver vazia, não há passageiros
        else:
            passageiros = len(z)
        mydata[horas, 1] += passageiros
        # Na segunda coluna irão ficar o nº de passageiros
        ler = f.readline()
    return mydata


def print_matriz():
    x = matriz()
    print(x)


def grafico():
    x = matriz()
    plt.plot(x)


def media():
    x = matriz()
    s = 0
    for i in x:
        s += i[0]
    # Somar todos os valores da primeira coluna
    return round(s / 24, 3)
    # arredondar com 3 casas decimais


def boleias():  # Hora do dia com maior número de boleias
    x = matriz()
    s = []
    for i in x:
        s.append(i[1])
    # Criar uma lista com todos os elementos da segunda coluna
    y = max(s)
    # Y = valor máximo da lista
    return s.index(y)
    # Vai retornar as horas correspondentes á linha onde se encontra o valor máximo


def leite():  # Proporção de viagens ocorridas da parte da manhã #sum
    x = matriz()
    t = []
    for i in x:
        t.append(i[0])
    # Criar uma lista com todos os 24 elementos da primeira coluna
    y = sum(t)
    # Somar todos os 24 elementos da lista
    m = sum(t[:12])
    # Somar os 12 primeiros elementos da lista
    return round((m / y) * 100, 3)
    # devolver em percentagem com 3 casas decimais


# - - - - - - - - - - - - - - - DateTime - - - - - - - - - - - - - - -

# date_time
def get_datetime(t):
    myt = time.fromisoformat(t)
    now = datetime.now()
    mydt = datetime(now.year, now.month, now.day, myt.hour, myt.minute)
    if (mydt - now).days < 0:
        mydt += timedelta(days=1)
    return mydt


# - - - - - - - - - - - - - - - Pré inserido - - - - - - - - - - - - - -
g = Gestor()

u1 = Utilizador('55555', 'Pedro Mota', 'Loures, Pirescoxe', 'pedro@iscte-iul.pt')
u2 = Utilizador('66666', 'Maria Mercedes', 'Sintra, Rio de Mouro', 'maria@iscte-iul.pt', '966666666')
u3 = Utilizador('102111', 'Manuel das Boleias', 'Sintra, Colares', 'manuel@iscte-iul.pt', '962222222')
u4 = Utilizador('19', 'yha', 'Amazonia, aquela árvore', 'k@lou-iul.pt', '969696969')
u5 = Utilizador('379', 'juan', 'Monte, evereste', 'tico@teco-iul.pt', '123456789')
u6 = Utilizador('123', 'sem carro', 'sem, carro', 'sem@carro-iul.pt', '984198327')

g.add_user(u1)
g.add_user(u2)
g.add_user(u3)
g.add_user(u4)
g.add_user(u5)
g.add_user(u6)

v1 = Viatura('TM-22-11', '55555', 'Tesla Model 3 azul', '5', 0)
v2 = Viatura('44-TA-00', '66666', 'Toyota Aygo cinzento', '4', 35)
v3 = Viatura('55-MX-55', '102111', 'Mazda MX-5 vermelho', '2', 10)
v4 = Viatura('55-MX-55', '19', 'Mazda MX-5 vermelho', '2', 10)
v5 = Viatura('99-AB-77', '29', 'BMW 3D preto', '2', 2)
v6 = Viatura('88-CD-66', '45', 'Volvo V40 cizento', '2', 1)

g.add_viatura(v1)
g.add_viatura(v2)
g.add_viatura(v3)
g.add_viatura(v4)
g.add_viatura(v5)
g.add_viatura(v6)

t1 = Viagem('55555', 'TM-22-11-5', 'TM-22-11', '23:19', 'Loures, Pirescoxe', 5)
t2 = Viagem('66666', '44-TA-00-7', '44-TA-00', '23:19', 'Sintra, Rio de Mouro', 7)
t3 = Viagem('102111', '55-MX-55-3', '55-MX-55', '23:19', 'Sintra, Colares', 3)
t4 = Viagem('26', '55-MX-21-2', '55-MX-21', '23:19', 'Vulcão, poeira', 2)
t5 = Viagem('24324', '93-GX-25-1', '93-GX-25', '23:19', 'BUDA, PANDA', 1)
t6 = Viagem('19', '55-MX-55-2', '55-MX-55', '23:19', 'Amazonia, aquela árvore', 2)
t7 = Viagem('29', '99-AB-77-9', '99-AB-77', '19:19', 'Planeta, Terra', 9)
t8 = Viagem('45', '88-CD-66-4', '88-CD-66', '14:45', 'Estrela, Sol', 4)

g.bruh(t1)
g.bruh_sai(t1)
g.bruh(t2)
g.bruh_sai(t2)
g.bruh(t3)
g.bruh_sai(t3)
g.bruh(t4)
g.bruh_sai(t4)
g.bruh(t5)
g.bruh_sai(t5)
g.bruh(t7)
g.bruh_sai(t8)