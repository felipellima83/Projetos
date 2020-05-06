#Exemplo 01
# Função range()
print("Exemplo 01")
for item in range(10):
    print(item)

# Exemplo 02
# Função range()
# Parâmetro start
print("\nExemplo 02")
for x in range(2, 6):
    print(x)

# Exemplo 03
# Função range()
# Parâmetro start 2
print("\nExemplo 03")
for x in range(2, 30, 3):
    print(x)

# Exemplo 04
# Exemplo 03
# Função range()
# Parâmetro start 2
# Decrescente
print("\nExemplo 04")
for i in range(9, -1, -1):
    print(i)

# Exemplo 05
# Loop aninhado
print("\nExemplo 05")
for x in range(3):
    for y in range(3):
        print(x, y)

# Exemplo 06
# Loop aninhado 2
print("\nExemplo 06")
for x in range(1,11):
    for y in range(1,11):
        print(x, "x", y, "=", x*y)

# Exemplo 07
# For em string
print("\nExemplo 07")
frase = "eu gosto de cachaça"
for letra in frase:
    print(letra)

#Exemplo 08
# Função len()
print("\nExemplo 08")
palavra = "monitoria"
print(len(palavra))