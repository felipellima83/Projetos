def maximo(a,b):
    if a > b:
        maior = a
    elif a < b:
        maior = b
    else:
        maior = a
    return maior

def le_valor (mensagem):
    a = float(input(mensagem))
    return a

if __name__ == "__main__":
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    retorno = maximo(n1,n2)
    print(f"O maior é {retorno}.")
    def le_valor(n1)