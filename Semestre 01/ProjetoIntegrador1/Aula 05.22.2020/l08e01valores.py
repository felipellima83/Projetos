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
l_valores = [ ]                                # Lista inicialmente vazia
for i in range(0, 3):                        # Repete 3 vezes
    # Recebe um número do usuário e adiciona à lista
    num = int(input("Digite um número: "))
    l_valores.append(num)
# mostra todos os valores da lista
print ('Valores da lista:')
print (l_valores)              # print (l_valores[ : : ]) 
'''
Alterações:
a. Mostre os valores armazenados na lista na vertical usando o for com a lista.
b. Mostre os valores armazenados na lista na vertical usando o for com a lista.
    E mostre também suas respectivas posições.
c. Mostre os valores armazenados na lista usando notação de vetor, use o for com range.
d. Mostre os valores armazenados na lista usando notação de vetor, use o for com range.
    E suas respectivas posições usando notação
        DICAS:
for conteudo in l_valores:            # a.
    print(conteudo)
ct = 0                                             # b.
print ('Posição -> Valor')
for conteudo in l_valores:
    print(ct , " -> ", conteudo)
    ct = ct + 1
for i in range(0, 3):                         # c. 
    print(l_valores [ i ] )
print ('Posição -> Valor')              # d.
for i in range(0, 3):                         
    print (i, " - ", l_valores[i] )
    #print("[", i, "] : ", l_valores[i])
    
'''
