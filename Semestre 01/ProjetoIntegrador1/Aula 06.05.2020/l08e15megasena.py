'''
Construa um programa da Mega sena, sortear 6 numeros entre 0 e 60.

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
'''
    a) verifique a pontuação do usuario, peça para o usuario escolher 6 numeros
e depois o programa deverá mostrar quantos numeros o usuario acertou e os
numeros sorteados
    
     
'''
