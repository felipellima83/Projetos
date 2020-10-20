'''   UniCEUB   -   Ciência da Computação   -   Prof. Barbosa
Atalho de teclado: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha'''
# def menu():                               # Original
#     print('[c] - create')
#     print('[r] - read')
#     print('[u] - update')
#     print('[d] - delete')
#     print('[e] - exit')
#     opcao = input('Opção: ')
#     return opcao
'''- Na função menu, inclua a msg: "Opção inválida, tente novamente." 
E só sai da função menu se o usuário digitar uma das opções válidas.
Ela deve aceitar letra maiúscula ou minúscula.
Dicas: use while e um if dentro do while com msg erro                               '''
def menu():
    l_opcoes = ['c', 'r', 'u', 'd', 'e']
    print('[c] - Create')
    print('[r] - Read')
    print('[u] - Update')
    print('[d] - Delete')
    print('[e] - Exit')
    # print("[c] - Create\n[r] - Read\n[u] - Update\n[d] - Delete\n[e] - Exit")
    while True:
        opcao = input('Opção: ').lower()      # .upper()
        if opcao in l_opcoes:                 # in, contido em             # Solução 1
            break
        else:
            print('Opção inválida, tente novamente.')
        # if opcao not in l_opcoes:           # [not] in, contido em       # Solução 2
        #     print('Opção inválida, tente novamente.')
        # else:
        #     break
    # Fim do while
    return opcao
def create():                                     # Original
    n = input('Nome: ')
    lista.append(n)
''' - Na função read, se a lista estiver vazia, mostre a msg: "Lista vazia."
Mostre todos os itens da lista na vertical.
Mostre todos os itens da lista na vertical com o íncice.   '''
# def read():
#     print(lista)                              # Na horizontal
def read():
    if lista != []:    # if len(lista) != 0:    # if len(lista):    # if lista: (Vefifica se lista não está vazia)
        # print(lista)                            # Na horizontal
        # for v in lista:                         # Na vertical, sem índice
        #    print(v)
        # ct = 0                                  # Na vertical, com índice e ct
        # for v in lista:
        #     print(ct, ' – ', v)
        #     ct += 1
        # qtd = len(lista)                        # Na vertical, com índice e com len e range
        # for i in range(qtd):
        #     print(i, '-', lista[i])
        for indice, v in enumerate(lista):      # Na vertical com índice e sem ct
            print(indice, ' - ', v)
    else:
        print('Lista vazia.')
'''- Na função update, se lista vazia, mostre msg "Lista vaiza."
Senão mostre os itens da lista.
Se posição não existe, msg erro. Use try ... except ...          '''
# def update():                             # original
    # p = int(input("Qual posição: "))
    # novo_nome = input("Novo nome: ")
    # lista[p] = novo_nome                  # Solução 1, notação vetor.
    # lista.pop(p)                          # Solução 2
    # lista.insert(p, novo_nome)            # Solução 2
# def update():                             # Algoritmo do update atualizado
#   Verificar se lista não está vazia (if)
#         mostre todos os itens
#         lê os dados necessários pra atualizar
#         try:
#             atualiza
#         except IndexError as e:
#             msg erro 1
#   Lista vazia (else:)
#         msg erro 2
def update():
    if lista != []:    # if len(lista) != 0:    # if len(lista):    # if lista: (Vefifica se lista não está vazia)
        read()
        try:                                    # Tentando
            p = int(input("Qual posição: "))
            novo_nome = input("Novo nome: ")
            lista[p] = novo_nome                # Solução 1, notação vetor
            # lista.pop(p)                      # Solução 2
            # lista.insert(p, novo_nome)        # Solução 2
        except IndexError as e:                 # IndexError: list assignment index out of range
            print("Error IndexError: ", e)
        except Exception as e:
            print("Error Exception: ", e)
    else:
        print('Lista vazia.')
'''- Na função delete, se lista vazia, mostre msg "Lista vaiza."
Senão mostre os itens da lista.
Verifique se valor (nome) está na lista. Se valor não existe, msg erro     
Nesta solução, não use try ... except                        --- '''
# def delete():                                           # Original
#     v = input("Qual nome: ")
#     lista.remove(v)
# def delete():                                           # Algoritmo do delete atualizado
#     Verificar se lista não está vazia
#         mostre a lista
#         lê o dado necessário
#         verificar se o item (nome) está na lista
#             remova
#         Se não estiver
#             msg erro 1
#     Se lista vazia
#         masg erro 2
def delete():
    if lista_nao_vazia():
    # if lista != []:    # if len(lista) != 0:    # if len(lista):    # if lista: (Vefifica se lista não está vazia)
        read()
        nome = input("Qual nome: ")
        if nome in lista:             # operador in, se item está na lista
            lista.remove(nome)
        else:
            print(f'O {nome} não está na lista.')
    # else:                                             # Atualizado com a def lista_nao_vazia
    #     print('Lista vazia.')
''' Com o objetivo de eliminar o código repetido nas defs read, update e delete crie esta função:
- Crie a função lista_nao_vazia, ela não recebe nada e retorna o valor
lógico True ou False. Se a lista estiver vazia, mostra a msg "Lista vazia"
e retorna False. Ele vai ser chamada pelas funções read, update, delete.
Atualize essas três funções para funcionar com a função lista_não_vazia. '''
# def lista_nao_vazia():                                  # Solução 1, algoritmo da função
    # Verificar se lista não vazia
    #       atualiza variável
    # Se lista vazia
    #       atualiza variavel
    #       msg: lista vazia
    # retorne variavel
def lista_nao_vazia():                                     # Solução 1
    if lista != []:    # if len(lista) != 0:    # if len(lista):    # if lista: (Vefifica se lista não está vazia)
        nao_vazia = True
    else:
        nao_vazia = False
        print('Lista vazia.')
    return nao_vazia
# def lista_nao_vazia():                                     # Solução 2
#     situacao = bool (lista)   # A variável situação recebe True (lista não vazia) ou False (lista vazia)
#     if not situacao:
#         print('Lista vazia.')
#     return situacao
if __name__ == '__main__':          # mai <tab>
    lista = []                      # Lista vazia
    while True:
        op = menu()                 # A variável op recebe o valor que a funão menu retorna
        if op == 'c':
            create()
        elif op == 'r':
            read()
        elif op == 'u':
            update()
        elif op == 'd':
            delete()
        else:
            break