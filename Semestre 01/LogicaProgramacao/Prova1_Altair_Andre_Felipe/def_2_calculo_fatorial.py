#Curso: Ciência da Computação
#Professor: Antônio Barbosa Junior
#Disciplina: Lógica de programação
#Alunos: Altair Correia Azevedo, André Luiz Vieira Mostaro e Felipe Ferreira Lima e Lima

# Função DEF 02
# CÁLCULO DE FATORIAL - função para fatorial de um número mostrando a cadeia de multiplicação (Ex.: 5 x 4 x 3... = 120)

def fatorial(n, show=False):
    fat = 1
    for c in range(n, 0, -1): #uso de For dentro da função fatorial()
        if show:
            print(c, end=' ')
        if c > 1:
            print(' x ', end=' ')
        else:
            print(' = ', end=' ')
        fat *= c
    return fat