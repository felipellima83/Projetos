#Felipe Lima
#Linguagem: Python
#Exercício 06 do site: https://wiki.python.org.br/EstruturaSequencial

#Importa biblioteca
import math

#Entra com o raio
raio = float(input("Qual o raio do círculo: "))

#Calcula a área
area = math.pi*raio

#Imprime o resultado
print("A área do círculo, para o raio digitado, é: {:.2f}.".format(area))