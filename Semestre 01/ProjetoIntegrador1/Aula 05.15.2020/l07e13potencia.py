'''
13. Projete a função potencia que recebe dois valores inteiros, a base e o expoente,
e retorna o valor da potência correspondente. O programa lê o valor da base e
do expoente, chama a função potencia passando os dois argumentos (os valores lidos)
e mostra o valor retornado pela função potencia. Considere que a base pode ser um
valor inteiro positivo, nulo ou negativo e o expoente, um inteiro positivo ou nulo.
Não use a função de potência da linguagem Python. E use variável local.
Teste 1: base = 2, expoente = 3. Resposta: 8.
'''
#import
import math

#criar funcao
def potencia (a,b):    
        c = a**b
        print(f"O resultado da potenciação é {c}.")

#iniciar o programa
if __name__ == "__main__":
    #alteração b
    while True:
        n1 = int(input("Digite o valor da base: "))
        n2 = int(input("Qual o valor do expoente: "))
        #alteração a
        if n2 >= 0:
            potencia (n1,n2)
            break
        else:
            print("O valor da potência não pode ser menor que 0!")
    #alteração c
    print(f"O resultado da potenciação é {pow(n1,n2)}.")

'''
Alterações:
a. Com o expoente negativo está dando resultado errado. Resolva este problema.
    Não chame a função se o valor do expoente for negativo.
b. Se o valor do expoente for negativo, peça para o usuário repetir a operação até um
    valor não negativo ser digitado.
c. Em Python a exponenciação pode ser feita da várias formas.
    Refaça sem usar a sua função, use a função do Python.
d. Crie a função leValorInteiro, ela não recebe nada e retorna um valor inteiro.
    O seu objetivo é ler um valor digitado pelo usuário. Altere o programa chamar
    essa função duas vezes e coloque um comentário nos inputs do programa.

'''
