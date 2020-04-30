package aula11.ex01;

import java.util.Scanner;

public class Academico {
    public String nome;
    public String rg;
    public String cpf;
    public String telefone;
    public String endereco;
    public String nascimento;

    public void cadastrarPessoa(){
        Scanner scanner = new Scanner(System.in);

        System.out.println("nome:");
        this.nome = scanner.nextLine();

        System.out.println("rg:");
        this.rg = scanner.nextLine();

        System.out.println("cpf:");
        this.cpf = scanner.nextLine();

        System.out.println("telefone:");
        this.telefone = scanner.nextLine();

        System.out.println("endereço:");
        this.endereco = scanner.nextLine();

        System.out.println("data de nascimento:");
        this.nascimento = scanner.nextLine();
    }
}
