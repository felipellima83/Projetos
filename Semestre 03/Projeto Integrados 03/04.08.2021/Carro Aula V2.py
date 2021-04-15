"""   CEUB   -   Bacharelado em Ciência da Computação   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.

- O valor do preço básico de locação é o mesmo (100.00) para os três tipos carros, como
podemos melhorar as classes retirando código redundante.

Implemente:
1- Altere a superclasse abstrata Carro
- Crie o construtor com os atributos nonme e preço base de locação com valor fixo de 100.00
- Refaça a subclasse Economico e retire o atributo preço básico da subclasse.
- Passe o atributo da subclasse para superclasse.
5- Crie um objeto da superclasse Carro, teste
- Crie um objeto da subclasse Economico, teste
- Refaça a subclasse Intermediário e retire o atributo preço básico da subclasse.
- Passe o atributo da subclasse para superclasse.
9- Crie um objeto da subclasse Economico, teste     """
from abc import ABC, abstractmethod
class Carro(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.preco_base = 100.00
    # nome = None
    # preco_base = 100.00

    def get_nome(self):                 # Método concreto
        return self.nome

    def get_preco_base(self):           # Método concreto
        return self.preco_base

    @abstractmethod
    def retorna_preco_diaria(self):     # Método abstrato
        pass

class Economico(Carro):
    def __init__(self, nome):
        super().__init__(nome)
        # Carro.nome = nome         (erro)

    def retorna_preco_diaria(self):
        return self.get_preco_base() * 1.05

class Intermediario(Carro):
    def __init__(self, nome):
        super().__init__(nome)
        # super(Intermediario, self).__init__(nome)

    def retorna_preco_diaria(self):
        return self.get_preco_base() * 1.1

class Automatico(Carro):
    def __init__(self, nome):
        super().__init__(nome)
        # super(Automatico, self).__init__(nome)

    def retorna_preco_diaria(self):
        return self.get_preco_base() * 1.25

if __name__ == '__main__':
    # o_carro = Carro('Modelo')     # TypeError
    o_eco = Economico('Uno')
    print(f'- O carro {o_eco.get_nome()} com:')
    print(f'Preço básico: {o_eco.get_preco_base()}')
    print('Diário R$ {:.2f}' .format(o_eco.retorna_preco_diaria()))
    o_int = Intermediario('HB20')
    print(f'- O carro {o_int.get_nome()} com:')
    print(f'Preço básico: {o_int.get_preco_base()}')
    print('Diário R$ {:.2f}' .format(o_int.retorna_preco_diaria()))
    o_aut = Automatico('Captur')
    print(f'- O carro {o_aut.get_nome()} com:')
    print(f'Preço básico: {o_aut.get_preco_base()}')
    print('Diário R$ {:.2f}' .format(o_aut.retorna_preco_diaria()))