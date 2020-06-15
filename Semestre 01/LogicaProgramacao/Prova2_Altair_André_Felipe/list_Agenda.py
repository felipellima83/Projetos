# Crie uma Agenda Telefônica em que seja possível inserir, pesquisar, apagar, alterar, gravar e mostrar toda a agenda usando listas() e suas funções nativas.

import time

agenda = []  # criando agenda/lista vazia


# DETERMINANDO AS FUNÇÕES Def

# funções de cadastro de nome/telefone
def inserir_nome():
    return input("Olá! Por favor, qual é o seu nome: ")


def inserir_telefone():
    return input("Obrigado! Agora digite seu número de Telefone: ")


# função de mostrar o cadastro já realizado
def mostra_dados(nome, telefone):
    print("Nome: %s Telefone: %s" % (nome, telefone))


# função para gerar um arquivo com os dados registrados anteriormente! A criptografia é só um atrativo!
def inserir_nome_arquivo():
    return input("Vamos gravar sua agenda em um arquivo seguro/criptografado! Digite o nome do arquivo: ")


# função que vai pesquisar na lista() pelo nome cadastrado
def pesquisar(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):  # FOR realizado baseado na quantidade de nomes registrados (enumerate)
        if e[0].lower() == mnome:  # Se nome (minúsculo) for encontrado retorna p, senão retorna None (nenhum)
            return p
    return None


# Função de criação de Registros/Cadstros
def novo_registro():
    global agenda
    nome = inserir_nome()
    telefone = inserir_telefone()
    agenda.append([nome, telefone])
    print()
    print("Novo Registro realizado com sucesso...")
    time.sleep(1.2)


# Função para apagar registros da agenda/lista()
def apagar():
    global agenda
    nome = inserir_nome()  # realiza uma pesquisa pelo nome registrado
    p = pesquisar(nome)
    if p != None:  # se encontrado (diferente de nenhum, ou seja, algum nome encontrado) então delete tal registro
        del agenda[p]
        print("Aguarde...")
        time.sleep(2)
        print("Registro eliminado com sucesso...")
        time.sleep(1.2)
    else:
        print("Nome não encontrado! Não existe esse registro no arquivo!")
        time.sleep(3)


# Função para alterar dados da agenda/lista()
def alterar():
    p = pesquisar(inserir_nome())
    if p != None:  # se encontrado (diferente de nenhum, ou seja, algum nome encontrado) então mostre tal registro
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print()
        print("Encontrado! Por favor, altere abaixo os dados que desejar!\n")
        mostra_dados(nome, telefone)
        print()
        nome = inserir_nome()  # Chama as funções para realizar as altereções desejadas
        telefone = inserir_telefone()  # Chama as funções para realizar as altereções desejadas
        agenda[p] = [nome, telefone]
        print()
        print("Dados Alterados com sucesso...")
        time.sleep(2)
    else:
        print()
        print("Nome não encontrado! Realize o registro usando a opção [1] - Novo Registro")
        time.sleep(4)


# Função para "imprimir" os dados cadastrados anteriormente
def lista():
    print("\nSua Agenda atualmente contém esses registros:\n\n------")
    for e in agenda:
        mostra_dados(e[0], e[1])
    print("------\n")
    time.sleep(5)


# Função que lê (abre) o arquivo gravado anteriormente! Observação: precisei pesquisar sobre criação/gravação/abertura
# de arquivos de dados de listas e alguns comandos citados abaixo precisei copiar de exemplos de livros e pdfs desse
# assunto, pois ainda não visto em aula.
def lê():
    global agenda
    nome_arquivo = inserir_nome_arquivo()
    arquivo = open(nome_arquivo, "r", encoding="utf-8")
    agenda = []
    for l in arquivo.readlines():
        nome, telefone = l.strip().split("#")
        agenda.append([nome, telefone])
    arquivo.close()
    print("Lendo Arquivo de dados da Agenda...")
    time.sleep(2)


# Função que grava (write) a agenda/lista() em um arquivo com nome definido pelo usuário
def grava():
    nome_arquivo = inserir_nome_arquivo()
    arquivo = open(nome_arquivo, "w", encoding="utf-8")
    for e in agenda:
        arquivo.write("%s#%s\n" % (e[0], e[1]))  # Grava um arquivo com todos os dados das posições da lista
    arquivo.close()
    print("Arquivo Criptografado gravado com sucesso...")
    time.sleep(1.5)


# Função que define se usuário escolheu opção correta dentre as oferecidas no menu, utilizando While/if
def valida_opcao(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print("Opção inválida! Por favor selecione entre %d e %d" % (inicio, fim))
            print("Fim de Execução da Agenda!")

    print("Fim de Execução da Agenda!")
# Função que executa o Menu para o usuário selecionar a opção desejada
def menu():
    print("""
   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
   Bemvindo(a) a sua Nova Agenda Telefônica!
   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
   
   [1] - Novo Registro
   [2] - Alterar Registro
   [3] - Apagar Registro
   [4] - Listar Agenda Completa
   [5] - Gravar Arquivo Criptografado da Agenda
   [6] - Lê Arquivo Criptografado da Agenda

   [0] - Sai da Agenda
""")
    return valida_opcao("Escolha uma opção --> ", 0, 6)


# Análise da opção desejada pelo usuário e chamada da função correspondente
while True:
    opção = menu()
    if opção == 0:
        break  # Sai da Agenda
    elif opção == 1:
        novo_registro()
    elif opção == 2:
        alterar()
    elif opção == 3:
        apagar()
    elif opção == 4:
        lista()
    elif opção == 5:
        grava()
    elif opção == 6:
        lê()