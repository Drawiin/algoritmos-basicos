/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aula27;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.util.Scanner;

/**
 *
 * @author vini6
 */
public class ex01 {

    public static void main(String[] args) {
        try {
            BufferedWriter fileWriter = new BufferedWriter(new FileWriter("msg.txt"));

            Scanner scanner = new Scanner(System.in);

            System.out.println("Entre com sua mensagem > ");
            String userMsg = scanner.nextLine();
            
            fileWriter.write(userMsg);

            System.out.println("Mensagem gravada com sucesso");

            fileWriter.close();

        } catch (Exception e) {
            System.out.println("Um erro ocorreu: " + e.getMessage());
        }
    }
}
