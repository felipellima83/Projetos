"""
12   Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120
"""

fatorial = int(input("Fatorial de: "))
result=1
i=1
while i <= fatorial:
    result *= i
    i += 1
print("O resultado do fatorial de {} é {}.".format(fatorial, result))