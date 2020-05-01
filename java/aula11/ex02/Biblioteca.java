package aula11.ex02;

public class Biblioteca {
    public static void main(String[] args) {
        Livro livros[] = new Livro[3];
        Academico academicos[] = new Academico[3];
        Emprestimo emprestimos[] = new Emprestimo[3];

        for(int i = 0; i < livros.length; i++){
            System.out.println("Livro: " + (i + 1));
            livros[i] = new Livro();
            livros[i].cadastrarLivro();
        }

        for(int i = 0; i < academicos.length; i++){
            System.out.println("academico: " + (i + 1));
            academicos[i] = new Academico();
            academicos[i].cadastrarPessoa();
        }

        for(int i = 0; i < emprestimos.length; i++){
            System.out.println("Emprestimo: " + (i + 1));
            emprestimos[i] = new Emprestimo();

            emprestimos[i].realizarEmprestimo(academicos[i], livros[i]);
        }
    }
}
