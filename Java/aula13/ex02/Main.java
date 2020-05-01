package aula13.ex02;

public class Main {
    public static void main(String[] args) {
        Adulto adulto = new Adulto();
        System.out.println("\nLer dados do adulto");
        adulto.lerDados();
        System.out.println("\nDados do Aulto:");
        adulto.mostrarDados();

        Funcionario funcionario = new Funcionario();
        System.out.println("\nLer dados do funcionário");
        funcionario.lerDados();
        System.out.println("\nDados do funcionário: ");
        funcionario.mostrarDados();
    }
}
