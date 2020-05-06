'''
39. Transforme o programa anterior num relógio acrescentando as horas. Gere uma
pausa para simular o tempo real e mostre o seguinte leiaute: xxhxxminxxseg

Exemplo: 23h46min57seg
'''

# importa a biblioteca de funções de tempo
import time
l=0
while True:
    for k in range(13):
        for i in range(60):
            for j in range(60):
                if l % 2 == 0:
                    print(f"{k}h {i}min {j}seg AM")
                    time.sleep(1)
                if l % 2 != 0:
                    print(f"{k}h {i}min {j}seg PM")
                    time.sleep(1)
    l+=1
            


'''
Alterações

a. Altere o programa para mostrar o horário no padrão americano: 0-12 horas am/pm

# importa a biblioteca de funções de tempo
import time

time.sleep(segundos)
'''
