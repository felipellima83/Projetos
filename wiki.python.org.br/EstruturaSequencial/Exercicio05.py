#Felipe Lima
#Linguagem: Python
#Exercício 05 do site: https://wiki.python.org.br/EstruturaSequencial

#Entra com o comprimento em metros
metros = float(input("Qual a medida em metros que deve ser convertido em centímetros: "))

#Faz a conversão
centimetros = metros*100

#Imprime o resultado
print("A conversão da medida digitada é {:.0f} cm.".format(centimetros))