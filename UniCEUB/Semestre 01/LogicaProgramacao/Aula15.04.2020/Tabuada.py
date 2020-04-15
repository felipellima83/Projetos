tabuada = int(input("Tabuada do número: "))
while tabuada != 0:
    for i in range(1,11):
        print("{} + {} = {}".format(tabuada, i, tabuada+i))
        i+=1
    tabuada = int(input("Tabuada do número: "))
print("FIM")