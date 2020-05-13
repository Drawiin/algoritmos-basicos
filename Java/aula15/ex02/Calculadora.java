package aula15.ex02;

public class Calculadora {
    public double soma(double number1, double number2){
        return number1 + number2;
    }
    public double multiplicacao(double number1, double number2){
        return number1 * number2;
    }
    public double subtracao(double number1, double number2){
        return number1 - number2;
    }
    public double divisao(double number1, double number2){
        return number1/number2;
    }
    public double raiz(double number1){
        return Math.sqrt(number1);
    }
    public double inverso(double number1){
        return -number1;
    }
    public double potencia(double number1, double number2){
        return Math.pow(number1, number2);
    }
}
