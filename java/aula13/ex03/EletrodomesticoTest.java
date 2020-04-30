package aula13.ex03;

public class EletrodomesticoTest {
    public static void main(String[] args) {
        Tv tv = new Tv(127, 52);
        tv.ligar();
        tv.ligar();
        tv.desligar();
        tv.desligar();

        Radio radio = new Radio(227);
        radio.ligar();
        radio.ligar();
        radio.desligar();
        radio.desligar();
    }
}
