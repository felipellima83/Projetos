'''
Veja os vídeos abaixo:
video1 - Introdução a Listas
https://www.youtube.com/watch?v=YeaB5IgS2rY&index=25&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe
video2 - Listas dentro de listas, Adicionar novos elemetos a listas(append) 
https://www.youtube.com/watch?v=zzRiX_nIIMc&index=26&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe

- 1. Leia trinta valores inteiros digitados pelo usuário e armazene-os numa lista.
Gere a tela de saída com os valores armazenados na lista.
- Obs.: Para simplificar os testes, substitua trinta por três.
-Inicie com uma lista vazia;
-Utilize a funcao.append() para adicionar um elemento na lista
ex: lista.append(valor)
--------------------------------------------------------------------------
'''
#inicio
lista = []
ct=0
tamanho_lista = int(input("Quantos elementos tem na lista? "))
while ct < tamanho_lista:
    num = int(input(f"Digite o {ct+1}º número a ser inserido na lista: ")) 
    lista.append(num)
    ct+=1
print(lista)

ct2=0
#Alteração A
for i in range(0,tamanho_lista):
    #Alteração B
    print(f"[{ct2}] = ", lista[i])
    ct2+=1


'''
Alterações:
a. Mostre os valores armazenados na lista na vertical usando o for com a lista.
b. Mostre os valores armazenados na lista na vertical usando o for com a lista.
    E mostre também suas respectivas posições.
c. Mostre os valores armazenados na lista usando notação de vetor, use o for com range.
d. Mostre os valores armazenados na lista usando notação de vetor, use o for com range.
    E suas respectivas posições usando notação
        DICAS:
    
'''
