/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aula27;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.Reader;
import javax.swing.JFileChooser;
import javax.swing.filechooser.FileNameExtensionFilter;

/**
 *
 * @author vini6
 */
public class ex02 {

    public static void main(String[] args) {
        try {
            JFileChooser fileChoser = new JFileChooser();
            
            FileNameExtensionFilter filter = new FileNameExtensionFilter("Arquivos de texto (*.txt)", "txt");
            fileChoser.setFileFilter(filter);
            
            int  result = fileChoser.showOpenDialog(null);
            
            if(result == JFileChooser.APPROVE_OPTION){
                String filePath = fileChoser.getSelectedFile().getPath();
                
                BufferedReader fileReader = new BufferedReader(new FileReader(filePath));
                
                String fileContent = "";
                String line = fileReader.readLine();
                
                while(line != null){
                    fileContent += line + "\n";
                    line = fileReader.readLine();
                }
                
                System.out.println("Conteudo:\n" + fileContent);
                
                fileReader.close();
                
                
            }
            
            
            

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

}
