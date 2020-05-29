'''
- 1. Leia trinta valores inteiros digitados pelo usuário e armazene-os numa lista.
Gere a tela de saída com os valores armazenados na lista.

- 2. Refaça o programa anterior, mostre os valores armazenados no vetor na ordem
inversa da entrada de dados.
- Obs.: Para simplificar os testes, substitua trinta por três.
Prova P2: 28/05  <--------------------------------------------------------------------------
'''
l_valores = [ ]                                # Lista inicialmente vazia
for i in range(0, 3):                        # repete 3 vezes
    # recebe um número do usuário e adiciona à lista
    num = int(input("Digite um número: "))
    l_valores.append(num)
# mostra todos os valores da lista em ordem inversa
print ('Valores da lista')
print (l_valores [ : : -1])                         
'''
Alterações:
a. Mostre os valores armazenados na lista na ordem inversa na vertical, use o for com range.
b. Mostre os valores armazenados na lista na ordem inversa na vertical, use o for com range.
    E suas respectivas posições.
c Também é possível acessar valores em uma lista do fim para o começo utilizando
    índices negativos. Refaça o loop que mostra os valores utilizando essa funcionalidade.
        DICAS:
for i in range(2, -1, -1):                         # a.
    print(l_valores [i])
for i in range(2, -1, -1):                         # b.
    print(i, " -> ", l_valores[i])
    #print("[", i, "] : ", l_valores[i])    
for i in range(-1, -4, -1):                         # c.
    print(i, " -> ", l_valores[i])
    print("[", i, "] : ", l_valores[i])

'''
