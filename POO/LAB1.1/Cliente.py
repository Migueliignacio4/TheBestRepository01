from Persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, fechaNacimiento, rut,password,productos):
        super().__init__(nombre, fechaNacimiento, rut)
        self.password = password
        self.productos = productos

    #get y set
    def getPassword(self):
        return self.password
    def setPassword(self,new_pass):
        if len(new_pass) == 10:
            self.password = new_pass
        else:
            print("Tienes que ingresar una password de 10 caracteres")

    def getProductos(self):
        return f""" Productos: {self.productos}"""
    def setProductos(self,new_producto):
        self.productos = new_producto