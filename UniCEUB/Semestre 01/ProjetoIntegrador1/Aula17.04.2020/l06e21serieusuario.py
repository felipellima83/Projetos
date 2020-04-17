'''
21. Deixe o problema anterior flexível, permita que o usuário forneça a
quantidade de termos da série. Sendo H = 1/1 + 1/2 + 1/3 + ... + 1/n

Alterações

a. Modifique o programa para que o usuário entre com o numerador da série

# adicionar essa linha no início
numerador_serie = int(input("Digite o numerador da série: "))

# modificar essa linha dentro do for
soma += numerador_serie / i
'''
numerador = int(input("Qual o valor numerador?"))
denominador = int(input("Qual o valor denominador?"))
soma=0
for i in range(1, denominador+1):
    soma+= numerador/i
print("A soma é igual a {:.2f}.".format(soma))