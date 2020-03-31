'''
    7. Construa o programa que encontre o menor valor de um conjunto de valores
inteiros digitados pelo usuário. Use o valor zero na condição de saída que não será
considerado na pesquisa.
Teste 1: valor: 1, 2, 0   Resposta: Menor = 1
Teste 2: valor: 2, 1, 0   Resposta: Menor = 1
'''
#inicio do programa aqui abaixo:
i = 1
menor = 999999
while True:
    numero = int(input("Digite o {}º número ou digite 0 para encerrar: ".format(i)))
    i += 1
    if numero == 0:
        break
    elif numero < menor:
        menor = numero
if menor == 999999:
    print("Você não digitou nenhum número!")
else:
    print("O menor número digitado foi o", menor,".")
