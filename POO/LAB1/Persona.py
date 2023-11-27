class Persona:
    def __init__(self, nombre, fechaNacimiento, rut):
        self.nombre = nombre
        self.fechaNacimiento = fechaNacimiento
        self.rut = rut

    #Get y set
    def getNombre(self):
        return self.nombre
    def setNombre(self,new_nombre):
        self.nombre = new_nombre
    
    def getFechaNacimiento(self):
        return self.fechaNacimiento
    def setFechaNacimiento(self,new_fecha):
        self.fechaNacimiento = new_fecha
    
    def getRut(self):
        return self.rut
    def setRut(self,new_rut):
        if
        self.rut = new_rut
    
    def toString():
        print("Organiza informacion de la persona")

    def esMayorDeEdad(self):
        if (self.fechaNacimiento - 2023) >= 18:
            print("es mayor de edad.")
        else:
            print("es menor de edad.")