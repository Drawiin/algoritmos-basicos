package aula14.ex01;

public class Main {
    public static void main(String[] args) {
        Circulo circulo = new Circulo(12);
        Retangulo retangulo = new Retangulo(12, 5);
        circulo.redimensionar();
        retangulo.redimensionar();
        circulo.desenhar();
        retangulo.desenhar();
    }
}
