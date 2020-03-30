#Curso: Ciência da Computação
#Professor: Antônio Barbosa Junior
#Disciplina: Lógica de programação
#Aluno: Felipe Ferreira Lima e Lima
#Matrícula: 22001310
#Data: 25/03/2020

#Exercício 01
i = 0 #Contador repetições
while i < 4:
    nota1 = float(input("Qual a primeira nota, do {}º aluno? ".format(i + 1))) #Recebe as notas
    nota2 = float(input("Qual a segunda nota, do {}º aluno? ".format(i + 1)))
    mediaAluno = (nota1+nota2)/2 #Calcula a média do aluno
    print("A média do {}º aluno foi {}.".format(i + 1, mediaAluno))
    if mediaAluno >= 5:
        print("O {}º aluno foi aprovado!".format(i + 1))
    else:
        print("O {}º aluno foi reprovado!".format(i + 1))
    i += 1
print("\nEncerrando o programa!")