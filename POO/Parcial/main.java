import java.util.Scanner;

public class main {
    public static void main(String[] args) {


        ProfesionalSalud dr1 = new ProfesionalSalud(001, "Eduardo Lopez", "Medicina General");
        ProfesionalSalud dr2 = new ProfesionalSalud(002, "Pablo Escobar", "Medicina General");




        Scanner lector = new Scanner(System.in);


        System.out.println("Ingresó al menu de agendar una hora medica, seleccione la especialidad: \n 1. Medicina General");
        System.out.println("Ingrese la opción ");
        int b = lector.nextInt();
        
        if (b == 1) {
            System.out.println("Necesitamos que ingrese los datos del paciente. ");
            System.out.println("Nombre del Paciente: ");
            String namePa = lector.nextLine();
            System.out.println("Ingrese su rut: ");
            String rutPa = lector.nextLine();

            System.out.println("Tenemos los siguientes doctores disponibles para esa especialidad, seleccione uno: ");
            System.out.println("\n 1. Dr." + dr1.nombre + "\n 2. Dr." + dr2.nombre);
            int c = lector.nextInt();
            if (c == 1){
                System.out.println("¿Qué dia desea agendar su hora? Ej: 10 Octubre");
                String diaAgend = lector.nextLine();

                System.out.println("Ingrese la hora en la que desea su hora ej: 10:30");
                String horaAgend = lector.nextLine();

                Reserva r01 = new Reserva(rutPa, 020202, namePa, diaAgend, horaAgend);
                r01.crearReserva(diaAgend, horaAgend, namePa, rutPa, dr1.nombre);

            }else if (c == 2){
                System.out.println("¿Qué dia desea agendar su hora? Ej: 10 Octubre");
                String diaAgend = lector.nextLine();

                System.out.println("Ingrese la hora en la que desea su hora ej: 10:30");
                String horaAgend = lector.nextLine();
                
                Reserva r01 = new Reserva(rutPa, 020202, namePa, diaAgend, horaAgend);
                r01.crearReserva(diaAgend, horaAgend, namePa, rutPa, dr2.nombre);
            }else{
                System.out.println("Ingrese una opción valida.");
            }
            
        }else{
            System.out.println("Ingrese opcion valida.");
        }


    }
}
