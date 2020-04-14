def verificaNumero(numero):
    if numero >0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero é um número nulo ou neutro, não é negativo e nem positivo.")
num = int(input("Digite um número: "))
verificaNumero(num)