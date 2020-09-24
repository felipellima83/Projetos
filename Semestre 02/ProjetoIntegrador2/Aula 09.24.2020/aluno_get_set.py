class Aluno:
    def __init__(self, nome, mensalidade=1000, idade=19):
    #def __init__(self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade
    
    def get_nome(self):
        return self.nome
    
    def set_nome (self, nome):
        self.nome = nome
    
    def get_mensalidade (self):
        return self.mensalidade
    
    def set_mensalidade (self, mensalidade):
        self.mensalidade = mensalidade
    
    def get_idade (self):
        return self.idade
    
    def set_idade (self, idade):
        self.idade = idade
    
    def mostra_dados (self):
        print('Nome: ', self.nome)
        print('Idade: ', self.idade)
        print("Mesalidade: ", self.mensalidade)
    
    def mostrar_dados_2 (self):
        print('Nome: ', self.get_nome())
        print('Idade: ', self.get_idade())
        print("Mesalidade: ", self.get_mensalidade())
    
    def retorna_dados (self):
        dados = 'Nome: '+self.get_nome() + '\nMesnalidade: ' + str(self.get_mensalidade()) + '\nIdade: ' + str(self.get_idade())
        return dados
    
    def aumento_mensalidade_valor (self, valor):
        self.mensalidade += valor
    
    def aumento_mensalidade_porcentagem(self):
        porcentagem = float(input("Qual a porcentagem do aumento: "))
        self.mensalidade += self.mensalidade * porcentagem/100


if __name__ == '__main__':
    aluno1 = Aluno('Felipe',100,37)
    #print("Nome: ", aluno1.get_nome())
    #novo_nome = input("Novo nome: ")
    #aluno1.set_nome(novo_nome)
    #print("Nome: ", aluno1.get_nome())
    #aluno1.mostra_dados()
    print(aluno1.retorna_dados())
    aluno1.aumento_mensalidade_valor(10)
    print(aluno1.retorna_dados())
    aluno1.aumento_mensalidade_porcentagem()
    print(aluno1.retorna_dados())
    aluno2 = Aluno('Felipe2')
    print(aluno2.retorna_dados())
    aluno3 = Aluno('Felipe3', 800)
    print(aluno3.retorna_dados())
    aluno4 = Aluno('Felipe4',idade=20)
    print(aluno4.retorna_dados())

