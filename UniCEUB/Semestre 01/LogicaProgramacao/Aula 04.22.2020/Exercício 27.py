# Exercício 27
# Letras A, B e C
print("Dado 1 - Dado 2")
ct=0
for x in range(1, 7):
    for y in range(1,7):   
        if x+y == 7:
            print(x, "-", y, end ="; ")                 
            ct+=1     
print("Possibilidades de combinação: ",ct)
#Letra D
print("Dado 1 - Dado 2")
ct=0
for x in range(1, 7):
    for y in range(1,7):   
        if x+y < 5:
            print(x, "-", y, end ="; ")                 
            ct+=1     
print("Possibilidades de combinação: ",ct)