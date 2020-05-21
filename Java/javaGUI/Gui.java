package javaGUI;

import javax.swing.*;

public class Gui {
    public static void main(String[] args) {
        JFrame jFrame = new JFrame("Exemplo");
        jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jFrame.setSize(250, 500);
        JButton button = new JButton("botão");
        jFrame.getContentPane().add(button);
        jFrame.setVisible(true);
    }
}
