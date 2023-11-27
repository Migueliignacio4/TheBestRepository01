class Camara:
    def __init__(self, nombre, id, resolucion):
        self.nombre = nombre
        self.id = id
        self.resolucion = resolucion


    def transmitir(self, USCAM=None):
        print("Trasnmitiendo con " + USCAM, "a " + self.resolucion)