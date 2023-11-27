package JavaProject;

public class rectangulo extends Cuadrilatero {

    public rectangulo(int x1, int x2, int x3, int x4, int y1, int y2, int y3, int y4){
        super(x1, x2, x3, x4, y1, y2, y3, y4);
    }

    public void metarea(){
        System.out.println("Rectangulo area: " + (x2 - x1) * (y3 - y1));
    }
}