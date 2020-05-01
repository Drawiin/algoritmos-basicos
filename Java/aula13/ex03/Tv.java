package aula13.ex03;

public class Tv extends Eletrodomestico{
    private int tamanho;
    private int canal;
    private int volume;

    Tv(int voltagem, int tamanho) {
        super(false, voltagem);
        this.tamanho = tamanho;
        this.canal = 0;
        this.volume = 0;
    }


    @Override
    public void ligar() {
        if (getLigado()){
            System.out.println("Tv já está ligada");
        }else{
            setLigado(true);
            System.out.println("A tv agora está ligada");
        }
    }

    @Override
    public void desligar() {
        if (!this.getLigado()){
            System.out.println("Tv já desligada");
        }else{
            this.setLigado(false);
            System.out.println("Tv desluigada");
        }
    }
}
