try:
    n1 = int(input("Numerador: "))
    n2 = int(input("Denominador: "))

    r = n1 / n2
except ValueError as erro:
    print(f"{erro.__class__.__name__}, informe um valor inteiro!")
except ZeroDivisionError:
    print("Informe um denominador diferente de 0")
except (IndexError, FileNotFoundError):
    print("")
else:
    print(f"Resultado = {r}")