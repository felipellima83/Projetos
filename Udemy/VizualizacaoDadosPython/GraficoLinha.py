# Importa a biblioteca Matplotlib
import matplotlib.pyplot as plt

# Entrada de dados
x = [1, 2, 5] 
y = [2, 3, 7]
tituloGrafico = "Gráfico de Linhas"

# Título do gráfico
plt.title(tituloGrafico)

# Legendas
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# Plota o gráfico de linhas
plt.plot(x, y)
plt.show()