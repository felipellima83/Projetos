#Curso: Minicurso de Python Básico
#Data: 03/04/2020

#Exercício 01
inicial = int(input("Qual valor inicial do range? "))
final = int(input("Qual valor final do range? "))
passo = int(input("Qual valor do passo do range? "))
for i in range(inicial, final, passo):
    print(i)