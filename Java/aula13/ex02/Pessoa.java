package aula13.ex02;

import java.util.Scanner;

public abstract class Pessoa {
    private String nome;
    private int idade;
    private String sexo;

    public String getNome() {
        return nome;
    }

    public int getIdade() {
        return idade;
    }

    public String getSexo() {
        return sexo;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public void setSexo(String sexo) {
        this.sexo = sexo;
    }

    public void lerDados(){
        Scanner scanner = new Scanner(System.in);

        System.out.println("\nQual o seu nome ?:");
        this.setNome(scanner.nextLine());

        System.out.printf("\nMuito bem %s quantos anos vc tem ?", this.getNome());
        this.setIdade(scanner.nextInt());

        System.out.println("\nEntre com o sexo:");
        this.setSexo(scanner.next());
    }

    public void mostrarDados(){
        System.out.printf("\nnome: %s\nidade: %d\nsexo: %s",
                this.getNome(), this.getIdade(), this.getSexo());
    }
}
