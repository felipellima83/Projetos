#Curso: Ciência da Computação
#Aluno: Felipe Ferreira Lima e Lima
#Matrícula: 22001310
#Data: 06/04/2020

#Prova
#Exercício 01
"""
Crie um algoritmo que compare uma senha contra uma já salva no algoritmo, se a senha estiver correta mostre a mensagem, "seja bem vindo", se estiver errada deve permitir outra tentativa de até no máximo de 3 erros, com 3 erros a seguinte mensagem deve ser mostrada. "Terminal bloqueado".
"""
#Início do código
i=0
for x in range(1, 4):
    senha = int(input("Digite a senha: "))
    if senha == 123:
        i+=1
        print("Seja bem vindo!")
        break
    if senha != 123:
        i+=1
        print("Senha incorreta!")
    if i == 3:
        print("Terminal bloqueado!")

#Exercício 02
"""
2) Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro que o usuário quiser, a tabuada deve ser de 1 até 10.
"""
#Início do código
tabuada = int(input("Tabuada do número: "))
i = 0
while i <=10:
    print(tabuada, "x", i, "=", tabuada*i)
    i+=1

#Exercício 03
"""
3) Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
números que são múltiplos de 17.
"""
#Início do código
i = 0
c = 1
for x in range(1, 11):
    numero = int(input("Digite o {}º número para saber se ele é múltiplo de 17: ".format(c)))
    c+=1
    if numero % 17 == 0:
        i+=1
print("Dos 10 número digitados, {} são divisível por 17.".format(i))