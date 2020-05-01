package aula11.ex01;

import java.util.Scanner;

public class Livro {
    private String titulo;
    private String autor;
    private String isbn;
    private int anoDePublicacao;

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public String getIsbn() {
        return isbn;
    }

    public int getAnoDePublicacao() {
        return anoDePublicacao;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }

    public void setAnoDePublicacao(int anoDePublicacao) {
        this.anoDePublicacao = anoDePublicacao;
    }

    public void cadastrarLivro(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Cadastro de Livro");

        System.out.println("Titulo do livro");
        this.setTitulo(scanner.nextLine());

        System.out.println("Autor do livro");
        this.setAutor(scanner.nextLine());

        System.out.println("ISBN");
        this.setIsbn(scanner.next());

        System.out.println("Ano de publicação");
        this.setAnoDePublicacao(scanner.nextInt());
    }
}
