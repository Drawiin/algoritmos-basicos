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
public class ProdutoRN {
    
    ProdutoRN(){
        
    }
    
    public void cadastrarProduto(ProdutoVO produto) throws Exception{
        ProdutoPersistir  produtoPers = new ProdutoPersistir();
        produtoPers.cadastrarProduto(produto);
    }
}
