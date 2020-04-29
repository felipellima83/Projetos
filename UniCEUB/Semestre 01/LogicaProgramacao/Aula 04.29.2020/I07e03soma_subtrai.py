def soma (a,b):
    return a + b

def subtrai (a,b):
    return a - b

if __name__ == "__main__":
    num1 = int(input(" Digite o primeiro valor: "))
    num2 = int(input(" Digite o segundo valor: "))
    print(f"A soma é igual a {soma(num1,num2)}.")
    print(f"A subtração é igual a {subtrai(num1,num2)}.")