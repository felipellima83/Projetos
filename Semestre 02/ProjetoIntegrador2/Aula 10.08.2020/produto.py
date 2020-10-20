class Produto (object):

    def __init__ (self, nome, vlr_compra=0.0, vlr_venda=0.0, qnt_estoque=0, qnt_minima=0):
        self.nome = nome
        self.vlr_compra = vlr_compra
        self.vlr_venda = vlr_venda
        self.qnt_estoque = qnt_estoque
        self.qnt_minima = qnt_minima

    def  get_nome(self):
        return self.nome
    
    def set_nome (self, novo_nome):
        self.nome = novo_nome
    
    def get_vlr_compra(self):
        return self.vlr_compra
    
    def set_vlr_compra (self, novo_vlr_compra):
        self.vlr_compra = novo_vlr_compra
    
    def get_vlr_venda (self):
        return self.vlr_venda

    def set_vlr_venda (self, novo_vlr_venda):
        self.vlr_venda = novo_vlr_venda
    
    def get_qnt_estoque (self):
        return self.qnt_estoque
    
    def set_atualiza_qnt_estoque (self, atualiza_qnt_estoque):
        self.qnt_estoque -= atualiza_qnt_estoque
    
    def repor_produto (self, qnt_comprada):
        self.qnt_estoque += qnt_comprada
    
    def get_qnt_minima (self):
        return self.qnt_minima
    
    def set_qnt_minima (self, novo_qnt_minima):
        self.qnt_minima = novo_qnt_minima

    def lucro (self):
        lucro = self.get_vlr_venda() - self.get_vlr_compra()
        return lucro
    
    def alerta_compra (self):
        if self.get_qnt_estoque() <= self.get_qnt_minima():
            ret = True
        else:
            ret = False
        return ret
    
    def maior_qnt (self, ):
        pass

    def maior_lucro (self):
        pass

    def __str__(self):
        dados = "Nome: {}\nValor de Compra: {}\nValor de Venda: {}\nQnt no Estoque: {}\nQnt Mínima: {}".format(self.nome,self.vlr_compra,self.vlr_venda,self.qnt_estoque,self.qnt_minima)
        return dados


if __name__ == "__main__":
    produto1 = Produto("Arroz", 15.00, 19.50, 67, 7)
    print(produto1)
    print(produto1.get_nome())
    print(produto1.get_qnt_estoque())
    produto1.set_atualiza_qnt_estoque(5)                 #Reduz a quantidade do estoque
    print(produto1.get_qnt_minima())
    print(produto1.lucro())
    if produto1.alerta_compra():
        print("Comprar")
    else:
        print("Não comprar")
    print("Comprar") if produto1.alerta_compra() else print("Não Comprar")      #Operador ternário, mesmo q anterior
    print("Qual o nome do produto: ")
    produto2 = Produto("Feijão")
    print(produto2)
    novo_produto = input("Qual o nome do novo produto: ")
    produto3 = Produto(novo_produto, qnt_estoque=55)
    produto3.set_atualiza_qnt_estoque(5)
    print(produto3)
    produto4 = Produto("Farinha", qnt_estoque=20)
    print(produto4)
        