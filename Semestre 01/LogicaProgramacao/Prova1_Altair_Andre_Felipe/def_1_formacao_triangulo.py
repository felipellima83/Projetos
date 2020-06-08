#Curso: Ciência da Computação
#Professor: Antônio Barbosa Junior
#Disciplina: Lógica de programação
#Alunos: Altair Correia Azevedo, André Luiz Vieira Mostaro e Felipe Ferreira Lima e Lima

# Função DEF 01
# FORMAÇÃO DE TRIANGULOS - este programa refaz a questão 01 (if,elif,else) com a intenção de mostrar o quão mais limpo e organizado fica um código escrito com funções DEF

def trianguloEquilatero(med1,med2,med3):
    P = med1 + med2 + med3
    h = med1 * ((3) ** (1 / 2)) / 2
    A = (med1 ** 2) * ((3) ** (1 / 2)) / 4
    print("\nDADOS DO TRI NGULO FORMADO\nTipo: EQUILÁTERO (3 ângulos internos iguais)\nL1 = L2 = L3: {} cm\n"
          "Perímetro(P): {} cm\nÁrea(A): {:.2f} cm²\nAltura(h): {:.2f} cm.".format(med1, P, A, h))
 
def trianguloIsosceles(med1,med2,med3):
    if (med1 == med2):
        P = med1 + med2 + med3
        h = ((med1 ** 2) - ((med3 / 2) ** 2)) ** (1 / 2)
        A = (med3 * h) / 2
        print("\nDADOS DO TRI NGULO FORMADO\nTipo: ISÓSCELES (2 ângulos internos e 2 lados iguais)\nL1 = L2 = {} cm"
              "\nL3 = {} cm\nPerímetro(P): {} cm\nAltura(h): {:.2f} cm\nÁrea(A): {:.2f} cm².".format(med1, med3, P, h, A))
    elif (med2 == med3):
        P = med1 + med2 + med3
        h = ((med2 ** 2) - ((med1 / 2) ** 2)) ** (1 / 2)
        A = (med1 * h) / 2
        print("\nDADOS DO TRI NGULO FORMADO\nTipo: ISÓSCELES (2 ângulos internos e 2 lados iguais)\nL2 = L3 = {} cm"
              "\nL1 = {} cm\nPerímetro(P): {} cm\nAltura(h): {:.2f} cm\nÁrea(A): {:.2f} cm².".format(med2, med1, P, h, A))
    elif (med1 == med3):
        P = med1 + med2 + med3
        h = ((med1 ** 2) - ((med2 / 2) ** 2)) ** (1 / 2)
        A = (med2 * h) / 2
        print("\nDADOS DO TRI NGULO FORMADO\nTipo: ISÓSCELES (2 ângulos internos e 2 lados iguais)\nL1 = L3 = {} cm"
              "\nL2 = {} cm\nPerímetro(P): {} cm\nAltura(h): {:.2f} cm\nÁrea(A): {:.2f} cm².".format(med1, med2, P, h, A))
 
def trianguloEscaleno(med1,med2,med3):
    P = med1 + med2 + med3
    print(
        "\nDADOS DO TRI NGULO FORMADO\nTipo: ESCALENO (3 ângulos internos e 3 lados diferentes)\nL1 = {} cm\nL2 = {} cm"
        "\nL3 = {} cm\nPerímetro(P): {} cm.".format(med1, med2, med3, P))
 
def naoTriangulo(med1,med2,med3):
    print('As medidas {} cm, {} cm e {} cm NÃO formam um triângulo.'.format(med1, med2, med3))
 
if __name__ == '__main__':
    med1 = int(input('Digite em cm a medida L1: '))
    med2 = int(input('Digite em cm a medida L2: '))
    med3 = int(input('Digite em cm a medida L3: '))
    if med1 < med2 + med3 and med2 < med1 + med3 and med3 < med1 + med2:
        if (med1 == med2 == med3):
            trianguloEquilatero(med1,med2,med3)
        elif (med1 == med2) or (med2 == med3) or (med1 == med3):
            trianguloIsosceles(med1,med2,med3)
        else:
            trianguloEscaleno(med1,med2,med3)
    else:
        naoTriangulo(med1,med2,med3)