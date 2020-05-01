package aula13.ex02;

import java.util.Scanner;

public class Funcionario extends Adulto{
    private String cargo;
    private double salario;

    public String getCargo() {
        return cargo;
    }

    public double getSalario() {
        return salario;
    }

    public void setCargo(String cargo) {
        this.cargo = cargo;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    @Override
    public void lerDados() {
        super.lerDados();
        Scanner scanner = new Scanner(System.in);

        System.out.printf("\n%s qual cargo ocupa ?", this.getNome());
        this.setCargo(scanner.next());

        System.out.printf("\n%s qual o salario de  da posição de %s ?", this.getNome(), this.getCargo());
        this.setSalario(scanner.nextDouble());
    }

    @Override
    public void mostrarDados() {
        super.mostrarDados();
        System.out.printf("\ncargo: %s\n salario: R$%.2f", this.getCargo(), this.getSalario());
    }
}
