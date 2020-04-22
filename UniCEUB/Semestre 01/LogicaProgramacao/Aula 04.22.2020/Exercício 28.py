# Exercício 28
# Letras A, B, C e D
print("Números binários de 0 a 7")
for x in range(2):
    for y in range(2):
        for z in range(2):
            decimal = x*4+y*2+z*1
            print(f"{decimal} - {x}{y}{z}")
#Letra E
print("Decimal - Binário")
for i in range(8):
    print(f"{i} - {bin(i)[2:]}")