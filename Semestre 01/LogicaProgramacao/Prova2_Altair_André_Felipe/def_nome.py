#3.1. Elabore o enunciado e a resolução de um programa em Python usando o programa principal (função main) e pelo menos seis funções (def) e as estruturas if ... elif ... else, while e for.

from time import sleep

saldo = 0

def senha (senha):
    senha = int(input("Digite a senha: "))
    ct=1
    if senha == 123:
        print("Acesso Garantido!\n")
    while senha != 123:
        print("Senha incorreta. Tente novamente!")
        print(f"Você tem {5-ct} chance(s)!")
        senha = int(input("Digite a senha: "))
        ct+=1
        if ct == 5:
            print("Limite de tentativas excedido!")
            break
        print("Acesso Garantido!\n")

def encerrar ():
    print("Encerrando o Programa!")
    ct=3
    for i in range(3):
        print(ct)
        sleep(1)                
        ct-=1
    print("Programa Encerrado!")

def menu ():
    print("---MENU PRINCIPAL---\n[0] Encerrar o programa\n[1] Depositar\n[2] Sacar\n[3] Saldo\n[4] Extrato")
    opcao = int(input("Qual opção deseja executar? "))
    while (opcao != 0 and opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4):
        print("\nOpção inválida!\n")
        print("---MENU PRINCIPAL---\n[0] Encerrar o programa\n[1] Depositar\n[2] Sacar\n[3] Saldo\n[4] Extrato")
        opcao = int(input("Qual opção deseja executar? "))
    return opcao

def saldo_conta ():
    return saldo

if __name__ == "__main__":
    print("Programa Iniciado!")
    senha (senha)
    retorno_menu = menu ()
    while retorno_menu :
        if retorno_menu == 0:
            encerrar()
            break
        elif retorno_menu == 1:
            print(f"Seu saldo atual é de {saldo_conta()} em sua conta.")
            continue
        elif retorno_menu == 2:
            pass
        elif retorno_menu == 3:
            pass
        elif retorno_menu == 4:
            pass
        else:
            print("Não existe essa opção!")