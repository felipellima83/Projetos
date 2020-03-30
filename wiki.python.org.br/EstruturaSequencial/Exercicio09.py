#Felipe Lima
#Linguagem: Python
#Exercício 09 do site: https://wiki.python.org.br/EstruturaSequencial

#Entra com a temperatura em graus Farenheit
farenheit = float(input("Qual a temperatura em F°: "))

#Realiza os cálculos
celcius = 5*((farenheit-32)/9)

#imprime o resultado
print("A temperatura em C° é {:.2f}.".format(celcius))