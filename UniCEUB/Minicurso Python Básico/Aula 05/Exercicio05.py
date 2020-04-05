#Curso: Minicurso de Python Básico
#Data: 03/04/2020

#Exercício 05

numero = int(input("Digite um número para saber se ele é primo: "))
i = 0
for x in range(1, numero+1):
    if numero % x == 0:
        i+=1
print("O número {} foi divisível {} vezes.".format(numero, i))
if i == 2:
    print("O número {} é primo.".format(numero))
else:
    print("O número {} não é primo.".format(numero))