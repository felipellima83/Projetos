#Felipe Lima
#Linguagem: Python
#Exercício 13 do site: https://wiki.python.org.br/EstruturaSequencial

#Entra com a altura
altura = float(input("Qual sua altura? "))

#Realiza os cálculos
pesoIdealHomem = (72.7*altura)-58
pesoIdealMulher = (62.1*altura)-44.7

#Imprime o resultado
print("Seu peso ideal caso você seja homem é {:.2f} e se for mulher {:.2f}". format(pesoIdealHomem,pesoIdealMulher))