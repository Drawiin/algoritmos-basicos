package aula16.ex02;

import java.io.IOException;

public class LetraTeste {
    public static void main(String[] args) {
        try{
            Letra letra = new Letra();
            String string1 = letra.leString();
            String string2 = letra.leString();
            System.out.println(letra.compara(string1, string2));
            System.out.println(letra.conta(string1));
            System.out.println(letra.maiuscula(string1));
            System.out.println(letra.minuscula(string2));
        } catch (IOException e) {
            System.out.println("Erro de E/S");
        } catch (Exception e){
            System.out.println("Ocorreu uma exeção");
        } finally {
            System.out.println("Programa finalizado");
        }

    }
}
