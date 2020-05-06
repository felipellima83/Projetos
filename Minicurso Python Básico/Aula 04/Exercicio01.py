#Curso: Minicurso de Python Básico
#Data: 02/04/2020

#Exercício 01
caixas = int(input("Quantas caixas serão colocadas no caminhão? "))
somaCaixa = 0
for i in range(caixas):
    peso = float(input("Peso da {} caixa: ".format(i + 1)))
    somaCaixa += peso
if somaCaixa <= 500:
    print("Peso dentro do limite, pode prosseguir!")
else:
    print("Peso ultrapassado, não prossiga!")