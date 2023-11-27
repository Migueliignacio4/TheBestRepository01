from Camara import Camara

class Dispositivo(Camara):
    def __init__(self, nombre, id, resolucion, marca, modelo):
        super().__init__(nombre, id, resolucion)
        self.marca = marca
        self.modelo = modelo

