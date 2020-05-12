import random
import time

life = 100
while life > 0:
    ato1 = int(input("Digite 1 para lançar o dado e tentar entrar em luta corporal e roubar a arma de Dryden ou 2 para lançar o dado e tentar usar a inteligência de um espião: "))
    if ato1 == 1:
        x = random.randint(1, 10)
        print(f"\nDado foi lançado, resultado = {x}.\n")      
        if x >3:
            life = life - 40
            print(f"Você tomou um dano! Sua vida atual é {life}.\n")
        else:
            print("STATUS 007 CONFIRMADO!!!")
    else:
        x = random.randint(1,10)
        print(f"\nO dado foi lançado, resultado = {x}.\n")
        if x > 6:
            life = life - 40
            print("STATUS 007 CONFIRMADO!!!")
        else:
            print("STATUS 007 CONFIRMADO!!!")
    ato2 = int(input("Digite 1 para explodir uma bomba e fugir ou 2 para se proteger dos tiros e fugir: "))
    if ato2 == 1:
        ct=0
        while True:
            senha = int(input(f"Qual a senha (0-9), restam {3-ct} tentativas: "))
            ct+=1
            if ct > 2:
                life = life - 40
                print(f"Você tomou um dano! Sua vida atual é {life}.\n")
                break
            if senha == 123:
                print("Bomba armada!")
                for i in range(3, 0, -1):
                    for j in range(2, 0, -1):
                        for k in range(1, 0, -1):
                            print(i,j,k)
                            time.sleep(1)
                break
    else:
        ct=0
        while True:
            senha = int(input(f"Qual a senha, restam {3-ct} tentativas: "))
            ct+=1
            if ct > 2:
                life = life - 40
                print(f"Você tomou um dano! Sua vida atual é {life}.\n")
                break
            if senha == 123:
                print("Cadeado aberto!")
                for i in range(3, 0, -1):
                    for j in range(2, 0, -1):
                        for k in range(1, 0, -1):
                            print(i,j,k)
                            time.sleep(1)
                break
    ato3 = int(input("Digite 1 para assassinar Le Chiffre ou 2 para pedir ajuda a CIA: "))
    if ato3 == 1:
        sorteado = random.randint(1, 51)
        tentativa = 0
        chute = 0
        while chute != sorteado:
            chute = int(input ('Escolha um cofre para abri-lo (1-50): '))
            tentativa+=1
            if chute == sorteado:
                print ('Bond encontra o cofre e pega o veneno.')
            elif tentativa == 6:
                life = life - 40
                print(f"Você tomou um dano! Sua vida atual é {life}.\n")
                if life > 0:                                    
                    print('Meu nome é Bond, James Bond!')
                else:
                    print("James Bond está morto!!!")
                break
            elif chute > sorteado:
                print ('Seu chute está mais alto que o valor sorteado! Chute um valor mais baixo.')
            else:
                print ('Seu chute está mais baixo que o valor sorteado! Chute um valor mais alto.')
    else:
        sorteado = random.randint(1, 51)
        tentativa = 0
        chute = 0
        while chute != sorteado:
            chute = int(input ('Escolha um número para adivinhar: '))
            tentativa+=1
            if chute == sorteado:
                print ('De volta ao jogo!')
            elif tentativa == 6:
                print('Le Chiffre e seus associados tentam matar Bond envenenando sua bebida!')
                life = life - 10
                break
            elif chute > sorteado:
                print ('Seu chute está mais alto que o valor sorteado! Chute um valor mais baixo.')
            else:
                print ('Seu chute está mais baixo que o valor sorteado! Chute um valor mais alto.') 
    break
print("------------FIM-------------")