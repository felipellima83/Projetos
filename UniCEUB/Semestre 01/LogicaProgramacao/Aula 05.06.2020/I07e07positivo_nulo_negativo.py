def positivo_nulo_negativo (a):
    if a > 0:
        ret = 1
    elif a < 0:
        ret = -1
    else:
        ret = 0
    return ret

def positivo_nulo_negativo2 (a):
    if a > 0:
        print("Resposta: Positivo")
    elif a < 0:
        print("Resposta: Negativo")
    else:
        print("Resposta: Nulo")

if __name__ == "__main__":
    valor = float(input("Qual número? "))
    resposta = positivo_nulo_negativo(valor)
    print("Resposta: ", resposta)
    positivo_nulo_negativo2(valor)