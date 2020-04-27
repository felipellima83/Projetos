'''
40
No relógio do programa anterior, vamos permitir que o usuário forneça a hora atual
(horas, minutos e segundos) para o relógio começar a funcionar.
'''
import time
l=0
hora = int(input("Quantas horas? "))
minuto = int(input("Quantos minutos? "))
segundo = int(input("Quantos segundos? "))
while True:
    for k in range(hora, 13):
        for i in range(minuto, 60):
            for j in range(segundo, 60):
                if l % 2 == 0:
                    print(f"{k}h {i}min {j}seg AM")
                    time.sleep(1)
                if l % 2 != 0:
                    print(f"{k}h {i}min {j}seg PM")
                    time.sleep(1)
    l+=1