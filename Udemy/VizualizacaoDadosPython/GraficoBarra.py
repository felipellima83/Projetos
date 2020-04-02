# Importa a biblioteca Matplotlib
import matplotlib.pyplot as plt

# Entrada de dados
x1 = [1, 3, 5, 7, 9] 
y1 = [2, 3, 4, 5, 6]
x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]
tituloGrafico = "Gráfico de Barras"
eixoX = "Eixo X"
eixoY = "Eixo Y"

# Legendas
plt.title(tituloGrafico)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

# Plota o gráfico de barras
plt.bar(x1, y1, label = "Grupo 1")
plt.bar(x2, y2, label = "Grupo 2")
plt.legend()
plt.show()