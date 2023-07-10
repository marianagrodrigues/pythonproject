#treino de POO
class Produto:
    def __init__(self, produto, cod=0, preco=0.0, estAtual=0, estMin=0, estMax=0):
        self.produto = produto
        self.cod = cod
        self.preco = preco
        self.estAtual = estAtual
        self.estMin = estMin
        self.estMax = estMax

    def exibir(self):
        print(self.produto)

p1 = Produto("mouse", 1, 15.99, 100, 25, 200)