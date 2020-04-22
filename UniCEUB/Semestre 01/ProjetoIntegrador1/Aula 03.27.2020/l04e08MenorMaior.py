"""
8. Construa um programa que encontre o menor valor e o maior valor de um conjunto (pelo menos 2) de valores inteiros digitados pelo usuário. A condição de saída será o valor zero que não será considerado na pesquisa.
Teste 1: valor: 1, 2, 0    Saída: menor: 1      Maior: 2
Teste 2: valor: 2, 1, 0    Saída: menor: 1      Maior: 2

 Alterações:
a. Mostre também a quantidade de valores digitados.
b. mostre também a soma de valores digitados.
        DICAS:
    ct = 0                                         # a.
    ct = ct + 1
print ('Quantidade: ', ct)            # a.
    soma = 0                                   # b.
    soma = soma + valor
print ('Soma: ', soma)                # b.
"""
#inicio do programa aqui abaixo:
i = 0
numeroMaior = 1
numeroMenor = 999999
limite = 1000000
soma = 0
while True:
    numero = int(input("Digite o {}º número (1 - 999.999) ou digite 0 para encerrar: ".format(i+1)))
    i += 1
    soma += numero
    if numero == 0:
        break
    if numero >= numeroMaior:
        numeroMaior = numero
        limite = numero
    if numero <= numeroMenor:
        numeroMenor = numero
if limite == 1000000:
    print("Você não digitou nenhum número entre 1 - 999.999 para compará-lós!")
else:
    print("Você digitou {} números.\nA soma dos valores digitados foi de {}.\nO menor número digitado foi o {} e o maior o {}.".format(i-1, soma, numeroMenor, numeroMaior))