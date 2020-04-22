'''
25. Escreva o programa que mostra todos os valores de um dado. Lembre-se do
objeto “dado” que normalmente é utilizado em jogos de mesa.

Modificações

a. Mostre somente os lados com números pares
b. Mostre somente os lados com números impares
c. Faça um programa, no qual utilize a função randomica para sortear
"N" vezes um dos lados do dado, o programa deverá mostrar cada
numero sorteado e mostrar a soma dos valores sorteados.

dica: importar o modulo do python "Random" e utilizar as funções dele
'''

import random

repeticao = int(input("Quantas vezes lançar o dado? "))
lista1=[] #lista 1 declarada, mas está vazia
lista2=[] #lista 2 declarada, mas está vazia

# Letras A e B
for x in range(1, 7):
    print(x, end=' ')
    if x%2==0:
        #y=x
        lista1.append(x) #lista.append() - adiciona um valor para lista
    if x%2==1:
        #z=x
        lista2.append(x)
print("\n",lista1,lista2)

# Letra C
print("Os números sorteados foram:")
soma=0
for i in range(repeticao):
    x = random.randint(1,6)
    soma+=x
    print(x, end=" ")
print("\nA soma dos valores sorteados {} vezes é igual a {}.".format(repeticao,soma))