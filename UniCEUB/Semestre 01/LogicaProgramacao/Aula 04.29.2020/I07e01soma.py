def soma (a,b):
    return a + b

def mostra_soma(a,b):
    soma = a + b
    print(f"A soma é igual a {soma}.")

if __name__ == "__main__":
    num1 = float(input("Qual o primeiro número a ser somado? "))
    num2 = float(input("Qual o segundo número a ser somado? "))
    mostra_soma(num1,num2)