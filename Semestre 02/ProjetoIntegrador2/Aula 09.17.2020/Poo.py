'''   UniCEUB   -   Ciência da Computação   -   Prof. Barbosa
Atalho de teclado: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha

- Sintaxe:       POO em Python
class NomeClasse:                                    # class NomeClasse (object):
    def __init__ (self, p_1, p_2, ...):              # Método construtor
        self.nome_atributo1 = p_1                    # Atributos
        self.nome_atributo2 = p_2
        . . .
    def nome_metodo (self):                          # Outros métodos da classe
        # script
        [return]
if __name__ == '__main__':                            # mai <tab>
    nome_objeto1 = NomeClasse(a_1, a_2, ...)        # Cria (instancia) o primeiro objeto da classe
    nome_objeto2 = NomeClasse(a_1, a_2, ...)        # Cria (instancia) o segundo objeto da classe
    . . .
    print ("Valor do atributo x: ", nome_objeto1.x)  # nome_objeto.nome_atributo
    nome_objeto1.nome_atributo = novo_valor          # alterar valor do atributo
    nome_objeto1.nome_metodo()                       # Modelo pra chamar método da classe
    nome_objeto2.nome_metodo()                       # Modelo pra chamar método da classe
----------------------- Com base no modelo acima, implemente estes itens:
1- Crie a classe Aluno
- Crie o construtor da classe com  os atributos: nome, mensalidade, idade
- No main, crie um objeto (instância) da classe 
- Mostre os dados do objeto da classe, aluno1. Não use o método get
5- No main, crie mais um objeto (instância) da classe, aluno2
- Mostre os dados do objeto da classe, aluno2
- Altere a mensalidade do Paulo para 850 reais e teste.
- Crie o método mostra_dados, mostre os atributos nome e idade.
- Testes o método para os dois objetos.
10- Crie o método retorna_dados, retorne os atributos nome e idade concatenados.
- Testes o método para os dois objetos.
- Crie o método pode_cnh, verifica se tem 18 anos ou mais. Mostre mensagem "Pode." ou "Não pode.".
- No main, crie mais um objeto (instância) da classe, aluno3 com menos de 18 anos.
- Testes o método pode_cnh para os três objetos (instâncias) da classe.
15- Crie o método aumento, ele recebe um valor que será acrescido a mensalidade.
- Teste o método para pelo menos uma instância, um aluno
- Crie o método aumento_2, ele não recebe nada e lê o valor do aumento dentro do método. Teste '''
class Aluno:                                        # class Aluno(object):
    def __init__(self, nome, mensalidade, idade):   # Método construtor
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade
    def nome_metodo(self):                          # Modelo de um método de uma classe
        ...                                         # pass
    def mostra_dados (self):
        print('Nome: ', self.nome)
        print('Idade: ', self.idade)
    def retorna_dados (self):
        dados = self.nome + ' - ' + str(self.idade) # concatenação
        return dados
    def pode_cnh(self):
        if self.idade >= 18:
            print("Pode.")
        else:
            print("Não pode.")
    def aumento(self, valor):
        self.mensalidade += valor
    def aumento_2(self):
        vl_aumento = int(input("Aumento: "))
        self.mensalidade += vl_aumento

if __name__ == '__main__':
    aluno1 = Aluno('Paulo', 1000, 21)               # Chamando o construtor (__init__)
    print("Mostra a classe e a posição de emória onde o objeto foio criado: ", aluno1)
    print("Aluno 1:")
    # print("Msg: ", nome_objeto.nome_atributo)
    print("Nome: ", aluno1.nome)                    # nome_objeto.nome_atributo
    print("Mensalidade: ", aluno1.mensalidade)
    print("Idade: ", aluno1.idade)
    aluno2 = Aluno('Carla', 900, 20)
    print("Aluno 2:")
    print("Nome: ", aluno2.nome)
    print("Mensalidade: ", aluno2.mensalidade)
    print("Idade: ", aluno2.idade)
    aluno1.mensalidade = 850                        # nome_objeto.nome_atributo = novo_valor
    print("Mensalidade: ", aluno1.mensalidade)
    aluno1.mostra_dados()                           # nome_objeto.nome_metodo()
    aluno2.mostra_dados()
    print(aluno1.retorna_dados())                   # O método retorna algo
    print(aluno2.retorna_dados())
    aluno3 = Aluno('Hélio', 1000, 17)
    aluno1.pode_cnh()                               # O método nao retorna nada (None)
    aluno2.pode_cnh()
    aluno3.pode_cnh()
    aluno2.aumento(100)
    print(aluno2.mensalidade)
    aluno3.aumento(110)
    print(aluno3.mensalidade)
    aluno1.aumento_2()
    print(aluno1.mensalidade)