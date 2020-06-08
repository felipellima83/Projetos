#Curso: Ciência da Computação
#Professor: Antônio Barbosa Junior
#Disciplina: Lógica de programação
#Alunos: Altair Correia Azevedo, André Luiz Vieira Mostaro e Felipe Ferreira Lima e Lima

# While com if dentro 01
# JOGO DE ADVINHAÇÃO - em uma disputa emocionante contra o astuto PY_PC, o usuário tem 3 tentativas para acertar qual número foi escolhido... preste atenção nas dicas e boa sorte!!!

from random import randint
computador = randint(0,10)
print("-"*60)
print("Olá, sou seu PY_PC e pensei em número entre 0 e 10.")
print("Será que você é capaz de acertar qual número pensei?")
print("Você tem 3 tentativas... Boa sorte!!!")
print("-"*60)
acertou = False
tentativas = 0
while not acertou:
    num = int(input("Digite um numero de 0 a 10: "))
    if num == computador:
        tentativas += 1
        acertou = True
        print("=" * 60)
        print("YOU WIN!!!\nPensei no número {} e você precisou de {} tentativa(s).".format(computador, tentativas))
        print("-" * 60)
    else:
        if num < computador:
            tentativas += 1
            print("DICA: MAIS...")
            print("Agora você só tem mais {} tentativas.".format(3-tentativas))
            print("=" * 60)
        elif num > computador:
            tentativas += 1
            print("DICA: MENOS...")
            print("Agora você só tem mais {} tentativas.".format(3 - tentativas))
            print("=" * 60)
    if tentativas == 3:
        print("=" * 60)
        print("GAME OVER... YOU LOOSE!!!")
        print("=" * 60)
        break