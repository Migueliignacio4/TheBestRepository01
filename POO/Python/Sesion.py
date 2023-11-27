from Dispositivo import Dispositivo

class Sesion:
    def __init__(self, id, nombreAsignatura, nombreProfesor, sala, fechaClase, horaInicio, horaFinal, camaraUsada, listaCamaras):
        self.id = id
        self.nombreAsignatura = nombreAsignatura
        self.nombreProfesor = nombreProfesor
        self.sala = sala
        self.fechaClase = fechaClase
        self.horaInicio = horaInicio
        self.horaFinal = horaFinal
        self.camaraUsada = camaraUsada
        self.listaCamaras = listaCamaras





    def iniciarTransmision(self):
        print(self.id +" || Iniciado la transmision...")

    def transmisionEnCurso(self):
        print("SesionID: " + self.id, "   ||   Docente: " + self.nombreProfesor, "   ||   Sala: " + self.sala, "\nAsignatura: " + self.nombreAsignatura, "   ||   Camara en uso: " + self.camaraUsada, "\nHora Inicio: " + self.horaInicio, "   ||   Hora Final: " + self.horaFinal)
        print("\n ")

    def terminarTransmision(self):
        print(self.id + " transmisión finalizada...")

    def cambiarCamara(self):
        print("Seleccione una de estas cámaras: ", self.listaCamaras)