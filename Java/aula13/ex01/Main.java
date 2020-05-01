package aula13.ex01;

public class Main {
    public static void main(String[] args) {
        Chefe chefe = new Chefe(1200, 12);
        System.out.println("Salario do chefe:" + chefe.calculaSalario());

        Horista horista = new Horista(1200, 200.20);
        System.out.println("Salario do horista:" + horista.calculaSalario());

        Comissionado comissionado = new Comissionado(1200, 300.67);
        System.out.println("Salario do comissionado: " + comissionado.calculaSalario());
    }
}
