#Curso: Minicurso de Python Básico
#Data: 03/04/2020

#Exercício 06

from datetime import date

anoAtual = date.today().year
maior = 0
menor = 0
for x in range(1, 8):
    ano = int(input("Ano de nascimento da {}ª pessoa: ".format(x)))
    if anoAtual - ano >=18:
        maior+=1
    else:
        menor+=1
print("{} pessoas são maiores de idade e {} ainda são menores de idade.".format(maior, menor))