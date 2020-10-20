'''   UniCEUB   -   Ciência da Computação   -   Prof. Barbosa
Atalho de teclado: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha

       POO em Pytthon
class NomeClasse (object): 
    def __init__ (self, p_1="nome1", p_2=valor2):   # Método construtor com valor default
        self.nome_atributo1 = p_1                   # Atributos da classe
        self.nome_atributo2 = p_2
    def get_nome_atributo1 (self):                  # Modelo do método get (retorna valor do atributo)
        return self.nome_atributo1
    def set_nome_atributo1 (self, valor):           # Modelo do método set (altera valor do atributo)
        self.nome_atributo1 = valor
    def outro_metodo (self):                        # Outros métodos da classe
        . . .
        [return ...]

if __name__ == '__main__':                      # main <tab>
    nome_objeto1 = NomeClasse(a_1, a_2)         # Cria (instancia) o primeiro objeto da classe
    nome_objeto2 = NomeClasse(a_1)              # Cria (instancia) o segundo objeto da classe
    nome_objeto3 = NomeClasse()                 # Cria (instancia) o terceiro objeto da classe
    print ("Valor do atributo x: ", nome_objeto1.x)  # nome_objeto . nome_atributo
----------------------- Com base no modelo acima, implemente estes itens:
1- Classe Veiculo
- Crie o construtor da classe com os atributos: modelo, ano, valor
- No main, crie pelo menos dois objetos da classe. Teste
- Crie os métodos gets e sets do atributo modelo. Teste
5- Altere o valor do veiculo, crie o método set_valor. Teste
- Faça uma crítica no método set_valor. Teste
- Crie o método mostra_dados. Teste
- Crie o método retorna_dados, ele retorna os dados (atritutos) concatenados. Teste
- Crie o método aumento_valor.
10- Peça pro usuário fornecer o valor do aumento do veículo. Teste
    --- '''
class Veiculo(object):
    def __init__(self, modelo, ano, valor):         # Atalho: def init <tab>
        self.modelo = modelo                        # Atributos
        self.ano = ano
        self.valor = valor
    def get_modelo(self):                           # Métodos gets e sets
        return self.modelo
    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo
    def get_valor(self):
        return self.valor
    def set_valor(self, novo_valor):                # Sem crítica
        self.valor = novo_valor
    def set_valor(self, novo_valor):                # Com crítica
        if novo_valor > 0:
            self.valor = novo_valor
        else:
            print("Valor inconsistente, valor negativo")
    def mostra_dados(self):                         # Métodos funcionais
        print('Modelo: ', self.modelo)
        print('Ano: ', self.ano)
        print('Valor: ', self.valor)
    def retorna_dados(self):
        dados = self.get_modelo() + ' - ' + str(self.ano) + ' - ' + str(self.valor)
        return dados
    def aumento_valor(self, valor):
        self.valor += valor

if __name__ == '__main__':
    carro1 = Veiculo('HB', 2018, 30000)
    carro2 = Veiculo('Corolla', 2019, 90000)
    retorno = carro1.get_modelo()               # Usando variável
    print("Modelo: ", retorno)
    print("Modelo: ", carro2.get_modelo())      # Direto no print
    carro1.set_modelo('HB20')
    print(carro1.get_modelo())
    carro1.set_valor(32000)
    print(carro1.get_valor())
    carro2.set_valor(-12000)
    print(carro2.get_valor())
    carro1.mostra_dados()
    carro2.mostra_dados()
    print('Dados concatenados: ', carro1.retorna_dados())
    carro1.aumento_valor(400)                       # Passando o valor
    print("Novo valor: ", carro1.get_valor())
    vl_aumento = float(input("Valor aumento"))
    carro2.aumento_valor(vl_aumento)                # Usuário digitou
    print(carro2.get_valor())