'''   UniCEUB   -   Ciência da Computação   -   Prof. Barbosa
Atalho de teclado: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha

      POO em Pytthon
class NomeClasse:
    def __init__ (self, p_1, p_2):                          # Método construtor
        self.nome_atributo1 = p_1
        self.nome_atributo2 = p_2
    def get_nome_atributo1 (self):           # Modelo do método get (consulta um atributo)
        return self.nome_atributo1
    def set_nome_atributo1 (self, valor): # Modelo do método set (altera valor de um atributo)
        self.nome_atributo1 = valor
    def outro_metodo (self):                      # Outros métodos da classe
        . . .
        [return ...]

if __name__ == '__main__':            # main <tab>
    nome_objeto1 = NomeClasse(a_1, a_2)  # Cria (instancia) o primeiro objeto da classe
    nome_objeto2 = NomeClasse(a_1, a_2)  # Cria (instancia) o segundo objeto da classe
    print ("Valor do atributo x: ", nome_objeto1.x) # nome_objeto . nome_atributo
------------------------------ Com base no modelo acima, implemente estes itens:

1- Crie a classe ContaCorrente, com estes atributos: titular, numero, saldo
- Crie o construtor da classe
3- Crie alguns métodos gets e sets.
- No main, crie o primeiro objeto da classe (primeira conta corrente) com estes dados: 'João', '123-4', 1000.00  
5- No main, consulte os dados do objeto criado. Ex.: nome_objeto.nome_metodo()
- Altere o número da conta corrente para 923-4. Ex.: nome_objeto.nome_metodo(valor). Teste
7- Refaça o método set_titular com crítica. Teste.
- Sobreescreva o método especial __str__ . Ele não recebe nada e retorna todos os atributos concatenados. Teste.
- Crie o método deposito, ele recebe um valor e acrescenta ao saldo. Faça crítica.
10- No main, realize um deposito. Verifique se o deposito foi bem-sucedido.
11- Crie o método retirada, ele recebe um valor e subtrai do saldo. Faça pelo menos duas crítica.
- No main, realize uma retirada. Verifique se a retirada foi bem-sucedido.
13- Verifique se o correntista realizou o saque. O nétodo retirada retorna um valor boolean.
14- Crie a conta2 (segundo objeto) com o titular e o número da conta. Teste
15- Crie a conta3 (terceiro objeto) com o titular e o saldo. Teste
16- Transferência entre duas contas quaisquer, crie o método transfere_para com crítica. Teste
17- Acrescente esta regra de negócio a transferência: quem faz a transferência paga uma tarifa de 5 reais.
18- O banco também quer controlar a quantidade de contas existentes no sistema.
  Crie o atributo de classe qtd_conta com o objetivo de armazenar a quantidade de contas existente.
19- Como o atributo de classe será atualizado?
20- Crie o método de classe mostra_qtd_conta, ele mostra o valor desse atributo de classe. Teste
21- Crie o método de classe get_qtd_conta, ele retorna o valor desse atributo de classe. Teste
-- '''

class ContaCorrente(object):
    qtd_conta = 0                               # Atributo de classe
    @classmethod                                # Com método de classe com decorator
    def mostra_qtd_conta(cls):                  # o parametro é a propria classe
        print(f'{cls.qtd_conta} conta(s) no sistema')
    @classmethod                                # Uso de decorator
    def get_qtd_conta(cls):                     # o parametro é a propria classe
        s = f'{cls.qtd_conta} conta(s) no sistema'
        return s
    def __init__(self, tit, num=0, saldo=0.0):      # Construtor com valor default
        self.titular = tit                          # Atributos de instância
        self.numero = num
        self.saldo = saldo
        ContaCorrente.qtd_conta += 1                # Atualizo o atributo de classe
        # self.limite = limite
    def get_titular(self):                          # Métodos gets e sets
        return self.titular
    # def set_titular(self, p_nome):                  # Sem crítica
    #     self.titular = p_nome
    def get_numero(self):                           # Consulta
        return self.numero
    def set_numero(self, v):                        # Altera
        self.numero = v
    def get_saldo(self):
        return self.saldo
    def set_titular(self, p_nome):                  # Com crítica
        if isinstance(p_nome, str):                 # Verifica se p_nome é uma string (True ou False)
            self.titular = p_nome
        else:
            print('Erro: nome deve ser string.')
    def __str__(self):                              # Método especial ou mágico ou dunder
        # s = '- Nome: ' + self.titular + '\nNúmero: ' + self.numero + '\nSaldo: ' + str(self.saldo) # Linhas equivalentes.
        # s = "- Nome: {}\nNúmero: {}\nSaldo: {:.2f}" .format(self.titular, self.numero, self.saldo)
        s = f'- Nome: {self.titular}\nNumero: {self.numero}\nSaldo: {self.saldo:.2f}'
        return s
        # return f'Nome: {self.titular}\nNumero: {self.numero}\nSaldo: {self.saldo}'    # Solução 2
    # def deposito(self, valor):                    # Sem crítica
    #    self.saldo += valor
    def deposito(self, valor):                      # Com crítica
        if valor <= 0:
            print('Valor inválido.')
        else:
            self.saldo += valor
            # ContaCorrente.total += valor
    # def retirada(self, valor):                    # Sem crítica
    #     self.saldo = self.saldo - valor
    def retirada(self, valor):                      # Com crítica. saque
        if valor > self.saldo:
            print("Saldo insuficiente.")
            ok = False
        elif valor < 0:                             # Se torna um depósito
            print('Valor inválido.')
            ok = False
        else:
            self.saldo = self.saldo - valor
            ok = True
        return ok
    def transfere_para(self, destino):
        vlr_transacao = float(input('Valor da transferência: '))    # vlr_transacao = 10
        # Verifica se pode fazer retirada (saque)
        # deposito  ou   msg erro
        taxa = 5
        retirou = self.retirada(vlr_transacao + taxa)
        if retirou == False:                        # if not retirou:
            print("Transferência não realizada.")
        else:
            destino.deposito(vlr_transacao)
            print("Transferência realizada.")


if __name__ == '__main__':
    print('Contas', ContaCorrente.mostra_qtd_conta())
    conta1 = ContaCorrente('João', '123-4', 1000.00)    # Cria o objeto conta1.
    print('Contas', ContaCorrente.mostra_qtd_conta())
    print ("Titular:", conta1.get_titular())
    conta1.set_numero('923-4')
    print(conta1)                                       # print(conta1.__str__())
    conta1.deposito(120.00)
    print(conta1)                                       # print(conta1.__str__())
    conta1.deposito(-20.00)                             # Testando o método depósito com valor negativo.
    print(conta1)
    conta1.retirada(200.00)
    print(conta1)
    conta2 = ContaCorrente('João', '123-4')             # Cria o objeto conta2.
    conta3 = ContaCorrente('Rogério', saldo=1000)       # Cria o objeto conta2.
    print(conta1)                                       # print(conta1.__str__())
    print(conta2)
    print(conta3)
    conta1.transfere_para(conta2)
    print(conta1)
    print(conta2)
    ContaCorrente.mostra_qtd_conta()                    # nome_classe.nome_metodo_classe()
    print('Contas', ContaCorrente.get_qtd_conta())      # nome_classe.nome_metodo_classe()
