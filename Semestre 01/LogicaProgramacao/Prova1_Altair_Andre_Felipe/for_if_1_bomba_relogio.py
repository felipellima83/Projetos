#Curso: Ciência da Computação
#Professor: Antônio Barbosa Junior
#Disciplina: Lógica de programação
#Alunos: Altair Correia Azevedo, André Luiz Vieira Mostaro e Felipe Ferreira Lima e Lima

# For com if dentr 01
# BOMBA RELÓGIO - este programa recebe um valor de tempo para explodir a bomba e se for maior que 2 segundo ela explode antes

import time
ct=0
t=int(input("Arme a bomba para lança-lá, mas cuidado que ela é velha!\nQual o tempo para a bomba explodir?"))
t2=t
for i in range(t):
    time.sleep(1)
    ct+=1
    if ct == ct:
        print(t2)
        t2-=1
    if ct == 3 and t > 3:
        print(" BOOM!!!! ")
        print("  _______")
        print(" /       \ ")
        print(" | o . o |")
        print(" |  xxx  |")
        print(" \_______/")
        print("\nA bomba apresentou defeito e ela explodiu.")
        break
if t <= 2:
    print("Lá vai bomba!")