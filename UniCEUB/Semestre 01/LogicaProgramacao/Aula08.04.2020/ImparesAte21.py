#Professor: Antônio Barbosa Junior
#Disciplina: Lógica de programação
#Aluno: Felipe Ferreira Lima e Lima
#Matrícula: 22001310
#Data: 08/04/2020

#Exercício 05
soma = 0
i = 0
for x in range(3,22):
    if x % 3 == 0:
        print(x)
        soma+=x
        i+=1
print("Soma:", soma)
print("Média: ", soma/i)