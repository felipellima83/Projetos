qntAluno = int(input("Quantos alunos tem na sala: "))
i = 0
acumulador = 0
while i != qntAluno:
    nota = float(input("Qual a nota do {}º aluno: ".format(i+1)))
    i = i + 1
    acumulador += nota
media = acumulador/qntAluno
print("A média da turma é {}.".format(media))