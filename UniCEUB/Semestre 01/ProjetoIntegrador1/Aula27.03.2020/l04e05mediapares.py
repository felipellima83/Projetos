'''    5. Construa o programa que calcule a média aritmética dos números pares. O usuário
fornecerá os valores de entrada que pode ser um número qualquer par ou ímpar.
A condição de saída será o número zero.
Teste 1:    valor: 1, 2 e 0.    Resposta: Média 2
Teste 2:    valor: 1, 3 e 0.    Resposta: Não pode ser dividido por zero (0)
'''
soma = 0                                                # Soma dos números pares
ct = 0                                                  # Contador de números pares
valor = 1
print ('Digite zero (0) para sair')
while valor != -1:                                       # while True:
    valor = int(input("Digite um número:"))             # recebe um número inteiro
    if valor == 0:                                      # valor igual (==) 0 é a condição de saída    
        break                                           # O break força a saída da estrutura de repetição (while)
    resto = valor % 2
    if resto == 0:                                      # Se o valor recebido é par
        soma = soma + valor                             # soma += valor  # incrementa a soma de valores recebidos
        ct = ct + 1                                     # ct+= 1                # incrementa o registro de notas recebidas
if ct != 0:                                                        # Fim da estrutura de repetição "while"
    media = soma / ct                                       # calcula a média
    print("A media de {} números pares recebidos é {:.4f}.".format(ct,media)) # mostra o resultado
else:
    print("Você não digitou nenhum número par!")
'''   Alterações:
a. Digite o zero (0) na primeira leitura. Corrija este erro.
b. Mostre a média com quatro casas decimais.
c. Mostre também a quantidade de números pares e a soma dos pares.
        DICAS:
if ct != 0:                                                      # a.
    media = soma / ct                
    print ('Média = ', media)
else;
    print ('Não posso dividir por zero')        # a.

'''
