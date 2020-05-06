#Curso: Minicurso de Python Básico
#Data: 03/04/2020

#Exercício 04
primeiroTermo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Qual a razão da PA: "))
decimo = primeiroTermo+9*razao
for x in range(primeiroTermo, decimo+1, razao):
    print('{}'.format(x), end=', ')
print("Fim")