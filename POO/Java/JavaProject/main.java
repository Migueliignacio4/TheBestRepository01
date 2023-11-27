package JavaProject;
public class main{
    public static void main(String[] args) {
        Cuadrilatero c2 = new Cuadrilatero(1, 2, 3, 4, 5, 6, 7, 8);
        

        
        cuadrado c3 = new cuadrado(0, 5, 0, 5, 0, 0, 5, 5);
        c3.metarea();

        trapecio c4 = new trapecio(0, 0, 0, 0, 0, 0, 0, 0);
        c4.metarea();

        rectangulo c5 = new rectangulo(0, 10, 0, 10, 0, 0, 5, 5);
        c5.metarea();
    }

    
}