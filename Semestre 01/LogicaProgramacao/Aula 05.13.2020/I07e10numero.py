def compara_valores (a,b):
    if a == b:
        ret = 0
    elif a > b:
        ret = 1
    else:
        ret = -1
    return ret

def compara_valores2 (a,b):
    if a > b:
        print("Resposta: Primeiro maior")
    elif a < b:
        print("Resposta: Segundo maior")
    else:
        print("Resposta: Iguais")

def le_numero (mensagem):
    return float(input(mensagem))

if __name__ == "__main__":
    #print(compara_valores(float(input("Qual número? ")),float(input("Qual número? "))))
    #n1 = float(input("Qual número? "))
    #n2 = float(input("Qual número? "))
    #compara_valores2(n1,n2)
    n3 = le_numero("Digite o primeiro valor: ")
    n4 = le_numero("Digite o segundo valor: ")