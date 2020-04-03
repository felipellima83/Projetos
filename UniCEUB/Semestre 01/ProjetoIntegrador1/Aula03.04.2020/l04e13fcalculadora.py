''' 13   Criar um programa que simule uma calculadora com as quatro operações basicas, enquanto o usuario não digitar o opção "5" o programa ficará em funcionando
1)soma
2)subtração
3)multiplicação
4)divisão
5)sair
OBS: cuidar divisão por 'zero'
'''
while True:
    operador = int(input("Digite o numero correspondente para realizar a operação desejada.\n(1) Soma\n(2) Subtração\n(3) Multiplicação\n(4) Divisão\n(5) Encerrar\nOperador:"))
    if operador == 5:
        print("Calculadora encerrada!")
        break
    if operador == 1:
        operando1 = float(input("Digite o 1º operando: "))
        operando2 = float(input("Digite o 2º operando: "))
        result = operando1+operando2
    if operador == 2:
        operando1 = float(input("Digite o 1º operando: "))
        operando2 = float(input("Digite o 2º operando: "))
        result = operando1-operando2
    if operador == 3:
        operando1 = float(input("Digite o 1º operando: "))
        operando2 = float(input("Digite o 2º operando: "))
        result = operando1*operando2
    if operador == 4:
        operando1 = float(input("Digite o 1º operando: "))
        operando2 = float(input("Digite o 2º operando: "))
        result = operando1/operando2
    print("O resultado é {:.2f}.".format(result))