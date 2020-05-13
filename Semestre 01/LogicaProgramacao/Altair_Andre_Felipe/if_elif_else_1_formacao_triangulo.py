#Curso: Ciência da Computação
#Professor: Antônio Barbosa Junior
#Disciplina: Lógica de programação
#Alunos: Altair Correia Azevedo, André Luiz Vieira Mostaro e Felipe Ferreira Lima e Lima

# If, elif e else 01
# FORMAÇÃO DE TRIÂNGULOS - este programa recebe as medidas dos 3 lados de um triângulo e retorna alguns dados sobre os mesmos

med1 = int(input('Digite em cm a medida L1: '))
med2 = int(input('Digite em cm a medida L2: '))
med3 = int(input('Digite em cm a medida L3: '))
if med1 < med2 + med3 and med2 < med1 + med3 and med3 < med1 + med2:
    print('As medidas {}cm, {}cm e {}cm formam um triângulo.'.format(med1, med2, med3))
    if (med1 == med2 == med3):
        P = med1 + med2 + med3
        h = med1 * ((3) ** (1 / 2)) / 2
        A = (med1 ** 2) * ((3) ** (1 / 2)) / 4
        print("\nDADOS DO TRI NGULO FORMADO\nTipo: EQUILÁTERO (3 ângulos internos iguais)\nL1 = L2 = L3: {} cm\n"
              "Perímetro(P): {} cm\nÁrea(A): {:.2f} cm²\nAltura(h): {:.2f} cm.".format(med1,P,A, h))
    elif (med1 == med2) or (med2 == med3) or (med1 == med3):
        if (med1 == med2):
            P = med1 + med2 + med3
            h = ((med1 ** 2)-((med3 / 2) ** 2)) ** (1 / 2)
            A = (med3 * h) / 2
            print("\nDADOS DO TRI NGULO FORMADO\nTipo: ISÓSCELES (2 ângulos internos e 2 lados iguais)\nL1 = L2 = {} cm"
                "\nL3 = {} cm\nPerímetro(P): {} cm\nAltura(h): {:.2f} cm\nÁrea(A): {:.2f} cm².".format(med1,med3, P, h, A))
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
    else:
        P = med1 + med2 + med3
        print("\nDADOS DO TRI NGULO FORMADO\nTipo: ESCALENO (3 ângulos internos e 3 lados diferentes)\nL1 = {} cm\nL2 = {} cm"
              "\nL3 = {} cm\nPerímetro(P): {} cm.".format(med1,med2, med3, P))
else:
    print('As medidas {} cm, {} cm e {} cm NÃO formam um triângulo.'.format(med1, med2, med3))