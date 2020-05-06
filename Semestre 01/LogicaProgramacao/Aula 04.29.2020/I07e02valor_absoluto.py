def valor_absoluto (x):
    if x < 0:
        return x * -1
    return x

if __name__ == "__main__":
    num1 = float(input("Qual o valor a ser passado o módulo? "))
    print(f"O módulo do número digitado é {abs(num1)}.")#abs função nativa