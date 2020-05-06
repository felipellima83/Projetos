'''
37. A série de Fibonacci é formada pela seguinte sequência: 1, 1, 2, 3, 5, 8, 13,
21, 34, 55, 89, 144, ... etc. A fórmu-la de recorrência para essa série é
n i = n i-1 + n i-2 para i ≥ 2 pois n 0 = n 1 = 1. Escreva o programa que gere a
série de Fibonacci até o vigésimo termo.
'''
p1 = 0
p2 = 1
print("1º termo da sequência: ", p2)
for i in range(19):
    p3 = p1 + p2
    print(f"{i+2}º termo da swquência: ", p3)
    p1 = p2
    p2 = p3



'''
Alterações


'''
