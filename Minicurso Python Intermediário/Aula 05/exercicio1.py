def lerInteiro():
    while True:
        try:
            n = int(input("Digite um número inteiro: "))
        except ValueError:
            print("\33[31mERRO: digite um número inteiro válido.\33[m")
            continue
        else:
            return n


n1 = lerInteiro()
print(f'O valor inteiro informado foi {n1}')
