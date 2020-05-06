#Curso: Minicurso de Python Básico
#Data: 03/04/2020

#Exercício 03
soma=0
i=0
for x in range(1, 7):
    numero = int(input("Digite um número inteiro qualquer: "))
    if numero % 2 == 0:
        soma+=numero 
        i+=1
print("A soma de todos os {} números pares encontrados é igual {}.".format(i,soma))