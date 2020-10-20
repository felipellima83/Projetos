'''   UniCEUB   -   Ciência da Computação   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha '''
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
''' - Na função create, colocar um menu com três opções: 
[f] - Acrescentar vários nomes sempre no final da lista.
[p] - Acrescentar vários nomes em posições específicas da lista.
[s] - Sair.
Incluir a mensagem de erro: "Opção inválida"        
Deve funcionar com letra minúscula ou maiúscula       ----- '''
# def create():
#     nome = input('Nome: ')
#     lista.append(nome)
def create():
    print('[f] - Final')
    print('[p] - Posição')
    print('[s] - Sair')
    opcao = input('Opção: ').lower()      # .upper()
    if opcao == 'f':
        nome = input('Nome ou <enter> para sair: ')
        while nome != '':
            lista.append(nome)
            nome = input('Nome ou <enter> para sair: ')
    elif opcao == 'p':
        i = int(input("Posição ou [-1] pra sair: "))
        while i != -1:
            nome = input('Nome: ')
            lista.insert(i, nome)           # lista.insert(indice, valor)
            i = int(input("Posição ou [-1] pra sair: "))
    elif opcao == 's':
        pass                                 # Passa por esta linha e não faz nada.
    else:
        print("Opção inválida")
def read():
    # if lista != []:  # if len(lista) != 0:    # if len(lista):    # if lista: (Vefifica se lista não está vazia)
    if lista_nao_vazia():                   # Chama a função lista_nao_vazia
        # print(lista)                      # Na horizontal
        # for v in lista:                     # Na vertical, sem índice
        #     print(v)
        # ct = 0                              # Na vertical, com índice e ct
        # for v in lista:
        #     print(ct, ' – ', v)
        #     ct += 1
        # qtd = len(lista)                    # Na vertical, com índice e com len e range
        # for i in range(qtd):
        #     print(i, '-', lista[i])
        for indice, v in enumerate(lista):  # Na vertical com índice e sem ct
            print(indice, ' - ', v)
    # else:
    #     print('Lista vazia.')
'''  - Na função update, colocar um menu com três opções: 
[p] - Atualizar usando uma posição específica da lista e o novo nome. 
[n] - Atualizar usando o nome na lista e o novo nome. 
[s] - Sair
Incluir mensagem de erro: "Opção inválida"        
Deve funcionar com letra minúscula ou maiúscula     
Obs.: para evitar erro, faça crítica antes de atualizar.        '''
def update():
    # if lista != []:  # if len(lista) != 0:    # if len(lista):    # if lista: (Vefifica se lista não está vazia)
    if lista_nao_vazia():                        # Chama a função lista_nao_vazia
        read()                                   # Chama a função read
        print('[p] - Posição')
        print('[n] - Nome')
        print('[s] - Sair')
        opcao = input('Opção: ').lower()         # .upper()
        if opcao == 'p':
            try:                                 # Tenta executar
                p = int(input("Qual posição: "))
                novo_nome = input("Novo nome: ")
                lista[p] = novo_nome             # Solução 1, notação de vetor
                # lista.pop(p)                   # Solução 2
                # lista.insert(p, novo_nome)     # Solução 2
            except IndexError as e:              # Se erro de índice
                print("Erro IndexError: ", e)
            except Exception as e:
                print("Erro Exception: ", e)
        elif opcao == 'n':
            nome_lista = input('Nome da lista: ')
            if nome_lista in lista:                 # operador in, nome_lista pertence a lista
                i = lista.index(nome_lista)         # Pega o índice do item (nome_lista) na lista
                novo_nome = input('Nome novo: ')
                lista[i] = novo_nome
            else:
                print(f'O {nome_lista} não está na lista')
        elif opcao == 's':
            pass
        else:
            print('Opção inválida')
    # else:
    #     print('Lista vazia.')
''' - Na função delete, colocar um menu com três opções:
[n] - Apagar usando o nome na lista. 
[p] - Apagar usando uma posição específica da lista. 
[s] - Sair
Incluir mensagem de erro: "Opção inválida"        
Deve funcionar com letra minúscula ou maiúscula     
Obs.: para evitar erro, faça crítica antes de apagar.        '''
def delete():
    # if lista != []:  # if len(lista) != 0:    # if len(lista):    # if lista: (Vefifica se lista não está vazia)
    if lista_nao_vazia():                       # Chama a função lista_nao_vazia
        read()                                  # Chama a função read
        # print('[n] - Nome')                   # Substituir os três prints por um único print numa linha
        # print('[p] - Posição')
        # print('[s] - Sair')
        print('[p] - Posição\n[n] - Nome\n[s] - Sair')
        opcao = input('Opção: ').lower()        # Converte em letra minúscula.
        if opcao == 'n':
            nome = input("Qual nome: ")
            if nome in lista:
                lista.remove(nome)
            else:
                print(f'O {nome} não está na lista.')
        elif opcao == 'p':
            posicao = int(input("Qual posição: "))
            tam = len(lista)
            if posicao < tam:               # Verifica se posição existe
                del lista[posicao]          # Solução 1
                # lista.pop(p)                # Solução 2
            else:
                print(f'Posição {posicao} não existe na lista.')
        elif opcao == 's':
            pass
        else:
            print('Opção inválida')
#    else:
#        print('Lista vazia.')
def lista_nao_vazia():                                     # Solução 1
    if lista != []:    # if len(lista) != 0:    # if len(lista):    # if lista: (Vefifica se lista não está vazia)
        nao_vazia = True
    else:
        nao_vazia = False
        print('Lista vazia.')
    return nao_vazia
# def lista_nao_vazia():                                     # Solução 2
#     situacao = bool (lista)
#     if not situacao:
#         print('Lista vazia.')
#     return situacao
if __name__ == '__main__':
    lista = []
    while True:
        r = menu()
        if r == 'c':
            create()
        elif r == 'r':
            read()
        elif r == 'u':
            update()
        elif r == 'd':
            delete()
        else:
            break