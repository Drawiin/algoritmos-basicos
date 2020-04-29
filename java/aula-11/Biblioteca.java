package com.company;

public class Biblioteca {

    public static void main(String[] args) {
         Emprestimo emprestimos[] = new Emprestimo[3];

        for (int i = 0; i < emprestimos.length; i++) {
            System.out.println("preencher dados do acadêmico");
            Academico academico = new Academico();
            academico.cadastrarPessoa();

            System.out.println("preencher dados do livro");
            Livro livro = new Livro();
            livro.cadastrarLivro();

            System.out.println("preencher dados do emprestimo");
            Emprestimo emprestimo = new Emprestimo();
            emprestimo.realizarEmprestimo(livro, academico);

            System.out.println("emprestimo cadastrado!!!!");

            emprestimos[i] = emprestimo;
        }

    }
}
