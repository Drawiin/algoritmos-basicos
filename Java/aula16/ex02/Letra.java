package aula16.ex02;

import javax.imageio.IIOException;
import java.io.DataInputStream;
import java.io.IOException;
import java.util.jar.JarOutputStream;

public class Letra {
    public boolean compara(String firstString, String secondString) throws Exception{
        return (firstString.equals(secondString));
    }

    public int conta(String string) throws Exception{
        return string.length();
    }

    public String maiuscula(String string) throws Exception{
        return string.toUpperCase();
    }

    public String minuscula(String string) throws Exception{
        return string.toLowerCase();
    }

    public String leString() throws IOException, Exception {
        DataInputStream teclado = new DataInputStream(System.in);
        System.out.println("Digite uma string");
        return teclado.readLine();
    }

}
