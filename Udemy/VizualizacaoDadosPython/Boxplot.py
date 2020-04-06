# Importa a biblioteca Matplotlib
import matplotlib.pyplot as plt
import random

# Entrada de dados
vetor = []
for i in range(100):
    numeroAleatorio = random.randint(0, 10000)
    vetor.append(numeroAleatorio)
plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()