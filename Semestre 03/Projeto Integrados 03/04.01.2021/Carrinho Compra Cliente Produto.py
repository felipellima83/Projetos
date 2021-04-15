"""   CEUB   -   Bacharelado em Ciência da Computação   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.

- Usando o conceito de associação de classes em POO, faça a análise das classes necessárias
para desenvolva um sistema de carrinho de compras com as informações do cliente e
dos produtos colocados no carrinho.

Implemente:
1- Crie a classe Cliente com os atributos (características) identidade e nome
- Crie os métodos gets
- Crie a classe CarrinhoCompra com os atributos número do pedido,o cliente e os produtos, teste.
- Crie os métodos gets, teste
5- Crie a classe Produto com os atributos:
  identificador, descrição, preço e quantidade.
- Crie os métodos gets, teste
- Crie o método __str__ pra retornar todos os dados de um produto formatados (concatenados)
8- Crie o método mostra carrinho, teste
- Insira um produto no carrinho de compras do cliente1,
  Crie o método insere_produto, ele recebe um objeto da classe Produto e insere no carrinho, teste.
10- Insira mais um produto no carrinho de compras do cliente1, teste
- Crie o método mostra_carrinho2, com todos os dados do produto e a quantidade de itens no carrinho.
  Se o carrinho estiver vazio, mostre a mensagem "Carrinho vazio". Teste
- Crie o método retorna_total, ele calcula e retorna o valor total da compra,
  ou seja, dos produtos no carrinho de compras, teste  (valor total 57,00)
13- Crie o método remova_produto, ele remove um produto do carrinho de compras, teste
- Crie o método remova_produto2, ele remove um produto do carrinho de compras
  com críticas e mensagens, teste
15- Insira mais um produto no carrinho de compras do cliente1, teste
- Crie o método fecha_compra. Ele finalize a compra e mostra os produtos e o
  valor total, teste
- Crie o método remova_produto3, ele não recebe nada, mostre todos os produtos no carrinho,
  o cliente escolhe o produto para remover e remove o produto do carrinho de compras, teste
- Finalize a compra e feche o carrinho 2. Além de mostrar os produtos e o valor total
  Mostrar também o número de pedido, o nome do cliente, a data e hora, teste
19- Altere quantidade de um determinado produto no carrinho de compras, o método altera_qtd
    recebe o produto e lê a nova quantidade, teste
20- Altere quantidade de um determinado produto no carrinho de compras, o método altera_qtd2
    Não recebe nada, mostra todos os produtos, o usuário escolhe o produto, lê a nova quantidade
    e insere a nova quantidade desse produto, teste
21 – Para evitar código repetido em vários métodos, crie um método para verificar se
o carrinho de compra está vazio, se estiver vazio ele mostra a mensagem “Carrinho vazio”
e retorna True, senão retorna False.
Chame o método carrinho_vazio no início dos métodos que precisar verificar      """
from datetime import datetime
class CarrinhoCompra(object):                       # class CarrinhoCompra:
    def __init__(self, num_pedido, o_cliente):
        self.num_pedido = num_pedido
        self.cliente = o_cliente
        self.produtos = list()              # self.produtos = []
    def get_num_pedido(self):
        return self.num_pedido
    def get_cliente_nome(self):             # Redundante, não precissa
        return self.cliente.get_nome()
    def mostra_carrinho(self):
        print('- Mostra carrinho:')
        for produto in self.produtos:
            print('Descirção:', produto.get_descricao())
    def insere_produto(self, o_produto):
        self.produtos.append(o_produto)
    def mostra_carrinho2(self):
        qtd = len(self.produtos)
        # if qtd == 0:
        if not self.produtos:       # if self.produtos == []
            print('Carrinho vazio')
        else:
            print('Mostra carrinho 2:')
            for o_produto in self.produtos:
                print(o_produto)                  # print(o_produto.__str__())
            print('Quantidade de itens:', qtd)
    def retorna_total(self):
        total = 0
        for o_produto in self.produtos:
            total += o_produto.get_preco() * o_produto.get_qtd()
        return total
    def remove_produto(self, o_produto):        # Sem crítica
        self.produtos.remove(o_produto)
    def remove_produto2(self, o_produto):       # Com crítica
        if o_produto in self.produtos:          # Operador in
            self.produtos.remove(o_produto)
            print('Produto removido')
        else:
            print('Produto não está no carrinho')
    def fecha_carrinho(self):               # Falta verificar se o carrinho está vazio
        print('Finalizando a compra 1, produtos:')
        self.mostra_carrinho2()
        print('Total R$', self.retorna_total())
    def remove_produto3(self):
        # qtd = len(self.produtos)                  # Solução 1, lista vazia?
        # if qtd == 0:
        # if self.produtos == []                    # Solução 2
        if not self.produtos:                       # Solução 3
            print('Carrinho vazio')
        else:
            self.mostra_carrinho2()
            indice = int(input("Posição do produto para remover: "))
            # self.produtos.pop(indice)             # Sem crítica
            if 0 <= indice < len(self.produtos):    # Com crítica
                self.produtos.pop(indice)
                print('Produto removido.')
            else:
                print('Produto não está no carrinho.')
    def fecha_carrinho2(self):
        # qtd = len(self.produtos)                  # Solução 1, lista vazia?
        # if qtd == 0:
        # if self.produtos == []                    # Solução 2
        if not self.produtos:                       # Solução 3
            print('Carrinho vazio')
        else:
            print('Finalizando a compra 2:')
            print('Data e horário:', datetime.today())          # Data e hora juntos
            print('Data e horário:', datetime.now())
            print('Data:', datetime.today().date())             # Só data
            print('Horário:', datetime.today().time())          # Só horas
            print('Número pedido:', self.get_num_pedido())
            print('Identidade:', self.cliente.get_identidade())
            print('Cliente:', self.cliente.get_nome())
            # print('Cliente:', self.get_cliente_nome())        # Equivalente a linha anterior
            self.mostra_carrinho2()
            print('Total R$', self.retorna_total())
    def altera_qtd(self, o_produto):
        # nova_qtd = int(input("Nova quantidade: "))
        # o_produto.set_qtd(nova_qtd)                      # Sem crítica.
        if o_produto in self.produtos:                     # Com crítica
            nova_qtd = int(input("Nova quantidade: "))
            o_produto.set_qtd(nova_qtd)
            print("Alteração realizada.")
        else:
            print('Produto não está no carrinho.')
    def altera_qtd2(self):
        # qtd = len(self.produtos)                  # Solução 1, lista vazia?
        # if qtd == 0:
        # if self.produtos == []                    # Solução 2
        if not self.produtos:                       # Solução 3
            print('Carrinho vazio')
        else:
            self.mostra_carrinho2()
            indice = int(input("Posição do produto para alterar: "))
            if 0 <= indice < len(self.produtos):            # Com crítica
                o_produto = self.produtos[indice]           # Notação de vetor
                nova_qtd = int(input("Nova quantidade: "))
                o_produto.set_qtd(nova_qtd)
                # self.produtos[indice].set_qtd(nova_qtd)       # Equivalente as duas linhas anteriores
                print('Produto alterado')
            else:
                print('Produto não está no carrinho')


class Cliente:
    def __init__(self, identidade, nome):
        self.identidade = identidade
        self.nome = nome

    def get_identidade(self):
        return self.identidade

    def get_nome(self):
        return self.nome


class Produto(object):
    def __init__(self, idt, descricao, preco=0.0, qtd=1):
        self.idt = idt
        self.descricao = descricao
        self.preco = preco
        self.qtd = qtd

    def get_descricao(self):
        return self.descricao

    def get_preco(self):
        return self.preco

    def get_qtd(self):
        return self.qtd

    def set_qtd(self, nova_qtd):
        self.qtd = nova_qtd

    def __str__(self):
        dados = f'Idt: {self.idt}, descrição: {self.descricao}, preço: {self.preco} e qtd: {self.qtd}'
        return dados


if __name__ == '__main__':
    cliente1 = Cliente(123, 'Ailton')           # Chama o contrutor da classe Cliente
    carrinho1 = CarrinhoCompra(12, cliente1)    # carrinhoCompra(num_pedido, objeto da classe Cliente)
    print('Número:', carrinho1.get_num_pedido())
    print('Nome:', carrinho1.get_cliente_nome())
    carrinho1.mostra_carrinho()                 # O carrinho está vazio
    p1_arroz = Produto(1, 'Arroz', 30.0)        # Chama o construtor da classe Produto
    carrinho1.insere_produto(p1_arroz)          # Chama o método passando o objeto da classe Produto
    carrinho1.mostra_carrinho()
    p2_feijao = Produto(2, 'Feijão', 9.00, 3)
    carrinho1.insere_produto(p2_feijao)
    carrinho1.mostra_carrinho()
    carrinho1.mostra_carrinho2()
    # Teste, valor total 57,00
    print('Valor total R$:', carrinho1.retorna_total())
    carrinho1.remove_produto2(p2_feijao)        # Teste sem erro
    carrinho1.remove_produto2(cliente1)         # Teste com erro
    carrinho1.mostra_carrinho2()
    p3_farinha = Produto(3, 'Farinha', 5.00, 2)
    carrinho1.insere_produto(p3_farinha)
    carrinho1.mostra_carrinho2()
    carrinho1.fecha_carrinho()
    carrinho1.remove_produto3()
    carrinho1.mostra_carrinho2()
    carrinho1.fecha_carrinho2()
    carrinho1.altera_qtd(p1_arroz)
    carrinho1.mostra_carrinho2()
    print('carrinho1.retorna_total():', carrinho1.retorna_total())
    carrinho1.altera_qtd2()
    carrinho1.mostra_carrinho2()
    print('carrinho1.retorna_total():', carrinho1.retorna_total())