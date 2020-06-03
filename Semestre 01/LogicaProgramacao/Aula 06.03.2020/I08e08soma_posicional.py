def mostra_lista(a):
    print("Lista na Vertical")
    for i in a:
        print(i)

if __name__ == "__main__":
    lista1 = [1,2,3,4,5]
    lista2 = [6,7,8,9,10]
    lista3 = []
    for i in range(0,5):
        lista3.append(lista1[i]+lista2[i])
    mostra_lista(lista3)