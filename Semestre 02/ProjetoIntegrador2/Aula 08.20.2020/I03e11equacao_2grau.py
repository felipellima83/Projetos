import math

a = float(input("Digite o valor de a: "))
if a == 0:
    print("Não pode dividir por zero!")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = pow(b,2) - 4*a*c
    if delta < 0:
        print("Não existe raízes reais!")
    elif delta == 0:
        print("Existem duas raízes iguais")
        x = (-b + math.sqrt(delta))/(2*a)
        print("x = {:.4f}".format(x))
    else:
        print("Existem duas raízes diferentes")
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("x' = {:.4f} e x'' = {:.4f}".format(x1, x2))