'''   UniCEUB   -   Ciência da Computação   -   Prof. Barbosa
Atalho de teclado: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha
     POO em Pytthon
class NomeClasse:
    def __init__ (self, p_1, p_2):          # Método construtor
        self.nome_atributo1 = p_1
        self.nome_atributo2 = p_2
    def get_nome_atributo1 (self):          # Modelo do método get (consulta um atributo)
        return self.nome_atributo1
    def set_nome_atributo1 (self, valor):   # Modelo do método set (altera valor de um atributo)
        self.nome_atributo1 = valor
    def outro_metodo (self):                # Outros métodos da classe
        . . .
        return ...

if __name__ == '__main__':                  # mai <tab>
    nome_objeto1 = NomeClasse(a_1, a_2)     # Cria (instancia) o primeiro objeto da classe
    nome_objeto2 = NomeClasse(a_1, a_2)     # Cria (instancia) o segundo objeto da classe
    print ("Valor do atributo x: ", nome_objeto1.nome_metodo()) 

----- Com base no modelo acima, implemente estes itens:

1- Crie um novo projeto e crie a classe Point.
- Crie o método construtor, ele recebe self e atribua o valor default zero para os parâmetros de x e y.
3- No construtor, crie os atributos x e y.
- Crie os métodos gets e sets.
5- Na função main, crie o objeto p1 (ponto p1) sem passar argumentos
- Mostre o objeto criado, o ponto p1. Teste
7- Mostre o valor do atributo x e y.
- Na função main, crie o objeto p2 (ponto p2) passsndo os argumentos 2 e 3. Teste
9- Sobreescreva o método especial __str__ . Ele não recebe nada e retorna todos os atributos concatenados. Teste.
- Na função main, crie o objeto p3 (ponto p3) passsndo somente o valor de x. Teste
11- Na função main, crie o objeto p4 (ponto p4) passsndo somente o valor de y. Teste
12- Crie o método distância de um ponto qualquer a origem (0, 0) do plano cartesiano. Ele retorna o valor calculado.
    distancia = raiz_quadrada ( ( x1-x2 )2 + ( y1-y2 )2 )   Teste
    Teste 1: x = 2 e y = 3                  Distância = 3.60555
    Teste 2: x = 3 e y = 5                  Distância = 5.83095
13- Crie o método distancia_dois_pontos, ele retorna a distância de dois pontos quaisquer no plano. Teste
    Teste 1: P1 (2, 3) e P2 (3, 0)          Distância:  3.1622776601683795
    Teste 2: P1 (2, 3) e P2 (0, 5)          Distância:  2.8284271247461903              '''

import math
class Point(object):  # Convenção: a primeira letra de cada palavra maiúscula e as outras minúsculas
    def __init__(self, x=0, y=0):               # def __init__(self, x, y) # Método construtor
        self.x = x                              # Atributos
        self.y = y
    def get_x (self):                           # Método get (retorna o valor de um atributo)
        return self.x
    def set_x (self, valor):                    # Método set (altera o valor de um atributo)
        self.x = valor
    def get_y (self):
        return self.y
    def __str__(self):
        s = '(' + str(self.get_x()) + ', ' + str(self.get_y()) + ')'    # Linhas equivalentes.
        s = "({}, {})" .format(self.get_x(), self.get_y())              # (x, y)   # (2, 3)
        s = f"({self.x}, {self.y})"                                     # (x, y)   # (2, 3)
        return s
    # def distancia_origem1 (self, a, b):                     # Ideia inicial
    #     distancia = math.sqrt((a - 0)**2 + (b - 0)**2)      # Cálculo
    #     return distancia
    def distancia_origem2 (self):                           # Melhor solução, a solução correta.
        distancia = math.sqrt((self.get_x() - 0)**2 + (self.get_y() - 0)**2)
        return distancia
    def distancia_dois_pontos (self, objeto):
        distancia = math.sqrt((self.get_x() - objeto.get_x())**2 + (self.get_y() - objeto.get_y())**2)  # Solução 1
        return distancia
        # return ((((self.get_x() - objeto.get_x()) ** 2) + ((self.get_y() - objeto.get_y()) ** 2)) ** (1/2))  # Solulção 2

if __name__ == '__main__':  # mai <tab>
    p1 = Point()                                    # Instantiate an object of type Point
    print("Objeto p1 da classe Point ", p1)         # print("Objeto p1 da classe Point ", p1.__str__())
    print("Atributo x do ponto p1= ", p1.get_x())
    print("Atributo y do ponto p1= ", p1.get_y())
    p2 = Point(2, 3)
    print("Objeto p2 da classe Point ", p2)
    print("Atributo x do ponto p1= ", p2.get_x())
    print("Atributo y do ponto p1= ", p2.get_y())
    print("Dados: ", p1)
    print("Dados: ", p2)
    p3 = Point(3)
    print("Dados do objeto p3: ", p3)                       # print("__str__ ", p3.__str__())
    print("Atributo x do ponto p1= ", p3.get_x())
    print("Atributo y do ponto p1= ", p3.get_y())
    p4 = Point(y=5)
    print("Dados do objeto p3: ", p4)                       # print("__str__ ", p3.__str__())
    print("Atributo x do ponto p1= ", p4.get_x())
    print("Atributo y do ponto p1= ", p4.get_y())
    # d1 = p2.distancia_origem1(p2.get_x(), p2.get_y())       # Solução ruim
    # print('Distância da origem de p2: ', d1)
    d2 = p2.distancia_origem2()                             # Melhor solução
    print('Distância da origem de p2: ', d2)
    print("Distância da origem: ", p2.distancia_origem2())  # Equivalente as duas linhas anteriores
    print('Distância de dois pontos: ', p2.distancia_dois_pontos(p3))  # nome_objeto.nome_metodo(argumento)
    print('Distância de dois pontos: ', p2.distancia_dois_pontos(p4))  # nome_objeto.nome_metodo(argumento)