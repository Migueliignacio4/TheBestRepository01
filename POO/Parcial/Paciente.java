public class Paciente {
    protected int creditCard;
    protected String nombre, rut;

    public Paciente(String rut, int creditCard, String nombre){
        this.rut = rut;
        this.creditCard = creditCard;
        this.nombre = nombre;

    }
}
