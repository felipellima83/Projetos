'''
Veja os vídeos abaixo:
video1 - Introdução a Listas
https://www.youtube.com/watch?v=YeaB5IgS2rY&index=25&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe
video2 - Listas dentro de listas, Adicionar novos elemetos a listas(append) 
https://www.youtube.com/watch?v=zzRiX_nIIMc&index=26&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe


Criando uma matriz
https://www.youtube.com/watch?v=EGmlFdwD4C4


'''

def crie_matriz(n_linhas, n_colunas, valor):
    ''' (int, int, valor) -> matriz (lista de listas)

    Cria e retorna uma matriz com n_linhas linha e n_colunas
    colunas em que cada elemento é igual ao valor dado.
    '''

    matriz = [] # lista vazia
    for i in range(n_linhas):
	        # cria a linha i
	        linha = [] # lista vazia
	        for j in range(n_colunas):
	            linha.append(valor)
	
	        # coloque linha na matriz
	        matriz.append(linha)
	
    return matriz
	
	#-----------------------
#programa principal

A = crie_matriz(3,3,1)
print(A)

'''
Alterações:
a. Alterar a função "crie_matriz" para o usuario digiter o valor de cada posição.

b. Criar a função "imprimir_matriz', apos a execução desta função,
deverá ser mostrada a seguinte matriz na tela:

[1] [2] [3]
[4] [5] [6]
[7] [8] [9]

c) Multiplique a matriz por um valor escalar digitado pelo usuário:
exemplo -  2*Matriz, o resultado será:

2  4  6
8  10 12
14 16 18

d) Crie uma função que devolva ao programa principal quantos numeros pares
a Matriz possue.

e) Crie uma função que devolva o maior numero dentro de uma Matriz


'''
