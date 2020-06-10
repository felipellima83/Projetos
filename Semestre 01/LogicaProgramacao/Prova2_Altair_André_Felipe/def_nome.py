#3.1. Elabore o enunciado e a resolução de um programa em Python usando o programa principal (função main) e pelo menos seis funções (def) e as estruturas if ... elif ... else, while e for.

from time import sleep

print("########################\n## PROGRAMA INICIADO! ##\n########################\n")

def encerrar ():
    print("Encerrando o Programa!")
    ct=3
    for i in range(3):
        print(ct)
        sleep(1)
        ct-=1
    print("Programa Encerrado!")

def saldo_conta ():
    return saldo

def depositar (deposito):
    saldo += deposito
    print(f"Você depositou R$ {deposito}.")

def sacar():
    pass

def imprime_extrato ():
    print(extrato)

def senha ():    
    senha = int(input("Digite a senha: "))
    ct=3 # Contador do limite de tentativas para inserir a senha correta
    if senha == 123:        
        print("Acesso Garantido!\n")
        print("----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
        opcao = int(input("Qual opção deseja executar? "))
        while True :
            if opcao == 0:
                encerrar()
                break
            elif opcao == 1:
                print(f"\nSEU SALDO ATUAL É DE R$ {saldo_conta()} EM SUA CONTA.\n")
                print("----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
                opcao = int(input("Qual opção deseja executar? "))
            elif opcao == 2:
                deposito = float(input("Quanto você quer depositar? "))
                extrato.append(deposito)
                depositar(deposito)
                print("----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
            elif opcao == 3:
                saque = float(input("Quanto você quer sacar? "))
                extrato.append(saque*-1)

                print("----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
                opcao = int(input("Qual opção deseja executar? "))
            elif opcao == 4:
                imprime_extrato()
                print("----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
                opcao = int(input("Qual opção deseja executar? "))
            else:
                print("Não existe essa opção!")
    else:
        while senha != 123:
            print("Senha incorreta. Tente novamente!\n")  
            print(f"Você tem mais {ct-1} chance(s)!")
            senha = int(input("Digite a senha: "))
            ct-=1
            if ct == 1:
                break
        if senha == 123:
            print("Acesso Garantido!\n")
            print("---MENU PRINCIPAL---\n[0] Encerrar o programa\n[1] Depositar\n[2] Sacar\n[3] Saldo\n[4] Extrato\n")
            opcao = int(input("Qual opção deseja executar? "))
            while True :
                if opcao == 0:
                    encerrar()
                    break
                elif opcao == 1:
                    print(f"Seu saldo atual é de R$ {saldo_conta()} em sua conta.\n")
                    print("----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Depositar\n[2] Sacar\n[3] Saldo\n[4] Extrato\n")
                    opcao = int(input("Qual opção deseja executar? "))
                elif opcao == 2:
                    pass
                elif opcao == 3:
                    pass
                elif opcao == 4:
                    pass
                else:
                    print("Não existe essa opção!")
        else:
            print("\nLimite de tentativas excedido!\n")
            encerrar()     
    

if __name__ == "__main__":
    saldo = 0
    extrato = []
    senha()