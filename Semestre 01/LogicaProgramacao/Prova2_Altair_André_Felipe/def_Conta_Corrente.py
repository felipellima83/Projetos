#3.1. Elabore um programa que simule uma conta corrente que solicite senha para acessar o programa e posteriormente de as opções de depositar, sacar, saldo e extrato.

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
    saldo = 0
    for i in extrato:
        saldo += i
    print(f"\nSEU SALDO ATUAL É DE R$ {saldo} EM SUA CONTA.\n")

def depositar ():
    deposito = float(input("\nQuanto você quer depositar? "))
    extrato.append(deposito)
    print(f"VOCÊ DEPOSITOU R$ {deposito}.")

def sacar():
    saque = float(input("\nQuanto você quer sacar? "))
    extrato.append(saque*-1)
    print(f"VOCÊ SACOU R$ {saque}.")

def imprime_extrato ():
    print(f"EXTRATO DOS LANÇAMENTOS\n{extrato}")

def senha ():    
    senha = int(input("Digite a senha: "))
    ct=3 # Contador do limite de tentativas para inserir a senha correta
    
    if senha == 123:        
        print("\n-------------------\n| Acesso Garantido! |\n-------------------\n")
        print("----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
        opcao = int(input("Qual opção deseja executar? "))
        
        while True :
            
            if opcao == 0:
                encerrar()
                break
            
            elif opcao == 1:
                saldo_conta()
                print("\n----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
                opcao = int(input("Qual opção deseja executar? "))
            
            elif opcao == 2:
                depositar()                
                print("\n----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
                opcao = int(input("Qual opção deseja executar? "))
            
            elif opcao == 3:
                sacar()
                print("\n----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
                opcao = int(input("Qual opção deseja executar? "))
            
            elif opcao == 4:
                imprime_extrato()
                print("\n----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
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
            print("\n-------------------\n| Acesso Garantido! |\n-------------------\n")
            print("----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
            opcao = int(input("Qual opção deseja executar? "))
            
            while True :
            
                if opcao == 0:
                    encerrar()
                    break
                
                elif opcao == 1:
                    saldo_conta()
                    print("\n----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
                    opcao = int(input("Qual opção deseja executar? "))
                
                elif opcao == 2:
                    depositar()                
                    print("\n----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
                    opcao = int(input("Qual opção deseja executar? "))
                
                elif opcao == 3:
                    sacar()
                    print("\n----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
                    opcao = int(input("Qual opção deseja executar? "))
                
                elif opcao == 4:
                    imprime_extrato()
                    print("\n----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
                    opcao = int(input("Qual opção deseja executar? "))
                
                else:
                    print("Não existe essa opção!")   

if __name__ == "__main__":
    extrato = []
    senha()