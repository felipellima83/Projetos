#Professor: Antônio Barbosa Junior
#Disciplina: Lógica de programação
#Aluno: Felipe Ferreira Lima e Lima
#Matrícula: 22001310
#Data: 08/04/2020

#Exercício 10
soma = 0
i = 0
alunos = int(input("Quantos alunos tem na turma? "))
for x in range(1, alunos+1):
    soma+=float(input("Qual a nota do {}º aluno? ".format(i+1)))
    i+=1
print("Média da turma: ", soma/i)