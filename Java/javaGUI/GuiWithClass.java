package javaGUI;

import javax.swing.*;

public class GuiWithClass {
    public static void main(String[] args) {
        JComponent components[] = {new JButton("botão")};
        SimpleFrame simpleFrame = new SimpleFrame(500, 500, "Janela", components);
    }
}

class SimpleFrame extends JFrame{


    SimpleFrame(int width, int height, String windowName, JComponent components[]){
        super(windowName);
        setSize(width, height);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
        for(int i = 0; i < components.length; i++){
            add(components[i]);
        }
    }

}
