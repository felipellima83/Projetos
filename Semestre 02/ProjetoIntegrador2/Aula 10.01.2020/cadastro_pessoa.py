'''   UniCEUB   -   Ciência da Computação   -   Prof. Barbosa
Atalho de teclado: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha

Sintaxe:       POO em Pytthon
class NomeClasse:
    def __init__ (self, p_1, p_2):           # Método construtor
        self.nome_atributo1 = p_1
        self.nome_atributo2 = p_2
    def get_nome_atributo1 (self):           # Modelo do método get (consulta um atributo)
        return self.nome_atributo1
    def set_nome_atributo1 (self, valor):    # Modelo do método set (altera valor de um atributo)
        self.nome_atributo1 = valor
    def outro_metodo (self):                 # Outros métodos da classe (fucionais)
        . . .
        [return ...]
if __name__ == '__main__':            # main <tab>
    nome_objeto1 = NomeClasse(a_1, a_2)  # Cria (instancia) o primeiro objeto da classe
    nome_objeto2 = NomeClasse(a_1, a_2)  # Cria (instancia) o segundo objeto da classe
    print ("Valor do atributo x: ", nome_objeto1.x) # nome_objeto . nome_atributo
----- Com base no modelo acima, implemente estes itens:
1- Crie a classe Pessoa
- Crie o método construtor: ele recebe o self e mais três parâmetros que serão armazenados nos atributos.
  No construtor, crie os três atributos da classe (nome, sobrenome e data de nascimento)
- No método main, crie o objeto pessoa1 e passe os argumentos: "Carlos", "Pereira", 1993-12-13
- Mostre o objeto criado, o objeto pessoa1, teste (rode a classe)
5- Na classe, crie os métodos get (consultar) e set (alterar) para os atributos nome e dta_nascimento.
  def get_nome_atributo1 (self):                        # Modelo do método get (consulta)
    return self.nome_atributo1
  def set_nome_atributo1 (self, valor):                 # Modelo do método set (altera)
    self.nome_atributo1 = valor
- No main, teste os métodos gets dos atributos da classe Pessoa (consulte e mostre)
  Mostre o valor do atributo nome, altere o nome do objeto pessoa1 e mostre o valor do atributo dta_nascimento
- Use o método set para alterar o valor do atributo dta_nascimento para 1985-12-13. Teste
- Na classe, crie o método nome_completo. Ele recebe o objeto e retorna o nome completo. Teste
- No programa (main), crie o objeto pessoa2 e passe os argumentos: "Maria", "Souza", 2000-11-23.
10- Teste o item anterior, ou seja, mostre o valor dos atributos do objeto pessoa2
- Altere o contrutor para ele instanciar um objeto sem a dta_nascimento, valor default 2000-01-01.
  Com nome e sobrenome. Teste
12- Sobreescrever o método especial __str__ . Ele recebe o objeto e retorna os dados
    de uma pessoa (nome completo e data de nascimento). Teste.
13- Crie o método calcula_idade, ele recebe o objeto e retorna a idade da pessoa. Teste abaixo:
    No final do main, altere a data da pessoa1 para: (1985, 12, 13). Qual a idade da pessoa1?
----- '''
import datetime
class Pessoa(object):  # Por convenção, o nome de classe começa cada palavra com letra maiúscula. E as outras letras minúsculas.
    def __init__(self, nome, sobrenome, dta_nascimento=datetime.date(2000, 1, 1)):  # Construtor com valor default
    # def __init__(self, nome, sobrenome, dta_nascimento):        # Método construtor
        self.nome = nome                                        # Atributos
        self.sobrenome = sobrenome
        self.dta_nascimento = dta_nascimento
    def get_nome(self):                                         # Métodos gets e sets
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_dta_nascimento(self):
        return self.dta_nascimento
    def set_dta_nascimento(self, nova_data):
        self.dta_nascimento = nova_data
    def nome_completo(self):                                    # Métodos funcionais.
        s = self.nome + ' ' + self.sobrenome
        # s = self.get_nome() + ' ' + self.sobrenome
        # s = '{} {}' . format(self.nome, self.sobrenome)
        # s = f'{self.nome} {self.sobrenome}'
        return s
    def __str__(self):                                          # Sobreescrevendo o método especial __str__
        # s = self.get_nome() + ' ' + self.sobrenome + ', ' + str(self.get_dta_nascimento())
        # s = "{} {}, {}" .format(self.nome, self.sobrenome, self.dta_nascimento)
        # s = f"{self.nome} {self.sobrenome}, {self.dta_nascimento}"
        s = f"{self.nome_completo()}, {self.dta_nascimento}"           # Uso o atributo dta_nascimento
        # s = f"{self.nome_completo()}, {self.get_dta_nascimento()}"     # Uso o método get_dta_nascimento
        return s
    def calcula_idade(self):
        hoje = datetime.date.today()
        idade = hoje.year - self.dta_nascimento.year
        # Dica: Teste os meses de hoje e da data de nascimento. Se precisar os dias também.
        if hoje.month < self.dta_nascimento.month:
            idade -= 1
        elif hoje.month == self.dta_nascimento.month and hoje.day < self.dta_nascimento.day:
            idade -= 1
        return idade

if __name__ == '__main__':
    dta_nascimento_1 = datetime.date(1993, 12, 13)
    pessoa1 = Pessoa("Carlos", "Pereira", dta_nascimento_1)  # Instantiate an object of type Pessoa
    # pessoa1 = Pessoa("Carlos", "Pereira", datetime.date(1993, 12, 13))  # Equivalente as duas linhas acima.
    print(pessoa1)                                           # Chama o método __str__
    nome = pessoa1.get_nome()
    print("Nome: ", nome)
    print("dta_nascimento: ", pessoa1.get_dta_nascimento())
    pessoa1.set_nome("Ailton")
    print('Nome: ', pessoa1.get_nome())
    dta_nascimento_2 = datetime.date(1985, 12, 13)
    pessoa1.set_dta_nascimento(dta_nascimento_2)
    print("dta_nascimento: ", pessoa1.get_dta_nascimento())
    print('Nome completo: ', pessoa1.nome_completo())
    dta_nascimento_3 = datetime.date(2000, 11, 23)
    pessoa2 = Pessoa("Maria", "Souza", dta_nascimento_3)    # chama o método __init__ (construtor)
    print("Nome: ", pessoa2.get_nome())
    print("dta_nascimento: ", pessoa2.get_dta_nascimento())
    print('Idade: ', pessoa1.calcula_idade())
    pessoa3 = Pessoa("Ana", "Souza")
    print('Pessoa 3: ', pessoa3.get_dta_nascimento())
    print('Nome completo: ', pessoa3.nome_completo())
    print(pessoa3.__str__())                    # Duas linhas equivalentes, __str__() é opcional.
    print(pessoa3)
    print(pessoa1)
    print("Idade: ", pessoa1.calcula_idade())
    print("Idade: ", pessoa3.calcula_idade())