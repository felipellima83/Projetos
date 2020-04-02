#Felipe Lima
#Linguagem: Python
#Exercício 15 do site: https://wiki.python.org.br/EstruturaSequencial

#Entrada
ganhoHora = float(input("Quanto você ganha por hora? "))
horasTrabalhadas = float(input("Quantas hora você trabalhou? "))

#Processamento
salarioBruto = (ganhoHora * horasTrabalhadas)
ir = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - ir - inss -sindicato

#Saída
print("Seu salário bruto esse mês foi de R$ {:.2f}.\nVocÊ pagou R$ {:.2f} de IR.\nVocê pagou R$ {:.2f} de INSS."
      "\nVocÊ pagou R$ {:.2f} ao Sindicato.\nSeu salário líquido após os descontos foi de R$ {:.2f}."
      "".format(salarioBruto,ir,inss,sindicato,salarioLiquido))