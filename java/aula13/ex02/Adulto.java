package aula13.ex02;

import java.util.Scanner;

public class Adulto extends Pessoa{
    private String rg;
    private String cpf;

    public String getRg() {
        return rg;
    }

    public String getCpf() {
        return cpf;
    }

    public void setRg(String rg) {
        this.rg = rg;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    @Override
    public void lerDados(){
        super.lerDados();
        Scanner scanner = new Scanner(System.in);

        System.out.printf("\nCerto %s qual o seu rg ?", this.getNome());
        this.setRg(scanner.next());

        System.out.printf("\n%s agora qual seu cpf ?", this.getNome());
        this.setCpf(scanner.next());
    }

    @Override
    public void mostrarDados() {
        super.mostrarDados();
        System.out.printf("\nrg: %s\ncpf: %s", this.getRg(), this.getCpf());
    }
}
