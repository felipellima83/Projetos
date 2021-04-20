#Curso: Ciência da Computação
#Professor: Antônio Barbosa Junior
#Disciplina: Lógica de programação
#Aluno: Felipe Ferreira Lima e Lima
#Matrícula: 22001310
#Data: 15/04/2021

#Prova 01

'''
Modele a classe Disciplina com os atributos identificador, nome e professor.
Usando o conceito de associação de classes, o atributo professor da classe Disciplina deve ser um objeto da classe Professor. E a classe Professor tem os atributos cpf, nome e idade.
Implemente a classe Professor com o construtor, os métodos gets e sets mais importantes e pelo menos um método funcional.
Implemente a classe Disciplina com o construtor, os métodos gets e sets necessários e estes métodos
funcionais dentro da classe Disciplina:
- mostra_dados_disciplina, ele mostra todos os dados da disciplina e do professor
- consulta_nome_professor
- altera_idade_professor, faça críticas para evitar dados inconsistentes
No método main, crie dois objetos da classe Disciplina e teste todos os métodos desenvolvidos na classe
Disciplina.
'''
#Exercício 01
"""class Disciplina(object):
    def __init__(self,identificador,nome_disciplina):
        self.identificador=identificador
        self.nome_disciplina=nome_disciplina
        self.professor=Professor()

    def get_identificador(self):
        return self.identificador

    def get_nome_disciplina(self):
        return self.nome_disciplina

    def consulta_nome_professor(self):
        return self.professor.get_nome_professor()

    def get_prof_idade(self):
        return self.professor.get_idade()

    def get_prof_cpf(self):
        return self.professor.get_cpf()

    def set_identificador(self, novo_identificador):
        self.identificador=novo_identificador

    def set_nome(self,novo_nome):
        self.nome=novo_nome

    def mostra_dados_disciplina(self):
        print(f"Nome da disciplina: {self.get_nome_disciplina()}\nIdentificador: {self.identificador}\nInformações do professor\n      Nome do professor: {self.professor.get_nome_professor()}\n      CPF: {self.professor.get_cpf()}\n      Idade:{self.professor.get_idade()}")

    def altera_idade_professor(self):
        nova_idade=int(input("Insira a nova idade do professor: "))
        if nova_idade<27:
            print("Muito novo para ser professor!")
        elif nova_idade>80:
            print("Já pode aposentar!")
        else:
            self.professor.idade=nova_idade
            print("Idade do professor foi alterada!")

class Professor():
    def __init__(self):
        self.nome_professor="Felipe"
        self.cpf=708450
        self.idade=37
        self.salario=0

    def get_nome_professor(self):
        return self.nome_professor

    def get_cpf(self):
        return self.cpf

    def get_idade(self):
        return self.idade

    def set_nome(self,novo_nome_prof):
        self.nome=novo_nome_prof

    def set_cpf(self,novo_cpf):
        self.cpf=novo_cpf

    def set_idade(self,nova_idade):
        self.idade=nova_idade

    def salario(self, novo_salario):
        salario=float(input(f"Qual o valor do salário do {self.nome_professor}? "))
        self.salario=novo_salario
        if novo_salario > 1000.0:
            print(f"O professor {self.nome_professor} recebe um salário muito bom!")
        else:
            print(f"O professor {self.nome_professor} deve recebe um salário melhor!")
            

if __name__ == '__main__':
    disciplina1=Disciplina(1,"Projeto Integrador 3")
    disciplina1.mostra_dados_disciplina()
    disciplina1.altera_idade_professor()
    disciplina2=Disciplina(2,"Projeto Integrador 4")
    disciplina2.mostra_dados_disciplina()"""

#Exercício 02
'''
2. Modele a superclasse abstrata Empregado com os atributos cpf, nome, pelo menos dois métodos
concretos e o método abstrato calcula_pagamento.
Implemente a subclasse concreta EmpregadoAssalariado que herda da superclasse abstrata Empregado com
os atributos cpf, nome, salário fixo e abono. O cálculo do pagamento do empregado assalariado é igual ao salário fixo mais o valor do abono. Crie pelo menos três métodos nesta subclasse.
Implemente a subclasse concreta EmpregadoHorista que herda da superclasse abstrata Empregado com os
atributos cpf, nome, horas trabalhadas no mês, valor em reais da hora. O cálculo do pagamento do empregado
horista é igual as horas trabalhadas no mês vezes o valor de cada hora. Crie pelo menos três métodos nesta
subclasse.
Evite redundância na implementação deste sistema observando os conceitos de herança. E use os conceitos
de classe concreta, classe abstrata, método concreto e método abstrato.
No método main, crie um objeto da classe abstrata Empregado, um objeto da classe concreta Assalariado e
um objeto da classe concreta Horista. Use o método calcula_pagamento com objetos criados e use (teste) também os outros métodos criados nas classes.
'''
from abc import ABC, abstractmethod


class Empregado(ABC):
    def __init__(self, cpf, nome):
        self.nome = nome
        self.cpf = cpf

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    @abstractmethod
    def calcula_pagamento(self):
        pass


class EmpregadoAssalariado(Empregado):
    def __init__(self, cpf, nome, salario_fixo, abono):
        super().__init__(cpf, nome)
        self.salario = salario_fixo
        self.abono = abono

    def get_salario(self):
        return self.salario

    def get_abono(self):
        return self.abono

    def calcula_pagamento(self):
        salario = self.salario + self.abono
        return salario

class EmpregadoHorista(Empregado):
    def __init__(self,cpf,nome,horas_trabalhada,valor_horas):
        super().__init__(cpf,nome)
        self.horas_trabalhada=horas_trabalhada
        self.valor_horas=valor_horas

    def calcula_pagamento(self):
        salario=self.horas_trabalhada*self.valor_horas
        return salario

    def get_horas(self):
        return self.horas_trabalhada

    def get_valorhora(self):
        return self.horas_trabalhada

    def set_horas(self):
        nova_hora=int(input("Digite a sua quantidade de horas: "))
        if nova_hora<0:
            print("Quantidade insuficiente!")
        elif nova_hora > 44:
            print("Quantidade maior que o permitido!")
        else:
            self.horas_trabalhada=nova_hora

if __name__ == '__main__':
    funcionario_assalariado = EmpregadoAssalariado(1100, "Felipe", 1700, 190)
    funcionario_horista = EmpregadoHorista(1000, "João", 1100, 290)
    print(f"Salário Funcionário Assalariado: {funcionario_assalariado.calcula_pagamento()}")
    print(f"Salário Funcionário Horista: {funcionario_horista.calcula_pagamento()}")