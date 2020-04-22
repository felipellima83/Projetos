for i in range(16):
    if i == 10:
        i = "A"
    elif i == 11:
        i = "B"
    elif i == 12:
        i = "C"
    elif i == 13:
        i = "D"
    elif i == 14:
        i = "E"
    elif i == 15:
        i = "F"
    print(i)

#Letra A
lista = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
for i in lista:
    print(i)

#Letra B
print("Decimal - Octal")
for i in range(16):
    print(f"{i} - {hex(i)[2:].upper()}")