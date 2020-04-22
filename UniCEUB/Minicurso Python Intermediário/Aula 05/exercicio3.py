try:
    arquivo = open('teste.txt')
except FileNotFoundError as erro:
    print(f"\33[31m ERRO {erro.__class__.__name__} - O arquivo {erro.filename} não foi encontrado.\33[m")
else:
    print(arquivo.read())
finally:
    print("Fim da verificação!")