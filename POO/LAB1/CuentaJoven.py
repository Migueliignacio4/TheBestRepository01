class CuentaJoven():
    def __init__(self, titular, saldo, movimientos, bonificacion):
        super().__init__(titular, saldo, movimientos)
        self.bonificacion = bonificacion

    
    def getBonus(self):
        return self.bonificacion