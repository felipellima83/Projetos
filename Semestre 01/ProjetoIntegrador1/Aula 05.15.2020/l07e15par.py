'''
15. Elabore a função ePar que recebe um número inteiro e retorna um valor booleano
(true ou false). Ela testa o número inteiro recebido e retorna true(verdadeiro)
se ele for par e retorna false(falso) se ele for ímpar. A fun-ção main lê o número,
chama a função ePar passando o número lido e depois gera a tela de saída testando
o valor retornado pela função ePar. Na tela de saída, mostre a mensagem “É par.” ou
a mensagem “É ímpar.”. Use variável local.
'''

#criar funcao
def e_par (a):
    if a % 2 == 0:
        return True
    else:
        return False

#iniciar o programa
if __name__ == "__main__":
    n1 = int(input("Digite o número: "))
    print(e_par(n1))

'''
Alterações

a. Os operadores relacionais e lógicos (>, <, ==, and, or, etc) "retornam" exatamente
True ou False dependendo da expressão que avaliam. Use essa proprierade para
reescrever o conteúdo da função ePar em apenas uma linha:

def ePar(numero):
    return numero % 2 == 0
    
'''
