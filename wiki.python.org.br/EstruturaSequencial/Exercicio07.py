#Felipe Lima
#Linguagem: Python
#Exercício 07 do site: https://wiki.python.org.br/EstruturaSequencial

#Entra com a altura do quadrado
altura = float(input("Qual a altura do quadrado: "))

#Entra com a base do quadrado:
base = float(input("Qual a largura do quadrado: "))

#Realiza os cálculos
area = base*altura
dobro = area*2

#Imprime os resultados
print("A área do quadrado é {:.2f}.".format(area))
print("O dobro da área é {:.2f}.".format(dobro))