lista = []
for i in range(0,10):
    if i %2 == 0:
        lista.append(1)
    else:
        lista.append(0)
ct=0
for i in lista:
    print(ct, "-", i)
    ct+=1