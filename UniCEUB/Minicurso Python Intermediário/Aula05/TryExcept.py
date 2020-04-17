def lerInteiro():
    while True:
        try:
            n = int(input("Digite um número intiero qualquer: "))
        except:
            print("O valor digitado não é um número inteiro.")
        else:
            return n
        finally:
            print("FIM")
n1 = lerInteiro()
print(f"O valor digitado foi o {n1}.")