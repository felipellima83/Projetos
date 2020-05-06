def soma (a,b):
    return a + b

def subtrai (a,b):
    return a - b

if __name__ == "__main__":
    num1 = int(input(" Digite o primeiro valor: "))
    num2 = int(input(" Digite o segundo valor: "))
    num3 = int(input(" Digite o 3 valor: "))
    num4 = int(input(" Digite o 4 valor: "))
    while True:
        escolha = int(input("Qual operação quer realizar, 1 - soma ou 2 - subtração? "))
        if escolha == 1:
            print(f"A soma é igual a {soma(soma(num1,num2),soma(num3,num4))}.")
            break
        elif escolha == 2:
            print(f"A subtração é igual a {subtrai(num1,num2)}.")
            break
        else:
            print("Opção inválida!")