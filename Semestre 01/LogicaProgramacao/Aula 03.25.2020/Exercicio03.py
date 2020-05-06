#Professor: Antônio Barbosa Junior
#Disciplina: Lógica de programação
#Aluno: Felipe Ferreira Lima e Lima
#Matrícula: 22001310
#Data: 25/03/2020

#Exercício 03
i = 0 #Contador repetições
media = 0 #Contador da média da turma
while i < 4: #Repetção do laço até o contador i atingir o valor 4
    nota = float(input("Qual a nota do {}º aluno? ".format(i + 1))) #Recebe a nota
    media += nota #Incrementa a nota na média
    i += 1 #Incrementa 1 ao contador de repetições
print("A média da turma foi {:.2f}.".format(media/i))