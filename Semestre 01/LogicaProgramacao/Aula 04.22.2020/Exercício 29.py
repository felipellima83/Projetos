# Exercício 29
# Letras A, B e C
print("Números Octais")
ct=0
for i in range(8):
    for j in range(8):
       print(f"{i}{j}", end=", ")
       ct+=1
print(f"Foram reptidas {ct} vezes.")
#Letra D
print("Decimal - Octal")
for i in range(64):
    print(f"{i} - {oct(i)[2:]}")