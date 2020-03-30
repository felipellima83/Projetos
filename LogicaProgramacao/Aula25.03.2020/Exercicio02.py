#Professor: Antônio Barbosa Junior
#Disciplina: Lógica de programação
#Aluno: Felipe Ferreira Lima e Lima
#Matrícula: 22001310
#Data: 25/03/2020

#Exercício 02
i = 0 #Contador repetições
aprovados = 0 #Contador de alunos aprovados
reprovados = 0 #Contador de alunos reprovados
while i < 4: #Repetção do laço até o contador i atingir o valor 4
    nota1 = float(input("Qual a primeira nota, do {}º aluno? ".format(i + 1))) #Recebe a 1ª notas
    nota2 = float(input("Qual a segunda nota, do {}º aluno? ".format(i + 1))) #Recebe a 2ª notas
    mediaAluno = (nota1+nota2)/2 #Calcula a média do aluno
    print("A média do {}º aluno foi {}.".format(i + 1, mediaAluno)) #Imprime a média do aluno
    if mediaAluno >= 4: #Condição para aprovação
        print("O {}º aluno foi aprovado!".format(i + 1))
        aprovados += 1
    else:
        print("O {}º aluno foi reprovado!".format(i + 1))
        reprovados += 1
    i += 1
print("Foram {} alunos aprovados e {} alunos reprovados!\nEncerrando o programa!".format(aprovados, reprovados))