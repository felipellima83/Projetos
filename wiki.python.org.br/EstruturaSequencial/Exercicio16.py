#Felipe Lima
#Linguagem: Python
#Exercício 16 do site: https://wiki.python.org.br/EstruturaSequencial

#Entrada
altura = float(input("Qual a altura da área a ser pintada? "))
comprimento = float(input("Qual o comprimento da área a ser pintada? "))

#Processamento
area = altura * comprimento
litros = area/3
latas = 18/litros
precoTotal = latas*80

#Saída
print("Seão necessárias {:.0f} latas de tinta e o preço total será de R$ {:.2f}.".format(latas, precoTotal))