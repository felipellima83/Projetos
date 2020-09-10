# Exercício de CRUD

def menu():    
    while True:
        print("[c] - Create")
        print("[r] - Read")
        print("[u] - Update")
        print("[d] - Delete")
        print("[e] - Exit")
        op = input('Opção: ').lower()
        if op == 'c':
            create()
        elif op == 'r':
            read()
        elif op == 'u':
            update()
        elif op == 'd':
            delete()
        elif op == 'e':
            break
        else:
            print("Opção inválida, tente novamente!")

def create():
    op_create = ['p','f','s']
    while True:
        print("[p] - Incluir um ou mais nomes ao final da lista.")
        print("[f] - Incluir um ou mais nomes em posições específicas da lista.")
        print("[s] - Sair.")
        op_create = input("Qual opção: ").lower()
        if op_create == 'p':
            n = input(" Digite o nome: ")
            lista.append(n)            
        elif op_create == 'f':
            n = input(" Digite o nome: ")
            try:
                p = int(input("Qual posição na lista: "))
                lista.insert(p,n)
            except IndexError as e:
                print("Erro IndexError: ",e)
            except Exception as e:
                print("Erro Exception: ",e)
        elif op_create == 's':
            break
        else:
            print("Opção inválida, tente novamente.")    
    
def read():
    if lista_nao_vazia():
        ct = 0
        for i in lista:
            print(ct, '-',i)
            ct+=1        
        
def update():
    while True:
        if lista_nao_vazia():
            read()
            print("[p] - Deseja atualizar pela posição na lista: ")
            print("[n] - Deseja atualizar pelo nome na lista: ")
            print("[s] - Sair")
            op_update = input("Qual opção: ").lower()
            if op_update == 'p':
                try:
                    p = int(input("Qual posição: "))
                    novo_nome = input("Novo nome: ")
                    lista[p] = novo_nome
                except IndexError as e:
                    print("Erro IndexError: ",e)
                except Exception as e:
                    print("Erro Exception: ",e)
            elif op_update == 'n':
                nome_lista = input("nome da lista: ")
                if nome_lista in lista:
                    i = lista.index(nome_lista)
                    novo_nome = input("Novo nome: ")        
                    lista[i] = novo_nome
            elif op_update == 's':
                break
            else:
                print("Opção inválida, tente novamente.")

def delete():
    if lista_nao_vazia():
        read()
        v = input("Qual nome deseja remover? ")
        if v in lista:
            lista.remove(v)            
        else:
            print("Esse nome {} não existe na lista!".format(v))

def lista_nao_vazia():
    if lista != []:
        nao_vazia = True
    else:
        nao_vazia = False
        print("Lista vazia.")
    return nao_vazia

if __name__ == "__main__":
    lista = []
    menu()