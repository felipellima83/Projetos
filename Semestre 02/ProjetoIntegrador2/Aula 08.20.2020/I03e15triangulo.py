a = float(input("Digite o tamanho do 1º lado:"))
b = float(input("Digite o tamanho do 2º lado:"))
c = float(input("Digite o tamanho do 3º lado:"))
if a >= b+c or b >= a+c or c >= a+b:
    print("Essas mediadas não formam um triângulo!")
elif a == b and b == c:
    print("Equilátero")
elif a!= b and b != c and c != a:
    print("Escaleno")
else:
    print("Isósceles")