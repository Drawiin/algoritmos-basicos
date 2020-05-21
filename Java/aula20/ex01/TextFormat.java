package aula20.ex01;

import javax.swing.*;
import java.awt.*;

public class TextFormat extends JFrame {
    private JTextField textField = new JTextField("Esccolha um estilo");
    private GridBagLayout layout = new GridBagLayout();
    private GridBagConstraints constraints = new GridBagConstraints();
    private  JPanel container = new JPanel();

    private JRadioButtonMenuItem radioButtonMenuItems[] = {
            new JRadioButtonMenuItem("Normal"),
            new JRadioButtonMenuItem("Negrito"),
            new JRadioButtonMenuItem("Italico"),
            new JRadioButtonMenuItem("Negrito e Italico")
    };

    void fillContainer(){
        for(int i = 0; i < radioButtonMenuItems.length; i++){
            container.add(radioButtonMenuItems[i]);
        }
    }

    TextFormat (int width, int height, String windowName){
        super(windowName);
        setSize(width, height);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);

        setLayout(layout);
        constraints.fill = GridBagConstraints.HORIZONTAL;
        constraints.gridx = 0;
        constraints.gridx = 0;
        add(textField, constraints);
        constraints.gridx = 0;
        constraints.gridy = 1;
        fillContainer();
        add(container, constraints);
        pack();
    }
}
