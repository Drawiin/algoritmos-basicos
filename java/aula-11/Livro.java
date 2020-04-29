package com.company;

import java.util.Scanner;

public class Livro {
    public String nome;
    public String autor;
    public String isbn;
    public String anoDePublicao;


    public void cadastrarLivro(){
        Scanner scanner = new Scanner(System.in);

        System.out.println("Nome:");
        this.nome = scanner.nextLine();

        System.out.println("Autor:");
        this.autor = scanner.nextLine();

        System.out.println("ISBN:");
        this.isbn = scanner.nextLine();

        System.out.println("Ano de publicação:");
        this.anoDePublicao = scanner.nextLine();
    }
}
