#Curso: Ciência da Computação
#Professor: Antônio Barbosa Junior
#Disciplina: Lógica de programação
#Aluno: Felipe Ferreira Lima e Lima
#Matrícula: 22001310
#Data: 19/11/2020

#Prova 02

#Exercício 01
#a.
'''
lista = [ ]
t_lista = int(input("Quantidade: "))
for i in range(t_lista):
    n = int(input("Digite o número: "))
    lista.append(n)
    media = sum(lista)/len(lista)
print("Média: ",media)
lista.insert(3,media)
posicao2 = lista.index(3)
print(lista)
#b.
lista.insert(2,77)
lista[2] = 77
print(lista)
#c. Faça um programa que leia um número indeterminado de valores, encerrando a entrada de dados quando for informado um valor igual a -1 e ao final mostre os números pares inseridos na lista
x = 0
lista2 = [ ]
    x = int(input("Digite um número: "))
    lista2.append(x)
print(lista)
print(lista2)
metodo = [num for num in lista2 if num % 2 == 0]
print(metodo)
'''

#Exercício 02
'''
class Time (object):
    def __init__(self, nome, estado = '', qtd_titulos = 0, valor_folha = 0, vitoria = 0, qtd_jogos = 0):
        self.nome = nome
        self.estado = estado
        self.qtd_titulos = qtd_titulos
        self.valor_folha = valor_folha
        self.vitoria = vitoria
        self.qtd_jogos = qtd_jogos
    
    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome
    
    def set_atualiza_nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self.titular = p_nome
        else:
            print('Erro: O nome do time deve ser uma string.')
    
    def get_quantidade(self):
        return self.quantidade
    
# Crie um método que calcule e mostre o aproveitamento de um time
    def aproveitamento(self):
        aproveitamento = self.vitoria/self.qtd_jogos
        return aproveitamento

if __name__ == '__main__':
    time1 = Time('Cruzeiro',vitoria = 2, qtd_jogos=10)
    time2 = Time('Flamengo', qtd_titulos = 3)
    time3 = Time('Chapecoense', valor_folha = 500)
    print(Time.aproveitamento(time1))
'''

#Exercício 03
'''
class Veiculo (object):
    def __init__(self, nome = '', ano = 2020):
        self.nome = nome
        self.ano = ano
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    
    def get_ano(self):
        return self.ano
    
    def set_ano(self, novo_ano):
        self.ano = novo_ano

    def __str__(self):
        s = f"Nome: {self.nome}, Ano: {self.ano}"
        return s

class Carro (Veiculo):
    def __init__(self, nome, ano, cor = 'Prata'):
        super().__init__(nome, ano)
        self.cor = cor
    
    def get_cor(self):
        return self.cor
    
    def set_cor(self, nova_cor):
        self.cor = nova_cor

    def __str__(self):
        s1 = super().__str__()
        s = s1 + ", Cor: {}" .format(self.cor)
        return s


if __name__ == '__main__':
    carro1 = Veiculo('Onix', 2019)
    print (carro1)
    c1 = Carro('Onix', 2019, 'Prata')
    print(c1)
'''