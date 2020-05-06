#Professor: Antônio Barbosa Junior
#Disciplina: Lógica de programação
#Aluno: Felipe Ferreira Lima e Lima
#Matrícula: 22001310
#Data: 08/04/2020

#Exercício 08 e 09
soma = 0
i = 0
inicio = int(input("Qual o valor inicial? "))
final = int(input("Qual o valor final? "))
passo = int(input("Qual o valor do passo? "))
if inicio < final:
    for x in range(inicio, final+1, passo):
        print(x, end=" ")
        soma+=x
        i+=1
elif inicio > final:
    for x in range(inicio, final-1, passo):
        print(x, end=" ")
        soma+=x
        i+=1
else:
    print("Os valores digitados são iguais!")
print("\nSoma:", soma)
print("Números: ", i)
print("Média: ", soma/i)