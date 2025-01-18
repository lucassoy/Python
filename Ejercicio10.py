class CuentaBancaria:
    def __init__(self,numero,name,saldo):
        self.numero = numero
        self.name = name
        self.saldo = saldo
    def depositar(self,cantidad):
        self.saldo += cantidad
    def retirar(self,cantidad):
        if cantidad > self.saldo:
            print("No tienes suficiente dinero")
        else:
            self.saldo -= cantidad

c1 = CuentaBancaria(1234,"Lucas",1000)
c2 = CuentaBancaria(5678,"Juan",1000)
for c in [c1,c2]:
    print(c.numero, c.name, c.saldo)
    print("")
c1.depositar(500)
c2.depositar(1000)
for c in [c1,c2]:
    print(c.numero, c.name, c.saldo)
    print("")
c1.retirar(5000)
c2.retirar(1000)
for c in [c1,c2]:
    print(c.numero, c.name, c.saldo)
    print("")
