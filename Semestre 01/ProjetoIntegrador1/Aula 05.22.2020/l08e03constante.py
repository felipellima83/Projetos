'''
1. Leia trinta valores inteiros digitados pelo usuário e armazene-os numa lista.
Gere a tela de saída com os valores armazenados na lista.

2. Refaça o programa anterior, mostre os valores armazenados no vetor na ordem
inversa da entrada de dados.

3. No programa anterior, usamos o valor trinta, tamanho da lista, em vários pontos
do programa. Para facilitar a manutenção, refaça o exercício utilizando o conceito
de constante.
- Obs.: Para simplificar os testes, substitua trinta por três.
-----------------------------------------------------------------------------------
'''
# Define o tamanho da lista. Em Python não existem constantes como em outras
# linguagens, portanto ainda é possível alterar essa variável. Porém, por
# convenção mantenha constantes em maiúsculas, assim como em outras
# linguagens e não altere seu valor.

TAM_LISTA = 3

# lista inicialmente vazia
l_valores = []
# repete TAM_LISTA vezes
for i in range(0, TAM_LISTA):
    # recebe um número do usuário e adiciona à lista
    num = int(input("Digite um número: "))
    l_valores.append(num)
# mostra todos os valores da lista
for i in range(0, TAM_LISTA):  # for i in range(0, TAM_LISTA, 1):
    print("[", i, "] : ", l_valores[i])

'''
Alterações
a. Uma outra forma de simular o comportamento de constantes é escrever uma
função que retorne seu valor. Faça a simulação.
            DICAS:
# TAM_LISTA = 3          # a.
def TAM_LISTA():         
    return 3
#for i in range(0, TAM_LISTA):    
for i in range(0, TAM_LISTA () ) :
'''
