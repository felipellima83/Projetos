'''
38
Construa o programa que simule o cronômetro digital com minutos e segundos. Comece de 0:0.
dica: Utilize um for encadeado
'''
import time

for i in range(60):
    for j in range(60):
        print(f"{i} min {j} seg")
        time.sleep(1)