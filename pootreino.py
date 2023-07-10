"""Banco"""
class ContaCorrente:
    def _init_(self,titular, saldo=0.0, ag=0, nConta=0):
        self.titular = titular
        self.saldo = saldo
        self.ag = ag
        self.nConta = nConta
    def exibirSaldo(self):
        print(f"titular: {self.titular}\nSaldo: R$ {self.saldo}")
    def depositar(self,valor):
        self.saldo = self.saldo + valor
    def sacar(self,valor):
        if valor<=self.saldo:
            self.saldo = self.saldo - valor
        else:
            print("Saldo insuficiente")
    def transferir(self,destino, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo = self.saldo - valor
            destino.saldo = destino.saldo + valor
        print("Transferência realizada com sucesso!")
print("____________")

conta1 = ContaCorrente("karol", 4500, 13, 1013)
conta2 = ContaCorrente("pedro", 1000, 15, 20104)
conta3 = ContaCorrente("jorge", 2500, 53, 89523)
conta4 = ContaCorrente("ana", 5500, 98, 5641)

conta1.transferir(conta2, 1000)
conta2.exibirSaldo()