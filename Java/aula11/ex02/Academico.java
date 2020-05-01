package aula11.ex02;

import java.util.Scanner;

public class Academico {
    private String nome;
    private String rg;
    private String cpf;
    private String telefone;
    private String endereco;
    private String nascimento;

    public String getNome() {
        return nome;
    }

    public String getRg() {
        return rg;
    }

    public String getCpf() {
        return cpf;
    }

    public String getTelefone() {
        return telefone;
    }

    public String getEndereco() {
        return endereco;
    }

    public String getNascimento() {
        return nascimento;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setRg(String rg) {
        this.rg = rg;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    public void setNascimento(String nascimento) {
        this.nascimento = nascimento;
    }

    public void cadastrarPessoa(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Cadastrar acadêmico");

        System.out.println("Nome");
        this.setNome(scanner.nextLine());

        System.out.println("Rg");
        this.setRg(scanner.next());

        System.out.println("cpf");
        this.setCpf(scanner.next());

        System.out.println("telefone");
        this.setTelefone(scanner.next());

        System.out.println("Endereço");
        this.setEndereco(scanner.nextLine());

        System.out.println("Nascimento");
        this.setNascimento(scanner.next());
    }
}

