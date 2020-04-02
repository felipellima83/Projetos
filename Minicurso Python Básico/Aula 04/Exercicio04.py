#Curso: Minicurso de Python Básico
#Data: 02/04/2020

#Exercício 04
i = 0
frase = input("Digite uma frase: ").lower()
for separaLetrasDaFrase in range(len(frase)):
    if frase[separaLetrasDaFrase] == "a":
        print("A frase digitada possui a letras 'A' na {}ª posição.".format(separaLetrasDaFrase+1))