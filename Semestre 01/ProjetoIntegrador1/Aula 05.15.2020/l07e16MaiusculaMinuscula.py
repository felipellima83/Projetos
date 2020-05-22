'''
16.
Construa a função que converta uma letra maiúscula em minúscula. Ela recebe um
caractere qualquer e verifica se é uma letra maiúscula. Se for letra maiúscula,
faça a conversão para letra minúscula; senão retorne o caractere recebido.
O programa principal lê uma tecla, chama a função maiuscula_minuscula passando a
tecla lida e mostra o valor retornado pela função maiuscula_minuscula.
'''

#criar funcao
def maiscula_minuscula(a):
        if a.isupper():
                retorno = a.lower()
        else:
                retorno = a
        return retorno

#iniciar o programa
if __name__ == "__main__":
    while True:
        a = input("Letra: ")
        if a != "aa":
                print(maiscula_minuscula(a))
        else:
                break
        





'''
a.  Obtenha o mesmo resultado sem usar o else
b. Altere o programa para o usuário fazer o teste várias vezes sem sair do programa.
c. Substitua o if por um operador ternário
        DICAS:


'''


