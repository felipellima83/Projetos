qtd = int(input("Quantidade de carro? "))
lista = []
for i in range(qtd):
    carro = input(f"Carro {i + 1}: ")
    lista.append(carro)

index = int(input("Index do carro que deseja excluir: "))
try:
    lista.pop(index)
except IndexError as err:
    print(f"\n\33[31mERRO {err.__class__.__name__}: Não possui nenhum carro nesse index.\33[m")
else:
    print("\nO índice foi excluído")
finally:
    print(f"Lista final : {lista}")