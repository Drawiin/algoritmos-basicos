package aula13.ex01;

public class Horista extends Funcionario{
    private double valorINSS;

    Horista(double slarioBase, double valorINSS){
        this.setSalarioBase(slarioBase);
        this.valorINSS = valorINSS;
    }

    @Override
    public double calculaSalario() {
        return getSalarioBase() - this.valorINSS;
    }
}
