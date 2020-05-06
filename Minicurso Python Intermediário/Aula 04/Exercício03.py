listaPar = []
listaImpar = []
for i in range(6):
    numero = float(input("Digite o {}º número de 6: ".format(i+1)))
    if numero % 2 == 0:
        listaPar.append(numero)
    else:
        listaImpar.append(numero)
print(listaPar)
print(listaImpar)