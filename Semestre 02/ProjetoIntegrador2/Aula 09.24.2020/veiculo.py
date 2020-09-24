class Veiculo:
    def __init__(self, modelo, ano, valor):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def get_modelo(self):
        return self.modelo
    
    def set_modelo (self, novo_modelo):
        self.modelo = novo_modelo

    def get_ano(self):
        return self.ano
    
    def set_ano (self, novo_ano):
        self.ano = novo_ano
    
    def get_valor(self):
        return self.valor
    
    def set_valor (self, novo_valor):
        #if novo_valor > 0:
        self.valor = novo_valor
        #else:
        #    print("Valor inválido.")
            
    def mostrar_dados (self):
        print('Modelo: ', self.modelo)
        print('Ano: ', self.ano)
        print("Valor: ", self.valor)
    
    def comparar_valor (self, outro_objeto):
        if self.valor > outro_objeto.valor:
            print("Valor veículo 1", self.valor)
        else:
            print("Veículo 2", outro_objeto.valor)

if __name__ == '__main__':
    veiculo1 = Veiculo('onix',2019,52000)
    veiculo2 = Veiculo('cruze',2017,89000)
    #print(veiculo1.get_modelo())
    #novo_valor = float(input("Novo valor: "))
    #veiculo1.set_valor(novo_valor)
    #print(veiculo1.get_valor())
    print(veiculo1.mostrar_dados())
    veiculo1.comparar_valor(veiculo2)