#Felipe Lima
#Linguagem: Python
#Exercício 08 do site: https://wiki.python.org.br/EstruturaSequencial

#Entra com quanto ganha por hora
ganhoHora = float(input("Quanto você ganha por hora: "))

#Entra quantas horas foi trabalhada no mês
horaTrabalhada = float(input("Quantas horas você trabalhou no mês: "))

#Realiza os cálculos
salario = ganhoHora*horaTrabalhada

#Imprime o resultado
print("Você ganhou {:.2f} reais esses mês.".format(salario))