package aula20.ex02;

import aula15.ex02.Calculadora;

import javax.swing.*;
import java.awt.*;

public class CalculadoraLayout extends JFrame {
    private GridBagLayout layout = new GridBagLayout();
    private GridBagConstraints constraints = new GridBagConstraints();
    private  JTextArea display = new JTextArea();

    private JButton buttons[][] = {
            {new JButton("7"), new JButton("8"), new JButton("9"), new JButton("/")},
            {new JButton("4"), new JButton("5"), new JButton("6"), new JButton("*")},
            {new JButton("1"), new JButton("2"), new JButton("3"), new JButton("-")},
            {new JButton("0"), new JButton("C"), new JButton("="), new JButton("+")}
    };

    void fillButtons(){
        for(int i = 0; i < buttons.length; i++){
            for (int j = 0; j < buttons[i].length; j++){
                constraints.fill = GridBagConstraints.HORIZONTAL;
                constraints.gridwidth = 1;
                constraints.gridy = i + 1;
                constraints.gridx = j;
                add(buttons[i][j], constraints);
            }
        }
    }

    CalculadoraLayout(){
        super("Calculadora");
        setSize(300, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
        setLayout(layout);

        constraints.fill = GridBagConstraints.HORIZONTAL;
        constraints.gridx = 0;
        constraints.gridy= 0;
        constraints.gridwidth = 4;
        constraints.ipadx = 30;
        constraints.ipady = 30;
        add(display, constraints);
        fillButtons();
    }

    public static void main(String[] args) {
        CalculadoraLayout calculadoraLayout = new CalculadoraLayout();
    }

}
