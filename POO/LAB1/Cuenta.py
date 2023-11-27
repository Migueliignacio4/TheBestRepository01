class Cuenta():
    def __init__(self, titular,saldo,movimientos):
        self.titular = titular
        self._saldo = saldo
        self.movimientos = movimientos
    
    def getSaldo(self):
        return self._saldo
    def deposito(self,dep):
        if dep > 0:
            self._saldo = dep
        else:
            print("solamente se pueden hacer depositos con montos mayores a 0")
    def retiro(self,ret):
        if ret > self._saldo and ret <= 0:
            print("No puede retirar montos que sean mayores a la cantidad de su cuenta")
        else:
            self._saldo = self._saldo - ret
    def __to_string__(self):
        return f"""Su cuenta\n Titular: {self.titular}\n Saldo: {self._saldo}\n Movimientos: {self.movimientos}   """
        
    #def registrarMovimiento():