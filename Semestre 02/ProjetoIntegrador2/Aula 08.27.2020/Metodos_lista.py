lista = [ ]
t_lista = int(input("Quantidade: "))
for i in range(t_lista):
    n = int(input("Digite o número: "))
    lista.append(n)
print(lista)
print(len(lista))
print(sum(lista))
print(max(lista))
print(min(lista))
pesquisa = int(input("Qual: "))
if pesquisa in lista:
    posicao = lista.index(pesquisa)
    print(posicao)
else:
    print("Não tem")
#lista.sort()
lista.reverse()
print(lista)
print("Média: ",sum(lista)/len(lista))