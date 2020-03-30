#Professor: Antônio Barbosa Junior
#Disciplina: Lógica de programação
#Aluno: Felipe Ferreira Lima e Lima
#Matrícula: 22001310
#Data: 25/03/2020

#Exercício 04
i = 0
soma = 0
nota = 0
print("Para terminar a inserção de notas, digite o valor da nota como -1!")
while nota != -1:
    nota = float(input("Qual a do {}º aluno? ".format(i + 1)))
    if nota == -1:
        break
    i += 1
    soma += nota
if i != 0:
    media = soma/i
    print("A média da turma de {} alunos foi {:.2f}.".format(i, media))
else:
    print("Não existe divisão por zero!")