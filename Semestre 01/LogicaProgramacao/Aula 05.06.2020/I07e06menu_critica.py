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
    while (operacao != '+' and operacao != '-' and operacao != 'x' and operacao != '/'):
        print("Opção inválida!")        
        operacao = input("Qual operação quer realizar, (+) soma, ou (-) subtração, ou (x) multiplicacao, ou (/) divisao?")
    return operacao
    

if __name__ == "__main__":
    retorno_menu = menu()
    num1 = int(input(" Digite o primeiro valor: "))
    num2 = int(input(" Digite o segundo valor: "))
    if retorno_menu == '+':            
        print(f"A soma é igual a {soma(num1,num2)}.")
    elif retorno_menu == '-':
        print(f"A subtração é igual a {subtrai(num1,num2)}.")
    elif retorno_menu == 'x':
        print(f"A multiplicação é igual a {multiplicacao(num1,num2)}.")
    else:
        print(f"A divisão é igual a {divisao(num1,num2)}.")