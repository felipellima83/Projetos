#Curso: Minicurso de Python Básico
#Data: 02/04/2020

#Exercício 03
menor = 500
maior = 0
for i in range(5):
    peso = float(input("Qual o peso da {}ª pessoa? ".format(i + 1)))
    if peso >= maior:
        maior = peso
    if peso < menor:
        menor = peso
print("O mais leve pesa {} kg e o mais pesado pesa {} kg.".format(menor,maior))