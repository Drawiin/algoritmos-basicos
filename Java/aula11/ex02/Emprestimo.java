package aula11.ex02;

import java.util.Scanner;

public class Emprestimo {
    private Livro livro;
    private Academico academico;
    private String data;
    private String hora;

    public Livro getLivro() {
        return livro;
    }

    public Academico getAcademico() {
        return academico;
    }

    public String getData() {
        return data;
    }

    public void setLivro(Livro livro) {
        this.livro = livro;
    }

    public String getHora() {
        return hora;
    }

    public void setAcademico(Academico academico) {
        this.academico = academico;
    }

    public void setData(String data) {
        this.data = data;
    }

    public void setHora(String hora) {
        this.hora = hora;
    }

    public void realizarEmprestimo(Academico academico, Livro livro){
        Scanner scanner = new Scanner(System.in);
        this.setAcademico(academico);
        this.setLivro(livro);
        System.out.println("Cadastrando emprstimo");

        System.out.println("Data");
        this.setData(scanner.next());

        System.out.println("Hora");
        this.setHora(scanner.next());
    }
}
