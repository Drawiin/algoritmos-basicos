package aula14.ex01;

public class Circulo implements ElementoDiagrama{
    private double raio;

    Circulo(double raio){
        this.raio = raio;
    }

    @Override
    public void desenhar() {
        System.out.println("()");
    }

    @Override
    public void redimensionar() {
        this.raio *= 2;
    }
}
