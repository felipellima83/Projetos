#Curso: Ciência da Computação
#Professor: Antônio Barbosa Junior
#Disciplina: Lógica de programação
#Aluno: Felipe Ferreira Lima e Lima
#Matrícula: 22001310
#Data: 01/04/2020

#Exercício para Casa
numeroMaior = 0.01
numeroMenor = 2.99
limite = 3
somaH = 0
somaM = 0
somaAltura = 0
print("Para encerrar o programa digite na altura o valor zero (0)!")
while True:
    altura = float(input("Qual sua altura? "))
    if altura == 0:
        break
    genero = input("Qual seu gênero (H ou M)? ").upper()
    if genero == "H":
        somaH += 1
    elif genero == "M":
        somaM += 1
        somaAltura += altura
        media = somaAltura/somaM
    else:
        print("Você não digitou uma opção válida!")
    if altura >= numeroMaior:
        numeroMaior = altura
        limite = altura
    if altura <= numeroMenor:
        numeroMenor = altura    
percentagemH = (somaH/(somaH+somaM))*100
percentagemM = (somaM/(somaH+somaM))*100
if percentagemH > percentagemM:
    percentagemT = percentagemH - percentagemM
else:
    percentagemT = percentagemM - percentagemH
if limite == 3:
    print("Você não digitou nenhum dado válido!")
else:
    print("A maior altura do grupo é {}m e a menor é {}m. A média da altura das mulheres é {:.2f}m.\nE a diferença percentual entre o(s) homem(ns) e a(s) mulher(res) é de {:.2f}%.".format(numeroMaior, numeroMenor, media, percentagemT))