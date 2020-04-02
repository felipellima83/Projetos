# Importa a biblioteca Matplotlib
import matplotlib.pyplot as plt

# Entrada de dados
x = [1, 3, 5, 7, 9] 
y = [2, 3, 7, 1, 0]
eixoX = "Eixo X"
eixoY = "Eixo Y"
tituloGrafico = "Gráfico de Dispersão"

# Legendas
plt.title(tituloGrafico)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

# Plota o gráfico de linhas
plt.scatter(x, y, label = "Meus pontos", color = "red", marker="*", s=100)
plt.plot(x, y, color="k", linestyle=":")
plt.legend()
plt.show()