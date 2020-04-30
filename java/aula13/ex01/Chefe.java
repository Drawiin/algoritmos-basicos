package aula13.ex01;

public class Chefe extends Funcionario{
    private final double numeroDeHoras;

    Chefe(double salarioBase, double numeroDeHoras){
        this.setSalarioBase(salarioBase);
        this.numeroDeHoras = numeroDeHoras;
    }

    @Override
    public double calculaSalario() {
        return this.getSalarioBase() * this.numeroDeHoras;
    }
}
