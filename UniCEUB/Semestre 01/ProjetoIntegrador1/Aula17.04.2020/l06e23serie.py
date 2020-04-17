'''
23. Desenvolva o programa que calcule o valor de S, em que:

S = 1/1 + 2/4 + 3/9 + 4/16 + ... + 10/100
'''
'''
Alterações

a. Modifique o programa para que o usuário possa escolher um valor arbitrário
de início e fim do cálculo da série

# incluir no início do programa
inicio = int(input("Digite o valor do início do cálculo da série: "))
fim = int(input("Digite o valor do fim do cálculo da série: "))

# modificar o for para acomodar os novos valores
for i in range(inicio, fim + 1):


b. Modifique o programa para calcular a mesma série, mas com valores
alternados em positivos e negativos:

S = 1/1 - 2/4 + 3/9 - 4/16 + ...

# incluir uma variável de controle do sinal
sinal = 1

# modificar a soma dentro do for para incluir uma multiplicação pelo sinal
# e alterar o valor do sinal para a soma seguinte
soma += sinal * (i / i ** 2)
sinal *= -1
'''
inicio = int(input("Qual o valor inicial do numerador? "))
final = int(input("Qual o valor final do numerador? "))
soma=0
sinal=1
for i in range(inicio,final+1):
    soma+= sinal* (i/i**2)
    sinal *= -1
print("A soma é igual a {:.2f}.".format(soma))