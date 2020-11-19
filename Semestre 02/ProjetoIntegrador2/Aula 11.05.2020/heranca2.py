'''   UniCEUB   -   Ciência da Computação   -   Prof. Barbosa
Atalho de teclado: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha

1- Crie a classe Funcionario com os atributos nome, cpf, salario
- Crie o construtor da classe Funcionario def __init___ (self, ...). Teste
3- Crie uma instância (objeto f1) da classe com os dados necessários (f1 = Funcionario ( ... ) )
- Crie alguns método get e set e teste.
5- Sobrescreva o método __str__. Ele recebe o objeto e retorna todos os dados do funcionário. Teste.
6- Antes do método main, crie a classe Gerente com os atributos nome, cpf, salario, senha, qtd_gerencia
7- Crie uma instância (objeto g1) da classe Gerente com os dados necessários
8- Mostre todos os dados (atributos) do objeto g1
9- Crie o método autentica dentro da classe Gerente. Ele recebe o objeto, o usuário digita a senha,
   imprime: "Acesso permitido." ou "Acesso negado." e retorna um valor booleano (True ou False).
10- Use o método autentica para o gerente instanciado (objeto g1).
11- Use o método autentica para o funcionario instanciado (objeto f1). Por quê deu erro?
12- Use o método __ str__ para o gerente (objeto g1) instanciado. Por quê mostrou endereço hexadecimal?
13- Crie outra instância (objeto g2) da classe Gerente com os dados necessários.
14- Use todos os métodos da classe Gerente para o gerente g2.
15-h1- Conceito de herança: eliminar código repetido e herdar atributos e métodos
16- A subclasse Gerente herda da superclasse Funcionario
17- Altere o construtor da subclasse Gerente. Teste
18- Crie outra instância (g3) da classe Gerente com os dados necessários. Teste
19-h2- Os funcionários recebem uma bonificação. Todos os funcionários recebem 10% do valor do salário.
    Então: crie o método bonificacao, ele não recebe nada e retorna o valor da bonificação.
20- Mostre a bonificacao das instâncias f1 e g1.
21- Use o método __str__ para o gerente instanciado (objeto g1).
22- Dados incompletos. Por quê? Sobrescreva o método __str__ na classe gerente
23- Altere o __str__ na subclasse, aproveite o que tem no __str__ da superclasse.
24- Utilize o método vars() ou __dict__ para acessar os atributos de Funcionario e Gerente. Ex.: print(vars(objeto))
25- Crie o método salario_total, ele não recebe nada e retorna o salário total do funcionário, ou seja o
valor do salário mais o valor da boninficação.
26- Use o método salario_total para o objeto f1 e o objeto g1.

'''
class Funcionario(object):                        # Nome de classe começa com letra maiúscula.
    def __init__(self, nome, cpf, salario):    # Método dunders
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_cpf(self):
        return self.cpf
    def get_salario(self):
        return self.salario
    def __str__(self):                           # Método mágico ou método dunder
        # s = 'Nome: ' + self.nome+ ',  CPF: ' + self.cpf+ ', salário: ' + str(self.salario) # Linhas equivalentes.
        # s = "Nome: {}, CPF: {}, salario: {:.2f}" .format(self.nome, self.cpf, self.salario)
        s = f"Nome: {self.nome}, CPF: {self.cpf}, salario: {self.salario:.2f}"
        return s
    def bonificacao(self):
        return self.salario * 0.10
    def salario_total(self):
        total = self.salario + self.bonificacao()
        return total

class Gerente(Funcionario):                  # Nome de classe começa com letra maiúscula.
    def __init__(self, nome, cpf, salario, senha, qtd_gerencia):
        super().__init__(nome, cpf, salario)                 # Solução 1
        # Funcionario.__init__(self, nome, cpf, salario)     # Solução 2
        self.senha = senha
        self.qtd_gerencia = qtd_gerencia
    def get_qtd_gerencia(self):
        return self.qtd_gerencia
    def autentica(self):                    # Solução 1
        senha = input("Insira a senha: ")
        if self.senha == senha:
            print("Acesso permitido.")
            return True
        else:
           print("Acesso negado.")
           return False
    # def autentica(self):                    # Solução 2
    #     senha = input("Insira a senha: ")
    #     while senha != self.senha:
    #         print("\033[31mAcesso negado!\033[m")
    #         senha = input("Insira a senha: ")
    #         return False
    #     else:
    #         print("\033[32mAcesso permitido!\033[m")
    #         return True
    def __str__(self):                          # Método mágico ou método dunder
        # s = 'Nome: ' + self.nome+ ',  CPF: ' + self.cpf+ ', salário: ' + str(self.salario+', Qtd.: '+ str(self.qtd_gerenia))
        s = "Nome: {}, CPF: {}, salario: {:.2f}, Qtd.: {}" .format(self.nome, self.cpf, self.salario, self.qtd_gerencia)
        s1 = super().__str__()                           # Aproveitando o método __str__ da superclasse
        s = s1 + ", Qtd.: {}" .format(self.qtd_gerencia)
        return s


if __name__ == '__main__':
    f1 = Funcionario('Paulo', '123', 1000.0)
    print(f1.get_nome())
    print(f1.get_cpf())
    print(f1.get_salario())
    r = f1                              # f1.__str__()
    print (r)
    g1 = Gerente('Paula', '234', 3000.0, 's1', 5)
    print(g1.get_nome())
    print(g1.__str__())                 # print(g1)
    r = g1.autentica()
    print(r)
    g2 = Gerente('Paulo', '34', 5000.0, 'g2', 3)
    print('G2: ', g2.get_nome())
    bonificacao_f1 = f1.bonificacao()               # Usando o método bonificacao
    print("Bonificação de f1", bonificacao_f1)
    bonificacao_g1 = g1.bonificacao()
    print("Bonificação de g1", bonificacao_g1)
    print('__str__ : ', g1)
    print(vars(f1))
    print(f1.__dict__)
    print(vars(g1))
    print(g1.__dict__)
    print('Salário total: ', f1.salario_total())
    print('Salário total: ', g1.salario_total())