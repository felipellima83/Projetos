def soma(x,y):
    resultado = x+y
    return resultado

def subtracao(x,y):
    resultado = x-y
    return resultado

def multiplicacao(x,y):
    resultado = x*y
    return resultado

def divisao(x,y):
    if y == 0:
        return 'O denominador não pode ser 0!'
    resultado = x/y
    return resultado

def numeroUsuario():
    numero = float(input('Informa um número: '))
    return numero

opcao = 1
while opcao != 0:
    opcao = int(input('\nMENU\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair\n\nEscolha uma das opções: '))
    if opcao == 1:
        x = numeroUsuario()
        y = numeroUsuario()
        print(soma(x,y))
    elif opcao == 2:
        x = numeroUsuario()
        y = numeroUsuario()
        print(subtracao(x,y))
    elif opcao == 3:
        x = numeroUsuario()
        y = numeroUsuario()
        print(multiplicacao(x,y))
    elif opcao == 4:
        x = numeroUsuario()
        y = numeroUsuario()
        print(divisao(x,y))
    elif opcao == 0:
        print('Calculadora Finalizada!')
    else:
        print('Opção inválida! Tente novamente.')
    