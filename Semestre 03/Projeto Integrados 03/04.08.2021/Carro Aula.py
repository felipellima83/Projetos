"""   CEUB   -   Bacharelado em Ciência da Computação   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.

- Uma classe abstrata deve herdar de ABC (Abstract Base Classes)

- Analise o problema de locação de carros e o valor da diária.

Implemente:
1- Crie a classe abstrata Carro
- Crie os atributos nome e preço base de locação com os valores None
- Crie os métodos concretos get dos atributos
- crie o método abstrato retorna_preco_diaria
5- Crie um objeto de Carro, teste
- Crie a subclasse Economico que herda de Carro
- Crie o construtor com os atributos nome e preço base
- Passe esses atributos para a superclasse abstrata
- Crie um obejto da classe carro econômico, teste
10- Sobreescreva o método retorna_preco_diaria
  Para carro econômico, o preço da diária corresponde ao preço base de locação acrescido de 5%
- Crie um obejto da classe carro econômico, teste
- Crie a subclasse Intermediario que herda de Carro
- Crie o construtor com os atributos nome e preço base
- Passe esses atributos para a superclasse abstrata
15- Sobreescreva o método retorna_preco_diaria
  Para carro intermediário, o preço da diário corresponde ao preço base de locação acrescido de 10%
- Crie um obejto da classe carro intermediário, teste         """
from abc import ABC, abstractmethod
class Carro(ABC):                   # Classe abstrata
    nome = None
    preco_base = None
    def get_nome(self):             # Método concreto
        return self.nome
    def get_preco_base(self):       # Método concreto
        return self.preco_base
    @abstractmethod                 # Método abstrato, obrigatório
    def retorna_preco_diaria(self):
        pass

class Economico(Carro):
    def __init__(self, nome, preco_base):
        Carro.nome = nome                   # super().__init__(nome, preco_base)
        Carro.preco_base = preco_base

    def retorna_preco_diaria(self):  # Método obrigatório, sobreescreve o método abstrato da superclasse abstrata
        return self.get_preco_base() * 1.05

class Intermediario(Carro):  # A subclasse Intermediario herda da superclasse Carro (herança)
    def __init__(self, nome, preco_base):
        Carro.nome = nome                   # Passando os dados pra superclasse Carro
        Carro.preco_base = preco_base

    def retorna_preco_diaria(self):
        return self.get_preco_base() * 1.1      # Usa o método da superclasse

class Automatico(Carro):
    def __init__(self, nome, preco_base):
        Carro.nome = nome
        Carro.preco_base = preco_base

    def retorna_preco_diaria(self):
        return self.get_preco_base() * 1.25

if __name__ == '__main__':
    # o_car = Carro()                   # TypeError
    o_eco = Economico('Uno', 100.00)
    print(f'Nome: {o_eco.get_nome()}')                          # Usa método concreto da superclasse
    print(f'Preço base: {o_eco.get_preco_base()}')              # Usa método concreto da superclasse
    print('Diário R$ {:.2f}' .format(o_eco.retorna_preco_diaria()))  # Usa o método da subclasse
    o_int = Intermediario('HB20', 100.00)
    print(f'Nome: {o_int.get_nome()}')                          # Chama o método concreto da superclasse
    print(f'Preço base: {o_int.get_preco_base()}')
    print('Diário R$ {:.2f}' .format(o_int.retorna_preco_diaria()))  # Chama o método da subclasse
    o_aut = Automatico('Captur', 100.00)
    print(f'Nome: {o_aut.get_nome()}')
    print(f'Preço base: {o_aut.get_preco_base()}')
    print('Diário R$ {:.2f}' .format(o_aut.retorna_preco_diaria()))