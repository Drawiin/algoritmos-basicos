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
public class ClientePersistir {

    public ClientePersistir() {
    }
    
    public void cadastraCliente(ClienteVO cliente) throws Exception{
        try{
            System.out.println("Conectando ao banco de dados");
            
            System.out.println("Cadastrando......");
            System.out.println("Codigo: " + cliente.getCodigo());
            System.out.println("Nome: " + cliente.getNome());
            System.out.println("Logradouro: " + cliente.getLogradouro());
            System.out.println("Numero: " + cliente.getNumero());
            System.out.println("Bairro: " + cliente.getBairro());
            System.out.println("Cep: " + cliente.getCep());
            System.out.println("Cidade: " + cliente.getCidade());
            System.out.println("Estado: " + cliente.getEstado());
            System.out.println("Sexo: " + cliente.getSexo());
            
        }finally{
            System.out.println("Desconectando do banco de dados");
        }
    }
}
