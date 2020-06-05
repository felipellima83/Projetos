'''
15. Simule o sorteio do jogo mega-sena. Sorteie seis números entre 1 e 60 e armazene-os num vetor.

16.Refaça o exercício anterior evitando que haja repetição nos números sorteados, ou seja, para cada
número sorteado deveremos verificar se ele já foi sorteado anteriormente.
'''
import random

lista_sorteado=[]
lista_escolhido=[]
elementos = 6
for i in range(0,elementos):
    lista_sorteado.append(random.randint(0,60))

ct=0
for i in range(0,elementos):
    num = int(input(f"Digite o {ct+1}º escolhido? "))
    ct+=1
    lista_escolhido.append(num)

ct2=0
for i in lista_escolhido:
    if (i in lista_sorteado):
        ct2+=1


print(lista_sorteado)
print(f"Você acertou {ct2} dos sorteados!")

#Tamanho da lista
TAM_LISTA = 6

# inicia a lista vazia
lista = []
















'''ALTERAÇÕES:
a. Agora permita que o usuário interaja com o programa. Peça que ele insira 6 números e mostre quantos numeros ele acertou do jogo.

'''

'''RESOLUÇÕES:


'''
