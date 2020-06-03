import random

lista=[]
elementos = 4
for i in range(0,elementos):
    lista.append(random.randint(0,10))
print(lista)
pesquisa = int(input("Pesquisar qual número?"))
if pesquisa in lista:
    print("Encontrado")
    indice = lista.index(pesquisa)
    print("Posição: ", indice)
    qtd=lista.count(pesquisa)
    print("Quantidade: ", qtd)
else:
    print("Não encontrado")