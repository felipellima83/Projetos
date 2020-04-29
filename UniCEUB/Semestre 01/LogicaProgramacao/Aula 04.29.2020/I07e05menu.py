def soma (a,b):
    return a + b

def subtrai (a,b):
    return a - b

def multiplicacao (a,b):
    return a + b

def divisao (a,b):
    return a / b
def menu ():
    operacao = input("Qual operação quer realizar, (+) soma, ou (-) subtração, ou (x) multiplicacao, ou (/) divisao? ")
    return operacao

if __name__ == "__main__":
    operacao = menu()
    num1 = int(input(" Digite o primeiro valor: "))
    num2 = int(input(" Digite o segundo valor: "))    
    while True:
        if operacao == '+':
            print(f"A soma é igual a {soma(num1,num2)}.")
            break
        elif operacao == '-':
            print(f"A subtração é igual a {subtrai(num1,num2)}.")
            break
        elif operacao == 'x':
            print(f"A multiplicação é igual a {multiplicacao(num1,num2)}.")
            break
        elif operacao == '/':
            print(f"A divisão é igual a {divisao(num1,num2)}.")
            break
        else:
            print("Opção inválida!")