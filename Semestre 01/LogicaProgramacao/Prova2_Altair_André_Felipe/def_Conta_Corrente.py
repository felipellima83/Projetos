#3.1. Elabore um programa que simule uma conta corrente que solicite senha para acessar o programa e posteriormente de as opções de depositar, sacar, saldo e extrato.

from time import sleep

print("########################\n## PROGRAMA INICIADO! ##\n########################\n")

# Função que encerra o programa
def encerrar ():
    print("Encerrando o Programa!")
    ct=3
    for i in range(3):
        print(ct)
        sleep(1)
        ct-=1
    print("Programa Encerrado!")

# Função que mostra o saldo da conta
def saldo_conta ():
    saldo = 0
    for i in extrato:
        saldo += i
    print(f"\nSEU SALDO ATUAL É DE R$ {saldo} EM SUA CONTA.\n")

# Função que adiciona fundos à conta
def depositar ():
    deposito = float(input("\nQuanto você quer depositar? "))
    extrato.append(deposito)
    print(f"VOCÊ DEPOSITOU R$ {deposito}.")

# Função que retira fundos da conta
def sacar():
    saque = float(input("\nQuanto você quer sacar? "))
    extrato.append(saque*-1)
    print(f"VOCÊ SACOU R$ {saque}.")

# Função que imprime o extrato
def imprime_extrato ():
    print(f"EXTRATO DOS LANÇAMENTOS\n{extrato}")

# Função que solicita a senha e realiza as operações
def senha ():    
    senha = int(input("Digite a senha: "))
    ct=3 # Contador do limite de tentativas para inserir a senha correta
    
    # Condição de acerto da senha
    if senha == 123:        
        print("\n-------------------\n| Acesso Garantido! |\n-------------------\n")
        print("----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
        opcao = int(input("Qual opção deseja executar? "))
        
        # Loop eterno até chamar a função que encerra o programa
        while True :
            
            # Opção que encerra o programa
            if opcao == 0:
                encerrar()
                break
            
            # Opção que mostra o saldo da conta
            elif opcao == 1:
                saldo_conta()
                print("\n----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
                opcao = int(input("Qual opção deseja executar? "))
            
            # Opção que adiciona fundos à conta
            elif opcao == 2:
                depositar()                
                print("\n----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
                opcao = int(input("Qual opção deseja executar? "))
            
            # Opção que retira fundos da conta
            elif opcao == 3:
                sacar()
                print("\n----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
                opcao = int(input("Qual opção deseja executar? "))
            
            # Opção que imprime o extrato com os operações realizadas
            elif opcao == 4:
                imprime_extrato()
                print("\n----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
                opcao = int(input("Qual opção deseja executar? "))
            
            # Opção para digitar valor invalido
            else:
                print("\nNão existe essa opção!")
                print("\n----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
                opcao = int(input("Qual opção deseja executar? "))
    
    # Condição caso se erre a senha na primeira tentativa
    else:
        
        # Caso continue errando a senha após a primeira tentativa
        while senha != 123:
            print("Senha incorreta. Tente novamente!\n")  
            print(f"Você tem mais {ct-1} chance(s)!")
            senha = int(input("Digite a senha: "))
            ct-=1
            
            # Condição para encerrar o programa caso exceda as tentativas
            if ct == 1:
                break
        
        # Condição de acerto da senha
        if senha == 123:
            print("\n-------------------\n| Acesso Garantido! |\n-------------------\n")
        print("----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
        opcao = int(input("Qual opção deseja executar? "))
        
        # Loop eterno até chamar a função que encerra o programa
        while True :
            
            # Opção que encerra o programa
            if opcao == 0:
                encerrar()
                break
            
            # Opção que mostra o saldo da conta
            elif opcao == 1:
                saldo_conta()
                print("\n----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
                opcao = int(input("Qual opção deseja executar? "))
            
            # Opção que adiciona fundos à conta
            elif opcao == 2:
                depositar()                
                print("\n----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
                opcao = int(input("Qual opção deseja executar? "))
            
            # Opção que retira fundos da conta
            elif opcao == 3:
                sacar()
                print("\n----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
                opcao = int(input("Qual opção deseja executar? "))
            
            # Opção que imprime o extrato com os operações realizadas
            elif opcao == 4:
                imprime_extrato()
                print("\n----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
                opcao = int(input("Qual opção deseja executar? "))
            
            # Opção para digitar valor invalido
            else:
                print("\nNão existe essa opção!")
                print("\n----MENU PRINCIPAL----\n[0] Encerrar o programa\n[1] Saldo\n[2] Depositar\n[3] Sacar\n[4] Extrato\n")
                opcao = int(input("Qual opção deseja executar? "))   

# Verifica se o programa está sendo executado
if __name__ == "__main__":
    extrato = []
    senha()