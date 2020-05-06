lista = []
expressao = str(input("Digite a expressão matemática: "))

ct1=0
ct2=0
j='('
k=')'
for j in expressao:
    ct1+=1
for k in expressao:
    ct2+=1
print(ct1,ct2)