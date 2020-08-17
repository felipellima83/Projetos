lista_signos = ['macaco','galo','cão','porco','rato','boi','tigre','coelho','dragão','serpente','cavalo','carneiro']
lista_aniv = [1983,1984]

def mostra_signo ():
    for i in lista_aniv:
        if i % 12 == 0:
            print(lista_signos[0])
        elif i % 12 == 1:
            print(lista_signos[1])
        elif i % 12 == 2:
            print(lista_signos[2])
        elif i % 12 == 3:
            print(lista_signos[3])
        elif i % 12 == 4:
            print(lista_signos[4])
        elif i % 12 == 5:
            print(lista_signos[5])
        elif i % 12 == 6:
            print(lista_signos[6])
        elif i % 12 == 7:
            print(lista_signos[7])
        elif i % 12 == 8:
            print(lista_signos[8])
        elif i % 12 == 9:
            print(lista_signos[9])
        elif i % 12 == 10:
            print(lista_signos[10])
        elif i % 12 == 11:
            print(lista_signos[11])
        elif i % 12 == 12:
            print(lista_signos[12])
        else:
            print('erro')

mostra_signo()