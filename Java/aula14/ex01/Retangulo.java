package aula14.ex01;

public class Retangulo implements ElementoDiagrama{
    private double comprimento;
    private double altura;

    Retangulo(double comprimento, double altura){
        this.comprimento = comprimento;
        this.altura = altura;
    }

    @Override
    public void desenhar() {
        System.out.println("+----+");
        System.out.println("|    |");
        System.out.println("|    |");
        System.out.println("+----+");
    }

    @Override
    public void redimensionar() {
        this.altura *= 2;
        this.comprimento *= 2.5;
    }
}
