import random

lista=[]
elementos = 30
for i in range(0,elementos):
    lista.append(random.uniform(0,100)) # uniform números reais
    # lista.append(random.randint(0,100))
    # lista.append(random.randrange(0,100,2)) #Pares
    # lista.append(random.randrange(1,100,2)) #Ímpares
print(lista)
maior = lista[0]
for i in lista:
    if i > maior:
        maior = i
print(f"O maior é {max(lista)}.")
print(f"O menor é {min(lista)}.")
print(f"A soma é {sum(lista)}.")
print(f"A média é {sum(lista)/elementos}.")