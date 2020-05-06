#Curso: Ciência da Computação
#Professor: Ivandro da Silva Ribeiro
#Disciplina: Projeto Integrador 1
#Aluno: Felipe Ferreira Lima e Lima
#Matrícula: 22001310
#Data: 07/05/2020

#Prova 01
#CASINO ROYALE

#O projeto consiste em criar um jogo que simula o filme 007 - Casino Royale.

#Importar as bibliotecas
import random
import time

print("-"*142)
print("007 - CASINO ROYALE")
print("-"*142)
#Total de vida para o jogo
life = 100
while life > 0:
    #Descrição do início do ato 1
    print("James Bond está em uma missão que, se for completada com sucesso, vai o qualificar para ser um agente 00. Ele vai para Praga, para matar um chefe de seção do MI6, Dryden, que vazou uma informação confidencial. Depois de conversarem, no escritório do Dryden, e James relatar o que veio fazer ali, Dryden saca uma arma de uma gaveta e se prepara para disparar. No mesmo momento em que James Bond vai cumprir sua missão, em outro lugar, um homem chamado apenas de Sr. White servia como intermediário apresentando o banqueiro Le Chiffre a um grupo terrorista que procura um paraíso fiscal para guardar seu dinheiro.\n")
    print("-"*142)

    #Ato1 é a variável que escolhe a opção do que James Bond irá fazer
    ato1 = int(input("O QUE JAMES BOND VAI FAZER AGORA? Você consegue terminar o filme vivo?\nDigite 1 para lançar o dado e tentar entrar em luta corporal e roubar a arma de Dryden ou 2 para lançar o dado e tentar usar a inteligência de um espião: "))
    #Tentar luta corporal
    if ato1 == 1:
        #x é a variável randômica que sorteia um número entre 10
        x = random.randint(1, 10)
        print(f"\nDado foi lançado, resultado = {x}.\n")      
        #Tentativa de luta corporal
        #Chance de sucesso de 20%
        #Falha na tentativa se o resultado do dado for maior que 3
        if x >3:

            print("RESULTADO DO LANÇAMENTO DO DADO:\nJames Bond calcula que a distância até Dryden é de 2 metros, logo em seguida ele pula em direção ao bandido, porém ele escorrega no tapete e perde o impulso, com isso Dyden dispara sua arma e acerta o braço esquerdo do James Bond. No entanto James Bond consegue alcançar Dryden, tira a arma da mão dele e o mata com um tiro na cabeça!\n")
            #Tira 40 pontos de vida
            life = life - 40
            print(f"Você tomou um dano! Sua vida atual é {life}.\n")
            print("-"*142)
            print("STATUS 007 CONFIRMADO!!!")
            print("-"*142)
        #Sucesso na tentativa
        else:
            print("RESULTADO DO LANÇAMENTO DO DADO:\nJames Bond calcula que a distância até Dryden é de 2 metros, logo em seguida ele pula em direção ao bandido, ele acerta em cheio um murro no rosto de Dryden que cai no chão e logo em seguida James pega sua arma e dispara contra o traidor.\n")            
            print("-"*142)
            print("STATUS 007 CONFIRMADO!!!")
            print("-"*142)
    #Tentar usar inteligência
    else:
        #x é a variável randômica que sorteia um número entre 10
        x = random.randint(1,10)
        print(f"\nO dado foi lançado, resultado = {x}.\n")
        #Chance de sucesso de 50%
        #Fracasso na tentativa se o resultado do dado for maior que 6
        if x > 6:
            print("RESULTADO DO LANÇAMENTO DO DADO:\nJames Bond, antes de Dryden chegar, vai até a mesa e vasculha as gavetas para ver se encontra algo que possa lhe ameaçar, porém as gavetas estão trancadas e ele não tem tempo para abri-lás antes que Dryden chegue. Então ele insere um pedaço de metal na fechadura para que Dryden não consiga abri-lás, no entanto ele corta seu dedo no metal. \n")
            #Tira 40 pontos de vida
            life = life - 40
            print(f"Você tomou um dano! Sua vida atual é {life}.\n")
            print("-"*142)
            print("STATUS 007 CONFIRMADO!!!")
            print("-"*142)
        #Sucesso na tentativa
        else:
            print("James Bond, antes de Dryden chegar, vai até a mesa e vasculha as gavetas para ver se encontra algo que possa lhe ameaçar. Ele encontra uma pistola, então ele retira todas as balas e coloca a arma na gaveta novamente e vai volta a senta na poltrona.\n")            
            print("-"*142)
            print("STATUS 007 CONFIRMADO!!!")
            print("-"*142)
#------------------------------------------------------------------------------------------------------------------------
    #Descrição do início do ato 2
    print("M, chefe do MI6, manda Bond em sua primeira missão como 007 para Madagascar, com o objetivo de perseguir um fabricante de bombas profissional chamado Mollaka. 007 segue Mollaka até um rigue de briga de galo, e em um vacilo de seu parceiro, Mollaka percebe e sai em disparada. Depois de uma perseguição free running até a embaixada de Nanbuto, sob tiroteio disparado pela segurança da embaixada, Bond mata Mollaka na frente de todos.\n")
    print("-"*142)

    #Ato2 é a variável que escolhe a opção do que James Bond irá fazer
    ato2 = int(input("O que James Bond vai fazer agora?\nDigite 1 para explodir uma bomba e fugir ou 2 para se proteger dos tiros e fugir: "))
    print("-"*142)
    #Tentar explodir bomba
    if ato2 == 1:
        #Tentativa de explodir bomba
        print("James Bond prepara uma bomba para joga-lá, para isso ele precisa acertar a senha!")
        print("-"*142)     
        #Define o contador de tentativas em desarmar a bomba  
        ct=0
        while True:
            #Variável senha para as 3 tentativas        
            senha = int(input(f"Qual a senha (0-9), restam {3-ct} tentativas: "))
            #Adiciona 1 no contador de tentativas em desarmar a bomba
            ct+=1
            #Falha na tentativa se errar 3 vezes a senha
            if ct > 2:
                print("RESULTADO DA TENTATIVA:\nVocê não conseguiu armar a bomba e teve que sair rasteijando entre os objetos que estavam por ali, mesmo assim estilhaços dos tiros te acertaram na fuga.")
                print("-"*142)
                #Tira 40 pontos de vida
                life = life - 40
                print(f"Você tomou um dano! Sua vida atual é {life}.\n")
                print("-"*142)
                #Encerra o if
                break
            #Sucesso na tentativa
            if senha == 123:
                print("Bomba armada!")
                #Inicia a contagem regressiva para explodir a bomba
                for i in range(3, 0, -1):
                    for j in range(2, 0, -1):
                        for k in range(1, 0, -1):
                            print(i,j,k)
                            time.sleep(1)
                print("RESULTADO DA TENTATIVA:\nBOOOMM!!!\nVocê conseguiu armar a bomba e a lançou na direção dos seguranças, matando todos eles!")
                print("-"*142)
                #Encerra o if  
                break
    #Tentar se proteger dos tiros
    else:
        print("James Bond observa em volta e procura possibilidades de fuga. Ele encontra um alçapão protejido dos tiros, porém está trancado com cadeado e para fugir ele precisa acertar a senha!")
        print("-"*142)   
        #Define o contador de tentativas em desarmar a bomba      
        ct=0
        while True:
            #Variável senha para as 3 tentativas        
            senha = int(input(f"Qual a senha, restam {3-ct} tentativas: "))
            #Adiciona 1 no contador de tentativas em abrir o cadeado
            ct+=1
            #Falha na tentativa em abrir o cadeado
            if ct > 2:
                print("RESULTADO DO LANÇAMENTO DO DADO:\nVocê não conseguiu acertar a senha e teve que sair rasteijando entre os objetos que estavam por ali, mesmo assim estilhaços dos tiros te acertaram na fuga.")
                print("-"*142)
                #Tira 40 pontos de vida
                life = life - 40
                print(f"Você tomou um dano! Sua vida atual é {life}.\n")
                print("-"*142)
                #Encerra o if
                break
            #Sucesso na tentativa
            if senha == 123:
                print("Cadeado aberto!")
                for i in range(3, 0, -1):
                    for j in range(2, 0, -1):
                        for k in range(1, 0, -1):
                            print(i,j,k)
                            time.sleep(1)
                print("RESULTADO DO LANÇAMENTO DO DADO:\nVocê conseguiu abrir o cadeado e conseguiu fujir pelo túnel qui havia ali.")
                print("-"*142)
                #Encerra o if
                break
    #Final do enredo do ato 2
    print("Antes de matar Malloka, 007 obve o celular de Mollaka e descobre que ele recebeu telefonemas de Le Chiffre, que está nas Bahamas. Lá, Bond frustra o plano de Le Chiffre de destruir o protótipo de avião desenvolvido para os terroristas, deixando o banqueiro com uma enorme perda e em apuros.")
#------------------------------------------------------------------------------------------------------------------------
    #Descrição do início do ato 3
    print("Agora sob pressão para recuperar o dinheiro de seus clientes, Le Chiffre vai ao Cassino Royale em Montenegro. Esperando que um fracasso em sua tentativa forçaria Le Chiffre a ajudar o governo britânico em troca de proteção contra seus clientes, o MI6 coloca Bond no Cassino. Ele se encontra com Vesper Lynd, agente do Tesouro que é enviada cuidar dos 10 milhões de dólares necessários para comprar as fichas. \n")
    print("-"*142)

    #Ato3 é a variável que escolhe a opção do que James Bond irá fazer
    ato3 = int(input("Após um tempo, depois de jogar um jogo de adivinhação, Bond perde todo o seu dinheiro. Vesper diz que seria um desperdício de dinheiro continuar a financiar Bond e se recusa a dar os 5 milhões de dólares necessários para ele comprar mais fichas e continuar jogando. O QUE JAMES BOND VAI FAZER AGORA?\nDigite 1 para assassinar Le Chiffre ou 2 para pedir ajuda a CIA: "))
    print("-"*142)
    #Tentar assassinar Le Chiffre
    if ato3 == 1:
        print('Sem saber o que fazer Bond pensa em um plano digno de um espião 00 para matar Le Chiffre. Seu plano consiste em envenenar o vilão, mas para isso ele precisa achar o cofre onde está guardado o veneno antes que persebam sua ausência.')
        print("-"*142)
        #Sorteia um número do jogo
        sorteado = random.randint(1, 51)
        #Inicia o contador de tentativas
        tentativa = 0
        #Inicia a variável como zero pois nunca será na variável sorteado
        chute = 0
        #Condição de parada
        while chute != sorteado:
            #Variável de entrada do número escolhido
            chute = int(input ('Escolha um cofre para abri-lo (1-50): '))
            #Adiciona 1 ao contador tentativa
            tentativa+=1
            #Verifica se o número escolhido foi o sorteado
            if chute == sorteado:
                print ('Bond encontra o cofre e pega o veneno. Em seguida, Bond em um ato quase de suicídio, consegue colocar o veneno no copo de Le Chiffre. Depois de um curto período de tempo, o vilão começa a se sentir mal. Sem saber o que fazer Le Chiffre saca sua arma e tenta atirar em Bond, mas ele já se encontra sem força e não consegue efetuar o disparo. Logo em seguida ele cai morto no chão e Bond termina falando Meu nome é Bond, James Bond!')
                print("-"*142)
            #Limita o número de tentativas em 6
            elif tentativa == 6:
                print('Bond falha em encontrar o cofre e Le Chiffre e seus associados tentam matar Bond afogado jogando-o da janela ao mar, porém ele sobrevive a queda e não morre afogado.')
                print("-"*142)
                #Tira 40 pontos de vida
                life = life - 40
                print(f"Você tomou um dano! Sua vida atual é {life}.\n")
                print("-"*142)
                if life > 0:                                    
                    print('Logo em seguida vai até seu Aston Martin DB8 e pega um rifle de longo alcance. Depois de se posicionar em um local com vista privilegiada do vilão, ele efetua o disparo e mata Le Chiffre e Bond termina falando Meu nome é Bond, James Bond!')
                else:
                    print("James Bond está morto!!!")
                break
            #Verifica se o número digitado é maior que o sorteado
            elif chute > sorteado:
                print ('Seu chute está mais alto que o valor sorteado! Chute um valor mais baixo.')
            #Verifica se o número digitado é menor que o sorteado
            else:
                print ('Seu chute está mais baixo que o valor sorteado! Chute um valor mais alto.')
    #Pedir ajuda a CIA
    else:
        print('O agente da CIA Felix Leiter, que também estava jogando, se oferece para financiar Bond em troca da custódia de Le Chiffre. Agora Bond pode continuar.')
        print("-"*142)
        #Sorteia um número do jogo
        sorteado = random.randint(1, 51)
        #Inicia o contador de tentativas
        tentativa = 0
        #Inicia a variável como zero pois nunca será na variável sorteado
        chute = 0
        #Condição de parada
        while chute != sorteado:
            #Variável de entrada do número escolhido
            chute = int(input ('Escolha um número para adivinhar: '))
            #Adiciona 1 ao contador tentativa
            tentativa+=1
            #Verifica se o número escolhido foi o sorteado
            if chute == sorteado:
                print ('De volta ao jogo, Bond começa a ganhar repedidamente e acumular fichas, e vence o vilão tirando todo seu dinheiro. Logo em seguida vai até seu Aston Martin DB8 e pega um rifle de longo alcance. Depois de se posicionar em um local com vista privilegiada do vilão, ele efetua o disparo e mata Le Chiffre e Bond termina falando Meu nome é Bond, James Bond!')
                print("-"*142)
            #Limita o número de tentativas em 6
            elif tentativa == 6:
                print('Le Chiffre e seus associados tentam matar Bond envenenando sua bebida, porém ele sobrevive. Mesmo envenenado, vence o vilão tirando todo seu dinheiro. Logo em seguida vai até seu Aston Martin DB8 e pega um rifle de longo alcance. Depois de se posicionar em um local com vista privilegiada do vilão, ele efetua o disparo e mata Le Chiffre e Bond termina falando Meu nome é Bond, James Bond!')
                print("-"*142)
                #Tira 10 pontos de vida
                life = life - 10
                print(f"Você tomou um dano! Sua vida atual é {life}.\n")
                print("-"*142)
                break
            #Verifica se o número digitado é maior que o sorteado
            elif chute > sorteado:
                print ('Seu chute está mais alto que o valor sorteado! Chute um valor mais baixo.')
            #Verifica se o número digitado é menor que o sorteado
            else:
                print ('Seu chute está mais baixo que o valor sorteado! Chute um valor mais alto.') 
    break
print("------------FIM-------------")