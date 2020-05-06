def tabuada(numero):
    #i = 1
    #while i <=10:
    for i in range(1,11):
        print(numero, "x", i, "=", numero*i, end='')
        print('\t',numero, "+", i, "=", numero+i, end='')
        print('\t',numero, "-", i, "=", numero-i, end='')
        print('\t',numero, "/", i, "=", numero/i)
        i+=1
num = int(input("Tabuada do número: "))
tabuada(num)