package aula13.ex03;

public class Radio extends Eletrodomestico{
    private double sintonia;
    private int volume;


    Radio(int voltagem) {
        super(false, voltagem);
        this.sintonia = 0.0;
        this.volume = 0;
    }

    @Override
    public void ligar() {
        if (getLigado()){
            System.out.println("Rádio já está ligado");
        }else{
            setLigado(true);
            System.out.println("O Rádio agora está ligado");
        }
    }

    @Override
    public void desligar() {
        if (!this.getLigado()){
            System.out.println("Rádio já desligado");
        }else{
            this.setLigado(false);
            System.out.println("Rádio desligado");
        }
    }
}
