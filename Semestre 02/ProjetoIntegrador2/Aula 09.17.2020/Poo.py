class Aluno:
    def __init__ (self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade

    def mostrar_dados (self):
        dados = self.nome +'-' + str(self.idade)
        print(dados)
    
    def retorna_dados (self):
        dados = self.nome + '-' + str(self.idade)
        return dados
    
    def pode_cnh (self):
        if self.idade >= 18:
            print("Pode!")
        else:
            print("Não pode!")
    
    def aumento (self):
        aumento = float(input("Qual o aumento: ")) 
        self.mensalidade += aumento

if __name__ == '__main__':
    aluno1 = Aluno('Felipe',100,17)
    aluno1.mostrar_dados()
    aluno1.pode_cnh()
    aluno1.aumento()
    print(aluno1.mensalidade)