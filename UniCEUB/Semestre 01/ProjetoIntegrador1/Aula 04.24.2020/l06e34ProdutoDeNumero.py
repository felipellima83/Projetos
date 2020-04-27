'''
34
Construa o programa que leia dez números reais quaisquer e calcule o produto deles.
'''
produto = 1
i = 0
qnt = int(input("Quantos números serão digitados? "))
for x in range(1,qnt+1):
    produto*=float(input("Qual o {}º número? ".format(i+1)))
    i+=1
print(f"O produto de todos os {i} digitados é Média da turma: ", produto)
   

    
'''
A letrra a é o enunciado do exercício 35.
a - deixe o usuário informar a quantidade de números
R:
  

'''
