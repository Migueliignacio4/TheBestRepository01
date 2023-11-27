from Sesion import Sesion
from Camara import Camara
from Dispositivo import Dispositivo


if __name__ == "__main__":

    Cam1 = Dispositivo("CAM001", 100, "2160p", "SONY", "Camara de grabacion digital")
    Cam2 = Dispositivo("CAM002", 200, "1080p", "CANON", "Camara reflex")
    Cam3 = Dispositivo("CAM003", 300, "1440p", "Olympus", "Camara de videoconferencias")
    Cam4 = Dispositivo("CAM004", 400, "720p", "Logitech", "Webcam")
    Cam5 = Dispositivo("CAM005", 500, "1080p", "iPhone", "Camara de Telefono")       


    comando = int(input("MENU PRINCIPAL — ULAGOSCAM\n1. Crear una Sesion.\n2. Salir.\n"))

    if comando == 1:
        print("CREANDO SESION — ULAGOSCAM\nRellene los datos pedidos...\n ")
        sesionAsignatura = input("Ingrese la asignatura: ")
        sesionProfesor = input("Ingrese nombre del docente: ")
        sesionSala = input("Ingrese la sala: ")
        sesionFecha = input("Ingrese la fecha: ")
        sesionHoraInicio = input("Ingrese la hora de inicio: ")
        sesionHoraFinal = input("Ingrese la hora en que finaliza: ")     
    elif comando == 2:
        print("Muchas gracias por utilizar ULAGOSCAM. Hasta luego.")
    else:
        print("Ingrese una opción valida. [1 or 2]")

    listaCamaras = [f"\nCámara: {Cam1.nombre} Modelo: {Cam1.modelo}", f"\nCámara: {Cam2.nombre} Modelo: {Cam2.modelo}", f"\nCámara: {Cam3.nombre} Modelo: {Cam3.modelo}", f"\nCámara: {Cam4.nombre} Modelo: {Cam4.modelo}", f"\nCámara: {Cam5.nombre} Modelo: {Cam5.modelo}"]
 

    sesionCreada = Sesion("ID" + sesionSala, sesionAsignatura, sesionProfesor, sesionSala, sesionFecha, sesionHoraInicio, sesionHoraFinal, Cam1.nombre, ", ".join(listaCamaras))

    iniciar = int(input("MENU SESION — ULAGOSCAM\nLa Sesion fue creada exitosamente...\n  1. Iniciar transmisión\n  2. Salir."))
    if iniciar == 1:
        
        sesionCreada.iniciarTransmision()
        Cam1.transmitir()
        while True:
            
            opcion2 = int(input("MENU SESION — ULAGOSCAM\n  1. Cambiar Camara.\n  2. Ver detalles de transmisión.\n  3.Finalizar Transmisión.\n"))
            if opcion2 == 1:
                sesionCreada.cambiarCamara()
                print("Elija una cámara:")
                for i, camara in enumerate(listaCamaras):
                    print(f"{i+1}: {camara}")

                while True:
                    try:
                        opcion = int(input("Ingrese el número de la cámara que desea: "))
                        if 1 <= opcion <= 5:
                            camara_seleccionada = listaCamaras[opcion - 1]
                            print(f"Ha seleccionado la siguiente cámara:\n{camara_seleccionada}")
                            break
                        else:
                            print("Ingrese un número válido (1-5).")
                    except ValueError:
                        print("Ingrese un número válido (1-5).")
            elif opcion2 == 2:
                print("Mostrando detalles...")
                sesionCreada.transmisionEnCurso()
            elif opcion2 == 3:
                sesionCreada.terminarTransmision()
                break
            else:
                print("Opcion no valida.")

    elif iniciar == 2:
        print("Gracias por haber utilizado ULAGOSCAM, se procede a cerrar y borrar su Sesión.")
    else:
        print("Opción Invalida.")


    


    #sesion1.iniciarTransmision()
    #sesion1.cambiarCamara()
    