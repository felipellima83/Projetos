# Importa a biblioteca Matplotlib
import matplotlib.pyplot as pyplot

# Entrada de dados
x=[1, 3, 5, 7, 9] 
y=[2, 3, 7, 1, 0]
z=[20, 5, 100, 33, 10]
eixoX="Eixo X"
eixoY="Eixo Y"
tituloGrafico="Gráfico de Dispersão"

# Legendas
pyplot.title(tituloGrafico)
pyplot.xlabel(eixoX)
pyplot.ylabel(eixoY)

# Plota o gráfico de linhas e dispersão
pyplot.plot(x, y, color="#F08080", linestyle=":", linewidth=3) # Cor é hexadecimal
pyplot.scatter(x, y, label="Meus pontos", color="k", marker="*", s=z)
pyplot.legend()
pyplot.show()
pyplot.savefig("figura.png", dpi=300) # Salva na pasta principal

"""
A seguir, alguns exemplos de argumentos que podem ser aplicados ao método plot( ).

color: cor (ver exemplos abaixo)
label: rótulo
linestyle: estilo de linha (ver exemplos abaixo)
linewidth: largura da linha
marker: marcador (ver exemplos abaixo)

CORES (color)
'b' blue
'g' green
'r' red
'c' cyan
'm' magenta
'y' yellow
'k' black
'w' white

Marcadores (marker)
'.' point marker
',' pixel marker
'o' circle marker
'v' triangle_down marker
'^' triangle_up marker
'<' triangle_left marker
'>' triangle_right marker
'1' tri_down marker
'2' tri_up marker
'3' tri_left marker
'4' tri_right marker
's' square marker
'p' pentagon marker
'*' star marker
'h' hexagon1 marker
'H' hexagon2 marker
'+' plus marker
'x' x marker
'D' diamond marker
'd' thin_diamond marker
'|' vline marker
'_' hline marker

Tipos de linha (linestyle)
'-' solid line style
'--' dashed line style
'-.' dash-dot line style
':' dotted line style
"""