'''
35. Construa o programa que leia “n” números reais quaisquer e calcule o produto
deles. O usuário fornecerá a quantidade de números, ou seja, o valor de “n”. O
usuário vai digitar também os “n” valores.
'''
import random

produto = 1
i = 0
qnt = int(input("Quantos números serão sorteados? "))
for x in range(1,qnt+1):
    x = random.randint(1,10)
    print(x, end=" ")
    produto*=x
    i+=1
print(f"\nO produto de todos os {i} números sorteados é: ", produto)
'''
Alterações

a. Altere o programa para multiplicar n valores aleatórios entre 1 e 10.

# adicionar a importação da biblioteca random
import random



'''

