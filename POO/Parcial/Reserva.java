public class Reserva extends Paciente {
    protected String fecha, hora;

    public Reserva(String rut, int creditCard, String nombre, String fecha, String hora){
        super(rut, creditCard, nombre);
        this.fecha = fecha;
        this.hora = hora;
    }

    public void crearReserva(String fecha, String hora, String nombrePa, String rutPa, String drName){
        System.out.println("Se creó una reserva. El día: "+ fecha + "A la hora: " + hora + "\n Nombre del paciente: " + nombrePa + "\n Rut del Paciente: " + rutPa + "\n Agendado con el doctor: " + drName);
        
    }
    
    
}