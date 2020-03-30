#Felipe Lima
#Linguagem: Python
#Exercício 12do site: https://wiki.python.org.br/EstruturaSequencial

#Entrada do peso pescado
pesoPescado = float(input("Quantos quilos foram pescados? "))

#Realiza os cálculos
excesso = pesoPescado - 50
multa = excesso * 4

#Imprime o resultado
print("O valor da multa a ser paga é de R$ {:.2f}.".format(multa))