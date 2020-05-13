package aula16.ex01;

import java.io.DataInputStream;
import java.io.IOException;

public class CalculadoraTeste {
    public static void main(String[] args) {
        Calculadora calculadora = new Calculadora();
        DataInputStream teclado = new DataInputStream(System.in);
        try {
            System.out.println("Entre com o primeiro numero");
            String numero1 = teclado.readLine();
            System.out.println("Entre com o segundo numero");
            String numero2 = teclado.readLine();
            System.out.println("soma: " + calculadora.soma(Double.parseDouble(numero1), Double.parseDouble(numero2)));
            System.out.println("subtração: " + calculadora.subtracao(Double.parseDouble(numero1), Double.parseDouble(numero2)));
            System.out.println("multiplicaçãp: " + calculadora.multiplicacao(Double.parseDouble(numero1), Double.parseDouble(numero2)));
            System.out.println("divisão: " + calculadora.divisao(Double.parseDouble(numero1), Double.parseDouble(numero2)));
            System.out.println("potencia: " + calculadora.potencia(Double.parseDouble(numero1), Double.parseDouble(numero2)));
            System.out.println("inverso: " + calculadora.inverso(Double.parseDouble(numero1)));
            System.out.println("raiz quadrada: " + calculadora.raiz(Double.parseDouble(numero1)));
        } catch (IOException e) {
            System.out.println("Erro na entrada");;
        } catch (NumberFormatException e) {
            System.out.println("O sistema aceita apenas numeros");
        } catch (ArithmeticException e){
            System.out.println("Numeros inválidos para operação");
        } catch (Exception e){
            System.out.println("Ocorreu uma exeção");
        } finally {
            System.out.println("Programa finalizado");
        }
    }
}
