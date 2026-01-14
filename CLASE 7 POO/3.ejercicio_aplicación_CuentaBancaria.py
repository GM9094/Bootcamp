class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, cantidad):
        self.saldo += cantidad #adiciona a saldo la cantidad ingresada

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad #resta cantidad al saldo actual      
        else: 
            print("saldo insuficiente, ingrese monto menor")
    
    def mostrar_info(self):
        return f"Nombre: {self.titular}, saldo: {self.saldo}"
    
    
#ver problema de ingresar montos negativos
#por incluir metodo de transferencias
c1 = CuentaBancaria("Leeloo", 1000)
print(c1.mostrar_info())
c1.depositar(1000)
print(c1.mostrar_info())
c1.retirar(2000)
print(c1.mostrar_info())
c1.depositar(1000)
print(c1.mostrar_info())
c1.retirar(4000)
print(c1.mostrar_info())