'''    6. Complemente o programa anterior, acrescente o cálculo da média aritmética
dos números ímpares.
Obs.: Salve o programa anterior como outro nome para alterá-lo.
Teste 1:   numero: 1, 2 e 0.    Resposta: Média pares: 2
                                                                    Média ímpares: 1
Teste 2:   numero: 1, 5 e 0.    Resposta: Não tem número par
                                                                     Média ímpares: 3
Teste 3:   numero: 2, 4 e 0.    Resposta:  Média pares: 3
                                                                    Não tem número ímpar
Teste 4: numero: 0                  Resposta: Não tem número par
                                                                    Não tem número ímpar
'''              
#inicio do programa aqui abaixo:


'''   Alrerações:
a. Mostre também a quantidade de números pares.
b. Mostre também  a quantidade de números ímpares.

'''
somaPar = 0
somaImpar = 0
ctPar = 0
ctImpar = 0
numero = 1
i = 1
print ("Digite zero (0) para terminar a inserção de números!!!")
while (True):
    numero = int(input("Digite o {}º número: ".format(i)))
    i += 1
    if numero == 0:
        break
    resto = numero % 2
    if resto == 0:
        somaPar = somaPar + numero
        ctPar = ctPar + 1
        mediaPar = somaPar / ctPar
    else:
        somaImpar = somaImpar + numero
        ctImpar = ctImpar + 1
        mediaImpar = somaImpar / ctImpar
if ctPar != 0 and ctImpar != 0:
    print("A media de {} números pares recebidos é {:.2f} e a média de {} números ímpares é {:.2f}."
          .format(ctPar,mediaPar, ctImpar, mediaImpar))
if ctPar != 0 and ctImpar == 0:
    print("A media de {} números pares recebidos é {:.2f} e você não digitou nenhum número ímpar."
          .format(ctPar, mediaPar))
if ctPar == 0 and ctImpar != 0:
    print("A media de {} números ímpares recebidos é {:.2f} e você não digitou nenhum números par."
          .format(ctImpar, mediaImpar))
if ctImpar == 0 and ctPar == 0:
    print("Você não digitou nenhum número!")