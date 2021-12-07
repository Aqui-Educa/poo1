from calculadora import Multiplica

class Imposto:

    def __init__(self):
        self.aliquota = 0

    def CalculaImposto(self, valorProduto):
        valorImposto = Multiplica(valorProduto, self.aliquota)  
        return valorImposto + valorProduto