package aula11.ex01;

import java.util.Scanner;

public class Emprestimo {
    public Livro livro;
    public Academico academico;
    public String data;
    public String hora;

    public void realizarEmprestimo(Livro livro, Academico academico) {
        this.livro = livro;
        this.academico = academico;

        Scanner scanner = new Scanner(System.in);

        System.out.println("Data:");
        this.data = scanner.nextLine();

        System.out.println("Hora:");
        this.hora = scanner.nextLine();
    }
}
