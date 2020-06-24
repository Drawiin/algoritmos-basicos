/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aula26;

/**
 *
 * @author vini6
 */
public class ProdutoPersistir {

    public ProdutoPersistir() {
    }

    public void cadastrarProduto(ProdutoVO produto) throws Exception {
        try {
            System.out.println("Conectando ao banco de dados");

            System.out.println("Cadastrando......");
            System.out.println("Produto: " + produto.getProduto());
            System.out.println("Descrição" + produto.getDescricao());
            System.out.println("Unidade Padrão: " + produto.getUnidadePadrao());
            System.out.println("Estoque Minimo: " + produto.getEstoqueMinimo());
            System.out.println("PreçoUnitario: " + produto.getPrecoUnitario());

        } finally {
            System.out.println("Desconectando do banco de dados");
        }
    }
}
