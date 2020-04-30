package aula13.ex01;

public class Comissionado extends Funcionario{
    private final double valorDesconto;

    Comissionado(double salarioBase, double valorDesconto){
        this.setSalarioBase(salarioBase);
        this.valorDesconto = valorDesconto;
    }

    @Override
    public double calculaSalario() {
        return this.getSalarioBase() - this.valorDesconto;
    }
}
