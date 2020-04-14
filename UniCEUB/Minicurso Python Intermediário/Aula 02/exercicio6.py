def calcular(num):
    num+=1
    for a in range(1,num):
        b = str(a)+' '
        print(b*a)
valor = int(input('Insirar um valor: '))
calcular(valor)