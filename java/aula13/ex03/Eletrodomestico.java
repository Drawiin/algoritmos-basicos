package aula13.ex03;

public abstract  class Eletrodomestico {
    private boolean ligado;
    private int voltagem;

    public boolean getLigado(){
        return this.ligado;
    }

    public int getVoltagem() {
        return voltagem;
    }

    public void setLigado(boolean ligado) {
        this.ligado = ligado;
    }

    public void setVoltagem(int voltagem) {
        this.voltagem = voltagem;
    }

    Eletrodomestico(boolean ligado, int voltagem){
        this.ligado = ligado;
        this.voltagem = voltagem;
    }

    public abstract void ligar();
    public abstract void desligar();
}
