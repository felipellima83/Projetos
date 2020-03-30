#Felipe Lima
#Linguagem: Python
#Exercício 11 do site: https://wiki.python.org.br/EstruturaSequencial

#Importa biblioteca
import math

#Entra com o primeiro número inteiro
numero1 = int(input("Qual o primeiro número: "))

#Entra com o segundo número inteiro
numero2 = int(input("Qual o segundo número: "))

#Entra com um número real
real = float(input("Qual o número inteiro: "))

#Realiza os cálculos
#Produto do dobro do primeiro pela metade do segundo
produto = (numero1*2)*(numero2/2)

#Soma do triplo do primeiro com o terceiro
soma = (numero1*3)+real

#Terceiro elevado ao cubo
cubo = pow(real, 3)

#imprime os resultados
print("O produto do dobro do primeiro pela metade do segundo é {}.\nA soma do triplo do primeiro com o terceiro é {}."
      "\nE o Terceiro elevado ao cubo é {:.2f}.".format(produto, soma, cubo))