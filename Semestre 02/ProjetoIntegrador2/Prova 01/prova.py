#Curso: Ciência da Computação
#Professor: Antônio Barbosa Junior
#Disciplina: Lógica de programação
#Aluno: Felipe Ferreira Lima e Lima
#Matrícula: 22001310
#Data: 22/10/2020

#Prova 01

#Exercício 01
'''
def maximo(a,b,c):
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return maior

if __name__ == "__main__":
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))
    retorno = maximo(n1,n2,n3)
    print(f"O maior é {retorno}.")
'''

#Exercício 02
'''
lista = [ ]
qnt_lista = int(input("Quantidade de números na lista: "))
for i in range(qnt_lista):
    n = int(input("Digite o número desejado para compor a lista: "))
    lista.append(n)
print("A lista digitada é: ", lista)

#Letra a
pesquisa = int(input("Qual número deseja buscar: "))
if pesquisa in lista:
    posicao = lista.index(pesquisa)
    print("posição:", posicao)
else:
    print("Não possui o elemento buscado!")

#Letra b
lista.sort()
print("A lista em ordem crescente é : ", lista)

#Letra c
lista.insert(1,33)
print("Número 33 inserido na lista, na posição 1!", lista)

#Letra d
lista.sort(reverse=True)
print("A lista em ordem decrescente é: ", lista)

#Letra e
print("A média dos números da lista é: ",sum(lista)/len(lista))

#Letra f
ct = 0
for v in lista:
    if v > 10:
        ct += 1
porcentagem = ct / len(lista) * 100
print("Porcentagem de números maiores que 10 é: ", porcentagem)

#Letra g
#Faça um programa que calcule e mostre a soma dos quadrados dos elementos da lista.
soma=0
for i in lista:
    soma = soma + (i**2)
print("A soma dos quadrados dos elementos do vetor é: ", soma)
'''

#Exercício 03

class Livro(object):
    def __init__(self, titulo, autor, paginas, preco=100):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.preco = preco
    
    def get_autor(self):
        return self.autor

    def get_preco(self):
        return self.preco

    def set_preco(self, novo_preco):
        self.preco = novo_preco
    
    def porcentagem(self,porcentagem):
        self.preco = (self.preco * (porcentagem/100)) + self.preco
    
    def retorna_dados(self):
        dados = str(self.titulo) + ' - ' + str(self.autor) + ' - ' + str(self.paginas) + ' - ' + str(self.preco)
        return dados
    

if __name__ == '__main__':
    livro_1 = Livro("Java como programar", "Paul Deitel", 934, 550)
    livro_2 = Livro("Python como programar", paginas=1001)
    livro_3 = Livro("C++ como programar", preco=330)
    print('Dados concatenados: ', livro_1.retorna_dados())
    print('Dados concatenados: ', livro_2.retorna_dados())
    print('Dados concatenados: ', livro_3.retorna_dados())
    Livro.get_autor(livro_1)
    Livro.set_preco(livro_1, 45)
    Livro.aumento_porcentagem(livro_1, 10)
    