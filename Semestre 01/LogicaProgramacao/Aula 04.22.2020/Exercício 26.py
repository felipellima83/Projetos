# Exercício 26
# Letras A, B, C e D
print("Dado 1 - Dado 2")
ct=0
for x in range(1, 7):
    for y in range(1,7):
        print(x, "-", y, end ="; ")
        ct+=1        
    print("\n")
print("Possibilidades de combinação: ",ct)