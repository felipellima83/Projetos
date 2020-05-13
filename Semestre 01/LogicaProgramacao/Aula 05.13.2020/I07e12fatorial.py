def fatorial (a):
    result=1
    if a < 0:
        print("Valor inválido!")
    else:
        for i in range(1,a+1,1):
            result *= i
        return result

if __name__ == "__main__":    
    n = int(input("Digite um número inteiro para saber seu fatorial: "))
    print(f"O fatorial de {n} é {fatorial(n)}.")