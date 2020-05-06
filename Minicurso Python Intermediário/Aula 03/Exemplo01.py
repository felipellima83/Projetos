def funcaoImprimir(parametroImpresso):
    print('-'*30)
    print(parametroImpresso)
    print('-'*30)

# Chama a função e insere o parâmetro na função
# O parâmetro pode ser solicitado
funcaoImprimir(input("Digite o que deseja ser impresso: "))
# O parâmetro pode ser inserido
funcaoImprimir(2+2)