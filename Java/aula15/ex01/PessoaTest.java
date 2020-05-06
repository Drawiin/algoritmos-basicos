package aula15.ex01;

import jdk.internal.org.objectweb.asm.tree.TryCatchBlockNode;

import java.io.DataInputStream;
import java.io.IOException;

public class PessoaTest {
    public static void main(String[] args) {
        DataInputStream teclado = new DataInputStream(System.in);
        Pessoa pessoa = new Pessoa();
        try{
            System.out.println("Nome");
            pessoa.setNome(teclado.readLine());
            System.out.println("Idade");
            pessoa.setIdade(Integer.parseInt(teclado.readLine()));
            System.out.println("CPF");
            pessoa.setCpf(Integer.parseInt(teclado.readLine()));
            System.out.println("Numero");
            pessoa.setNumero(Integer.parseInt(teclado.readLine()));
            System.out.println("Logradouro");
            pessoa.setLogradouro(teclado.readLine());
            System.out.println("Bairro");
            pessoa.setBairro(teclado.readLine());
            System.out.println("Cidade");
            pessoa.setCidade(teclado.readLine());
            System.out.println("Estado");
            pessoa.setEstado(teclado.readLine());
            System.out.println("CEP");
            pessoa.setCep(Integer.parseInt(teclado.readLine()));

            System.out.println("nome> " + pessoa.getNome());
            System.out.println("idade> "+pessoa.getIdade());
            System.out.println("cpf> "+pessoa.getCpf());
            System.out.println("numero> "+pessoa.getNumero());
            System.out.println("logradouro> "+pessoa.getLogradouro());
            System.out.println("bairro> "+pessoa.getBairro());
            System.out.println("cidade> "+pessoa.getCidade());
            System.out.println("estado> "+pessoa.getEstado());
            System.out.println("cep>"+pessoa.getCep());

        } catch (IOException e) {
            System.out.println("Ocorreu uma exeção de E/S");
        } catch (NumberFormatException e){
            System.out.println("Apenas números inteiros permitidos");
        } catch (Exception e){
            System.out.println("Ocorreu um exeção");
        }finally {
            System.out.println("Programa finalizado");
        }
    }
}
