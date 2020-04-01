b = 0
i = int(input("Digite um número maior que 1: "))
while b < i:
    if b % 2 == 0:
        b = b+2
        print(b, end=" ")
    else:
        b = b+2