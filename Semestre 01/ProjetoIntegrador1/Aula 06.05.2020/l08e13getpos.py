'''
Cria uma lista com 30 numeros randomicos entre 0 à 10, depois peça
para o usuario digitar um numero especifico.
O programa deverá retornar quantas vezes o mumero aparece na lista
e mostra as posições dele na lista
'''
import random

lista=[]
lista_posicoes = []
elementos = 30
for i in range(0,elementos):
    lista.append(random.randint(0,10))
print(lista)

pesquisa = int(input("Pesquisar qual número? "))
qtd=lista.count(pesquisa)
print("Quantidade: ", qtd)

for i in range(0,elementos):
    if lista[i] == pesquisa:
        lista_posicoes.append(i)

for i in lista_posicoes:
    print("Posição: ", i)
    
lista.sort()
print(lista)