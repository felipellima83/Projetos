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
    print("James Bond está em uma missão que, se for completada com sucesso, vai o qualificar para ser um agente 00. Ele vai para Praga, para matar um chefe de seção do MI6, Dryden, que vazou uma informação confidencial. Depois de conversarem, no escritório do Dryden, e James relatar o que veio fazer ali, Dryden saca uma arma de uma gaveta e se prepara para disparar.No mesmo momento em que James Bond vai cumprir sua missão, em outro lugar, um homem chamado apenas de Sr. White servia como intermediário apresentando o banqueiro Le Chiffre a um grupo terrorista que procura um paraíso fiscal para guardar seu dinheiro.\n")
    print("-"*142)

    #Ato1 é a variável que escolhe a opção do que James Bond irá fazer
    ato1 = int(input("O que James Bond vai fazer agora? Você consegue terminar o filme vivo?\nDigite 1 para lançar o dado e tentar entrar em luta corporal e roubar a arma de Dryden ou 2 para lançar o dado e tentar usar a inteligência de um espião: "))
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
            #Tira 10 pontos de vida
            life = life - 10
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
            #Tira 10 pontos de vida
            life = life - 10
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
    print("M, chefe do MI6, manda Bond em sua primeira missão como 007 para Madagascar, com o objetivo de perseguir um fabricante de bombas profissional chamado Mollaka. 007 segue Mollaka até um rigue de briga de galo, e em um vacilo de seu parceiro, Malloka percebe e sai em disparada. Depois de uma perseguição free running até a embaixada de Nanbuto, sob tiroteio disparado pela seguança da embaixada, Bond mata Mollaka na frente dos seguranças.\n")
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
            senha = int(input(f"Qual a senha, restam {3-ct} tentativas: "))
            #Adiciona 1 no contador de tentativas em desarmar a bomba
            ct+=1
            #Falha na tentativa se errar 3 vezes a senha
            if ct > 2:
                print("RESULTADO DO LANÇAMENTO DO DADO:\nVocê não conseguiu armar a bomba e teve que sair rasteijando entre os objetos que estavam por ali, mesmo assim estilhaços dos tiros te acertaram na fuga.")
                print("-"*142)
                #Tira 10 pontos de vida
                life = life - 10
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
                print("RESULTADO DO LANÇAMENTO DO DADO:\nBOOOMM!!!\nVocê conseguiu armar a bomba e a lançou na direção dos seguranças, matando todos eles!")
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
                #Tira 10 pontos de vida
                life = life - 10
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
    print("Antes de matar Malloka, 007 obve o celular de Mollaka e descobre que ele recebeu telefonemas de Le Chiffre, que está nas Bahamas. Lá, Bond frustra o plano de Le Chiffre de destruir o protótipo de avião desenvolvido para os terroristas, deixando o banqueiro com uma enorme perda.")
#------------------------------------------------------------------------------------------------------------------------
    #Descrição do início do ato 3
    print("\n")
    print("-"*142)

    #Ato3 é a variável que escolhe a opção do que James Bond irá fazer
    ato3 = int(input(""))
    print("-"*142)
    #Tentar 
    if ato3 == 1:
        print()
    else:
        print()

#------------------------------------------------------------------------------------------------------------------------
    #Descrição do início do ato 4
    print("\n")
    print("-"*142)

    #Ato4 é a variável que escolhe a opção do que James Bond irá fazer
    ato4 = int(input(""))
    print("-"*142)
    #Tentar 
    if ato4 == 1:
        print()
    else:
        print()

#------------------------------------------------------------------------------------------------------------------------
    #Descrição do início do ato 5
    print("\n")
    print("-"*142)

    #Ato5 é a variável que escolhe a opção do que James Bond irá fazer
    ato5 = int(input(""))
    print("-"*142)
    #Tentar 
    if ato5 == 1:
        print()
    else:
        print()

#------------------------------------------------------------------------------------------------------------------------
    #Descrição do início do ato 6
    print("\n")
    print("-"*142)

    #Ato6 é a variável que escolhe a opção do que James Bond irá fazer
    ato6 = int(input(""))
    print("-"*142)
    #Tentar 
    if ato6 == 1:
        print()
    else:
        print()
print("------------FIM-------------")
"""
ENREDO
Na sequência de abertura, James Bond está em uma missão que, se for completada com sucesso, vai o qualificar para ser um agente 00. Ele vai para Praga e mata um chefe de seção do MI6, Dryden, que vazou uma informação confidencial, e seu aliado, Fisher. Em outro lugar, um homem chamado apenas de Sr. White serve como intermediário apresentando o banqueiro Le Chiffre a um grupo terrorista que procura um paraíso fiscal para guardar seu dinheiro. Le Chiffre garante que não há riscos para o dinheiro, porém seus investimentos envolvem um risco considerável: ele vende a descoberto ações em companhias de sucesso e depois cria um ataque terrorista para afundar os preços das ações.[9]

M, chefe do MI6, manda Bond em sua primeira missão como 007 para Madagascar, com o objetivo de perseguir um fabricante de bombas profissional chamado Mollaka. Depois de uma perseguição free running até a embaixada de Nanbuto, Bond mata Mollaka e explode parte do prédio para escapar. Ele obtêm o celular de Mollaka e descobre que ele recebeu telefonemas de Alex Dimitrios, um associado de Le Chiffre, que mora nas Bahamas. Bond viaja até Nassau e seduz a esposa de Dimitrios, Solange. Enquanto atendia um telefonema, Solange revela que seu marido está indo para Miami. Bond vai embora para persegui-lo. Em Miami, 007 mata Dimitrios e depois segue o capanga de Le Chiffre, Carlos, até o Aeroporto Internacional de Miami. Lá, Bond frustra o plano de Le Chiffre de destruir o protótipo de avião desenvolvido pela Skyfleet ao conseguir prender a bomba em Carlos, deixando o banqueiro com uma enorme perda.[9]

Agora sob pressão para recuperar o dinheiro de seus clientes, Le Chiffre arruma um torneio de poquer de alto risco no Cassino Royale em Montenegro. Esperando que uma derrota forçaria Le Chiffre a ajudar o governo britânico em troca de proteção contra seus clientes, o MI6 coloca Bond no torneio. Ele se encontra com René Mathis, seu aliado em Montenegro, e com Vesper Lynd, agente do Tesouro que é enviada cuidar dos 10 milhões de dólares necessários para comprar as fichas. Após um tempo depois do início do torneio, Bond perde todo o seu dinheiro. Vesper diz que seria um desperdício de dinheiro continuar a financiar Bond e se recusa a dar os 5 milhões de dólares necessários para ele comprar mais fichas e continuar jogando.[9]

Perturbado por sua derrota, Bond resolve assassinar Le Chiffre. Antes que ele faça o que estava planejando, o agente da CIA Felix Leiter, que também estava jogando no torneio, intervem e se oferece para financiar Bond em troca da custódia de Le Chiffre. De volta ao jogo, Bond começa a acumular fichas. Le Chiffre e seus associados tentam matar Bond envenenando sua bebida, porém ele sobrevive e vence o torneio. Pouco tempo depois, Le Chiffre sequestra Vesper e a usa para atrair Bond para uma quase fatal perseguição de carros, que termina com sua captura. Le Chiffre tortura Bond para ter acesso aos códigos para os ganhos do torneio. Quando se torna claro que Bond não vai cooperar, Le Chiffre avança para castrá-lo, dizendo a Bond que ele ainda vai receber proteção dos britânicos pela informação que ele possui sobre seus empregadores, mesmo se Bond e Vesper forem mortos. O Sr. White entra na sala e mata Le Chiffre e seus associados, aparentemente depois de ter ouvido Le Chiffre admitir que ele trairia White e sua organização. Bond e Vesper são deixados vivos.[9]

Bond acorda em um hospital no Lago de Como, e ordena que Mathis, que tinha revelado ser um agente duplo, seja preso. Bond admite que ele está apaixonado por Vesper e promete deixar o serviço secreto antes que esse tire toda sua humanidade. Ele envia sua carta de demissão para M e vai para umas férias românticas com Vesper em Veneza. Porém, logo, Bond descobre que seus ganhos no poquer não foram depositados na conta do Tesouro. Percebendo que Vesper havia roubado o dinheiro, ele a persegue e também persegue membros de uma organização que ela estava trabalhando até um prédio em obras. Após matar os inimigos dentro e fora do prédio, Bond encontra Vesper presa no elevador. Se desculpando pela traição, ela se tranca dentro do elevador e mergulha na água. Bond tenta resgatá-la, porém ela se afoga antes que ele chegasse a ela. Sr. White, observando de uma varanda, vai embora com o dinheiro.[9]

Bond, se sentindo traído, descobre de M que Vesper tinha um namorado franco-argelino que foi sequestrado pela organização por trás de Le Chiffre e Sr. White e que ela havia concordado em entregar o dinheiro se Bond fosse deixado vivo. Ele descobre o nome e o número de White no celular de Vesper. White, chegando em uma grande casa perto do Lago de Como, recebe um telefonema e pede que o homem do outro lado da linha se identifique. Enquanto Sr. White termina de fazer a pergunta sobre a identidade do homem, ele é atingido na perna por um tiro. Enquanto ele se rasteja até a casa, Bond aparece, com uma arma em uma mão e um celular na outra, e responde: "Meu nome é Bond, James Bond".[9]
"""