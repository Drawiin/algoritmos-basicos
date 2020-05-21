package aula21.ex02;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class CapturarTextoV2 extends JFrame {
    private JLabel label = new JLabel("Digite");
    private JTextField textField = new JTextField("Digite aqui o texto", 25);
    private JButton button = new JButton("Capturar");
    private JLabel textLabel = new JLabel("Texto");
    private JPanel container = new JPanel();
    private FlowLayout containerLayout = new FlowLayout(FlowLayout.CENTER);

    private void startListeners(){
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                String conteudo = textField.getText();
                textLabel.setText(conteudo);
            }
        });

        textField.addFocusListener(new FocusListener() {
            @Override
            public void focusGained(FocusEvent focusEvent) {
                textField.setText("");
            }

            @Override
            public void focusLost(FocusEvent focusEvent) {

            }
        });

        textField.addKeyListener(new KeyListener() {
            @Override
            public void keyTyped(KeyEvent keyEvent) {}

            @Override
            public void keyPressed(KeyEvent keyEvent) {
                if(keyEvent.getKeyChar() == '\n'){
                    String conteudo = textField.getText();
                    textLabel.setText(conteudo);
                }
            }

            @Override
            public void keyReleased(KeyEvent keyEvent) { }
        });
    }

    private void montarJanela(){
        container.setLayout(containerLayout);
        container.add(label);
        container.add(textField);
        container.add(button);
        add(container, BorderLayout.PAGE_START);
        textLabel.setHorizontalAlignment(JLabel.CENTER);
        textLabel.setVerticalAlignment(JLabel.NORTH);
        add(textLabel, BorderLayout.CENTER);
    }

    CapturarTextoV2(){
        super("Ouvir Texto");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);

        startListeners();
        montarJanela();
    }


    public static void main(String[] args) {
        new CapturarTextoV2();
    }
}
