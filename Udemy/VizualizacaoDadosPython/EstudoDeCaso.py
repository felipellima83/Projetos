# Importa a biblioteca Matplotlib
import matplotlib.pyplot as pyplot

# Entrada de dados
dados = open("original.csv").readlines() # O arquivo csv deve estar na pasta principal do projeto
x=[] 
y=[]
legendaEixoX="Ano"
legendaEixoY="População"
tituloGrafico="Gráfico de Crescimento da População Brasileira 1980-2016"

for i in range(len(dados)):
    if i!=0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

# Legendas
pyplot.title(tituloGrafico)
pyplot.xlabel(legendaEixoX)
pyplot.ylabel(legendaEixoY)

# Plota o gráfico de barras
pyplot.bar(x, y, color="#F08080", linestyle=":", linewidth=3) # Cor é hexadecimal
pyplot.plot(x, y, color="k") # Gráfico de dispersão
pyplot.legend()
pyplot.show()
#pyplot.savefig("figura.png", dpi=300)