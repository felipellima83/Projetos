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
somaPar = 0                                                # Soma dos números pares
somaImpar = 0
ctPar = 0
ctImpar = 0                                             # Contador de números pares
valor = 1
i = 1
print ('Digite zero (0) para sair')
while (True):                                       # while True:
    valor = int(input("Digite o {}º número: ".format(i)))
    i += 1# recebe um número inteiro
    if valor == 0:                                      # valor igual (==) 0 é a condição de saída
        break                                           # O break força a saída da estrutura de repetição (while)
    resto = valor % 2
    if resto == 0:                                      # Se o valor recebido é par
        somaPar = somaPar + valor                             # soma += valor  # incrementa a soma de valores recebidos
        ctPar = ctPar + 1                                     # ct+= 1                # incrementa o registro de notas recebidas
        mediaPar = somaPar / ctPar
    else:
        somaImpar = somaImpar + valor
        ctImpar = ctImpar + 1
        mediaImpar = somaImpar / ctImpar                            # calcula a média
if ctPar != 0 and ctImpar != 0:                                                        # Fim da estrutura de repetição "while"
    print("A media de {} números pares recebidos é {:.2f} e a média de {} números ímpares é {:.2f}."
          .format(ctPar,mediaPar, ctImpar, mediaImpar)) # mostra o resultado
if ctPar != 0 and ctImpar == 0:
    print("A media de {} números pares recebidos é {:.2f} e você não digitou nenhum número ímpar."
          .format(ctPar, mediaPar))  # mostra o resultado
if ctPar == 0 and ctImpar != 0:
    print("A media de {} números ímpares recebidos é {:.2f} e você não digitou nenhum números par."
          .format(ctImpar, mediaImpar))  # mostra o resultado
if ctImpar == 0 and ctPar == 0:
    print("Você não digitou nenhum número!")