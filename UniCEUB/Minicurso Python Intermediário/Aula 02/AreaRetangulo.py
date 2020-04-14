def areaRetangulo(base, altura):
    areaRetangulo = base * altura
    return areaRetangulo
b = float(input("Qual o valor da base? "))
a = float(input("Qual o valor da altura? "))
print("A área do retângulo é {}.".format(areaRetangulo(b,a)))