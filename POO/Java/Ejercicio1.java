import java.util.Scanner;

public class Ejercicio1 {

    static int potencia(int base, int exp){
        int pot = 1;
        for(; exp > 0; exp--)
            pot *= base;
        return pot;
    }
    
    public static void main(String[] args){
        try (Scanner lector = new Scanner(System.in)) {
            System.out.println("Ingrese la Base: ");
            int b = lector.nextInt();
            System.out.println("Ingrese el Exponente: ");
            int exp = lector.nextInt();

            int resultado = potencia(b, exp);

            System.out.println("La potencia es: " + resultado);
        }
    }
}