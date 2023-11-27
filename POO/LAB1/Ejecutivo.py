from Persona import Persona
class Ejecutivo(Persona):
    def __init__(self, nombre, fechaNacimiento, rut,usuario,password):
        super().__init__(nombre, fechaNacimiento, rut)
        self.usuario = usuario
        self.password = password

    #get y set
    def getUsuario(self):
        return self.usuario
    def setUsuario(self,new_usuario):
        if len(new_usuario) == 10:
            self.usuario = new_usuario
        else:
            print("Tienes que ingresar un usuario de 10 caracteres")
        
    
    def getPassword(self):
        return self.password
    def setPassword(self,new_pass):
        if len(new_pass) == 10:
            self.password = new_pass
        else:
            print("Tienes que ingresar una password de 10 caracteres")
        