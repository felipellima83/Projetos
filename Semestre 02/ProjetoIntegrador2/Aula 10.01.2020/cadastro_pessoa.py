import datetime

class Pessoa(object):
    def __init__(self, nome, sobrenome, dta_nascimento=datetime.date(2000,1,1)):
    #def __init__(self, nome, sobrenome, dta_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dta_nascimento = dta_nascimento

    def get_nome(self):
        return self.nome
    
    def set_nome (self, novo_nome):
        self.nome = novo_nome
    
    def get_sobrenome(self):
        return self.sobrenome
    
    def set_sobrenome (self, novo_sobrenome):
        self.sobrenome = novo_sobrenome
    
    def get_dta_nascimento(self):
        return self.dta_nascimento
    
    def set_dta_nascimento (self, novo_dta_nascimento):
        self.dta_nascimento = novo_dta_nascimento
    
    def nome_completo(self):
        nome_completo = self.get_nome() + ' ' + self.get_sobrenome()
        return nome_completo
    
    def set_nome_completo (self, novo_nome_completo):
        self.nome_completo = novo_nome_completo
    
    def __str__(self):
        dados = "{},{},{}".format(self.nome,self.sobrenome,self.dta_nascimento)
        return dados

    def calcula_idade(self):
        hoje = datetime.date.today()
        idade = hoje.year - self.dta_nascimento.year
        if hoje.month < self.dta_nascimento.month:
            idade -=1
        elif hoje.month == self.dta_nascimento.month and hoje.day < self.dta_nascimento.day:
            idade -=1
        return idade
    
    def mais_velho(self, pessoa):
        if self.calcula_idade() < pessoa.calcula_idade():
            print("\nA idade de ",self.get_nome()," é maior: ",self.calcula_idade())
        elif self.calcula_idade() == pessoa.calcula_idade():
            print("\nAs duas idades sao iguais: ")
        else:
            print("\nA idade de ",pessoa.get_nome()," é maior: ",pessoa.calcula_idade())



if __name__ == '__main__':
    pessoa1 = Pessoa('Carlos','Pereira', datetime.date(1993,12,13))
    print('Pessoa: ',pessoa1)
    nome = pessoa1.get_nome()
    print("Nome: ", nome)    
    print("Data Nascimento: ", pessoa1.get_dta_nascimento())
    pessoa1.set_nome('Ailton')
    print("Nome: ", pessoa1.get_nome())
    dta_nascimento_2 = datetime.date(1985,12,13)
    pessoa1.set_dta_nascimento(dta_nascimento_2)
    print("Data Nascimento: ", pessoa1.get_dta_nascimento())
    print("Nome Completo: ", pessoa1.nome_completo())
    dta_nascimento_3 = datetime.date(2000,11,23)
    pessoa2 = Pessoa('Maria','Souza',dta_nascimento_3)
    print("Nome: ", pessoa2.get_nome())
    print("Data Nascimento: ", pessoa2.get_dta_nascimento())
    print("Nome Completo: ", pessoa2.nome_completo())
    pessoa3 = Pessoa('Ana','Souza')
    print('Pessoa3: ', pessoa3.get_dta_nascimento())
    print("Nome Completo: ", pessoa3.nome_completo())
    print("Idade: ", pessoa1.calcula_idade())
    pessoa1.mais_velho(pessoa2)
