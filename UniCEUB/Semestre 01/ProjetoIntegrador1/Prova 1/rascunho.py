import time
#Tentativa de explodir bomba
print("James Bond prepara uma bomba para joga-lá, para isso ele precisa acertar a senha!")
print("-"*142)       

ct=0
while True:            
    senha = int(input(f"Qual a senha, restam {3-ct} tentativas: "))
    ct+=1
    if ct > 2:
        print("RESULTADO DO LANÇAMENTO DO DADO:\nVocê não conseguiu armar a bomba e teve que sair rasteijando entre os objetos que estavam por ali, mesmo assim estilhaços dos tiros te acertaram na fuga.")
        print("-"*142)
        #life = life - 10
        print(f"Você tomou um dano! Sua vida atual é 10.\n")
        print("-"*142)
        break
    if senha == 123:
        print("Acesso garantido!")
        for i in range(3, 0, -1):
            for j in range(2, 0, -1):
                for k in range(1, 0, -1):
                    print(i,j,k)
                    time.sleep(1)
        print("RESULTADO DO LANÇAMENTO DO DADO:\nBOOOMM!!!\nVocê conseguiu armar a bomba e a lançou na direção dos seguranças, matando todos eles!")
        break