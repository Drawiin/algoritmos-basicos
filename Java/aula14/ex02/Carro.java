package aula14.ex02;

public class Carro implements Motor{
    private boolean ligado;

    @Override
    public void ligar() {
        this.ligado = true;
    }

    @Override
    public void desligar() {
        this.ligado = false;

    }
}
