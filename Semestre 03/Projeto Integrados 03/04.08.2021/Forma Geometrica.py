"""   CEUB   -   Bacharelado em Ciência da Computação   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.

Teoria:
- Uma classe abstrata deve herdar de ABC (Abstract Base Classes)
- A superclasse abstrata FormaGeometrica com os métodos abstratos area e perímetro.
- Uma classe abstrata tem que ter pelo menos um método abstrato
- Pode ter métodos concretos
- Não posso instanciar um objeto de uma classe abstrata
- As subclasses Circulo e Quadrado herdam da superclasse abstrata e tem que
implementar todos os métodos abstratos da superclasse

Implemente:
1- Crie a superclasse abstrata FormaGeometrica (Abstract Base Classes)
- Crie os dois métodos abstratos area e perímetro
- Crie um objeto da superclasse abstrata FormaGeometrica, teste
- Crie a subclasse Quadrado que herda da superclasse abatrata FormaGeometrica
5- Crie o construtor com o atributo lado
- Método get_lado
- Sobreescreva o método area da superclasse abstrata
- Crie um objeto da subclasse Quadrado, teste
- Sobreescreva o método perímetro da superclasse abstrata
10- Crie um objeto de Quadrado, teste
- Crie a subclasse Circulo que herda de FormaGeometrica
- Crie o construtor com o atributo lado
- Método get_lado
- Sobreescreva o método area
15- Crie um objeto da subclasse Circulo, teste
- Sobreescreva o método perímetro
- Crie um objeto de Circulo, teste
- Crie um método concreto na superclasse para mostrar uma mensagem, teste
- Crie mais um método concreto para mostrar uma mensagem na superclasse
  e identifique o objeto da subclasse que chamou o método, teste
20- Refaça sem mostrar o endereço hexadecimal, mostre só o nome da classe       """
from abc import ABC, abstractmethod  # Importa o módulo abc
class FormaGeometrica(ABC):     # Classe abstrata, herda de ABC
    @abstractmethod             # decorator
    def area(self):             # Método abstrato
        ...                     # Equivalente ao pass
    @abstractmethod
    def perimetro(self):        # Método abstrato
        pass                    # Equivalente ao ...
    def mensagem(self):         # Método concreto
        print('Método concreto da superclasse abstrata FormaGeometrica que herda de ABC')
    def mensagem2(self):        # Método concreto
        print('Método concreto da superclasse abstrata FormaGeometrica que herda de ABC')
        print(self)
    def mensagem3(self):
        print('Método concreto da superclasse abstrata FormaGeometrica que herda de ABC')
        print('Nome da classe:', self.__class__.__name__)

class Quadrado(FormaGeometrica):  # Subclasse Quadrado que herda da superclasse abstrata FormaGeometrica
    def __init__(self, lado):
        self.lado = lado
    def get_lado(self):
        return self.lado
    def area(self):     # Método obrigatório, sobreescreve o método abstrato da superclasse abstrata
        vl_area = self.lado ** 2
        return vl_area
    def perimetro(self):  # Método obrigatório, sobreescreve o método abstrato da superclasse abstrata
        vl_perimetro = 4 * self.lado
        return vl_perimetro

class Circulo(FormaGeometrica):  # A subclasse Circulo herda da superclasse abstrata
    def __init__(self, raio):
        self.raio = raio

    def get_lado(self):
        return self.raio

    def area(self):     # Método obrigatório, sobreescreve o método abstrato da superclasse abstrata
        vl_area = 3.14 * pow(self.raio, 2)
        return vl_area

    def perimetro(self):  # Método obrigatório, sobreescreve o método abstrato da superclasse abstrata
        vl_perimetro = 2 * 3.14 * self.raio
        return vl_perimetro

if __name__ == '__main__':
    # o_forma = FormaGeometrica()     # TypeError
    # TypeError: Can't instantiate abstract class FormaGeometrica with abstract methods area, perimetro
    o_quad = Quadrado(3)
    print('Área:', o_quad.area())
    print('Perímetro:', o_quad.perimetro())
    print('Lado:', o_quad.get_lado())
    o_circ = Circulo(3)
    print('Área:', o_circ.area())
    print('Perímetro:', o_circ.perimetro())
    print('Lado:', o_circ.get_lado())
    o_quad.mensagem()
    o_circ.mensagem()
    o_quad.mensagem2()
    o_circ.mensagem2()
    o_quad.mensagem3()
    o_circ.mensagem3()