import random
ct=0
pontuacaoJ = 0
pontuacaoC = 0
print("JOGO PEDRA, PAPEL OU TESOURA\n")
while ct<5:
    opcao = int(input("Digite 1 p/ pedra, 2 p/ papel ou 3 p/ tesoura. Qual sua escolha? "))
    x = random.randint(1, 3)
    if opcao ==1:
        ct+=1
        print(f"O resultado da {ct}ª rodada foi:" )
        if x == 1:
            print("EMPATE!\nAmbos os jogadores escolheram pedra.\n")
        elif x == 2:
            print("DERROTA!\nVocê escolheu pedra e o computador papel.\n")
            pontuacaoC+=1
        else:
            print("VITÓRIA!\nVocê escolheu pedra e o computador tesoura.\n")
            pontuacaoJ+=1
    elif opcao == 2:
        ct+=1
        print(f"O resultado da {ct}ª rodada foi:" )
        if x == 1:
            print("VITÓRIA!\nVocê escolheu papel e o computador pedra.\n")
            pontuacaoJ+=1
        elif x == 2:
            print("EMPATE!\nAmbos os jogadores escolheram papel.\n")
        else:
            print("DERROTA!\nVocê escolheu papel e o computador tesoura.\n")
            pontuacaoC+=1
    elif opcao == 3:
        ct+=1
        print(f"O resultado da {ct}ª rodada foi:" )
        if x == 1:
            print("DERROTA!\nVocê escolheu tesoura e o computador pedra.\n")
            pontuacaoC+=1
        elif x == 2:
            print("VITÓRIA!\nVocê escolheu tesoura e o computador papel.\n")
            pontuacaoJ+=1
        else:
            print("EMPATE!\nAmbos os jogadores escolheram tesoura.\n") 
    else:
        print("Opção inválida, tente novamente.\n")
if pontuacaoJ > pontuacaoC:
    print(f"Você ganhou o jogo pelo placar de {pontuacaoJ} x {pontuacaoC}.\n")
elif pontuacaoC > pontuacaoJ:
    print(f"Você perdeu o jogo pelo placar de {pontuacaoC} x {pontuacaoJ}.\n")
else:
    print(f"O jogo empatou no placar de {pontuacaoJ} x {pontuacaoC}.\nFIM DO JOGO!\n")
