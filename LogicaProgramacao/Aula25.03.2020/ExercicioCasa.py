#Professor: Antônio Barbosa Junior
#Disciplina: Lógica de programação
#Aluno: Felipe Ferreira Lima e Lima
#Matrícula: 22001310
#Data: 25/03/2020

# Construa um programa que calcule a média aritmética dos números pares.
# O usuário fornecera os valores de entrada que pode ser um número qualquer, par ou impar.
# Condição de saída será o número 0.

i = 0
soma = 0
numero = 1
print("Para parar o programa, digite o valor 0!")
while numero != -1:
    numero = int(input("Qual o número a ser inserido? "))
    if numero == 0:
        break
    resto = numero%2
    if resto == 0:
        i += 1
        soma += numero
if i != 0:
    print("A soma dos valores pares digitados foi {} e a média é {:.2f}.".format(soma, soma/i))
else:
    print("Você não digitou nenhum número par!")