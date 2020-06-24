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
public class ClienteRN {
    
    ClienteRN(){
        
    }
    
    public void cadastratCliente(ClienteVO cliente) throws Exception{
        ClientePersistir  clientePers = new ClientePersistir();
        clientePers.cadastraCliente(cliente);
    }
}
