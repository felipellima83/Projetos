
print("Olá ")

try:
    numerador = int(input('Numerador:'))
    denominador = int(input('Denominador:'))

    resultado = numerador / denominador

except Exception as erro:
    print(f"Deu ruim, aconteceu o erro:  {erro.__class__.__name__}")
else:
    print(f"Resultado: {resultado}")
finally:
    print("final!")
