class Aluno (object):
    def __init__ (self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade
        
    def get_nome (self):
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
    


if __name__ == '__main__':
    aluno1 = Aluno('Felipe',100,17)
    print("Nome: ", aluno1.get_nome())
    novo_nome = input("Novo nome: ")
    aluno1.set_nome(novo_nome)
    print("Nome: ", aluno1.get_nome())