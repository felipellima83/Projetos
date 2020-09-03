

def menu():
    l_opcoes = ['c','r','u','d','e']
    print("[c] - create")
    print("[r] - read")
    print("[u] - update")
    print("[d] - delete")
    print("[e] - exit")
    opcao = input('Opção: ')
    while True:
        opcao = input('Opção: ').lower()
        if opcao in l_opcoes:
            break            
        else:
            print("Opção inválida, tente novamente.")
    return opcao

def create():
    n = input("Nome: ")
    lista.append(n)
    
def read():
    if lista != []:
        ct = 0
        for i in lista:
            print(ct, '-',i)
            ct+=1
    else:
        print("Lista vazia.")           
        
def update():
    if lista != []:
        read()
        p = int(input("Qual posição: "))
        novo_nome = input("Novo nome: ")
        try:
            lista[p] = novo_nome
        except IndexError as e:
            print("Erro IndexError: ",e)
        except Exception as e:
            print("Erro Exception: ",e)
    else:
        print("lista vazia.")


def delete():
    v = input("Qual nnome: ")
    lista.remove(v)

if __name__ == "__main__":
    lista = []
    while True:
        op = menu()
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