package com.company;

import javax.swing.*;
import java.awt.*;

public class PokemonBattle extends JFrame {
    private JTextField fieldName1;
    private JTextField fieldHeight1;
    private JTextField fieldWeight1;
    private JTextField fieldStrength1;

    private JTextField fieldName2;
    private JTextField fieldHeight2;
    private JTextField fieldWeight2;
    private JTextField fieldStrength2;

    private JButton buttonBattle;

    PokemonBattle() {
        setSize(600, 300);
        setLayout(null);
        setupLabels();
        setupTextFields();
        setupBattleButton();
        startListeners();
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    private void setupLabels() {
        JLabel labelTitle = new JLabel("Batalha Pokemon");

        labelTitle.setBounds(200, 0, 100, 20);

        JLabel labelTitlePokemon1 = new JLabel("Pokemon 1");
        JLabel labelName1 = new JLabel("Nome: ");
        JLabel labelHeight1 = new JLabel("Altura: ");
        JLabel labelWeight1 = new JLabel("Peso: ");
        JLabel labelStrength1 = new JLabel("Força: ");

        labelTitlePokemon1.setBounds(50, 20, 100, 20);
        labelName1.setBounds(50, 40, 100, 20);
        labelHeight1.setBounds(50, 80, 100, 20);
        labelWeight1.setBounds(50, 120, 100, 20);
        labelStrength1.setBounds(50, 160, 100, 20);

        JLabel labelTitlePokemon2 = new JLabel("Pokemon 2");
        JLabel labelName2 = new JLabel("Nome: ");
        JLabel labelHeight2 = new JLabel("Altura: ");
        JLabel labelWeight2 = new JLabel("Peso: ");
        JLabel labelStrength2 = new JLabel("Força: ");

        labelTitlePokemon2.setBounds(250, 20, 100, 20);
        labelName2.setBounds(250, 40, 100, 20);
        labelHeight2.setBounds(250, 80, 100, 20);
        labelWeight2.setBounds(250, 120, 100, 20);
        labelStrength2.setBounds(250, 160, 100, 20);

        Container window = getContentPane();

        window.add(labelTitle);
        window.add(labelTitlePokemon1);
        window.add(labelName1);
        window.add(labelHeight1);
        window.add(labelWeight1);
        window.add(labelStrength1);

        window.add(labelTitlePokemon2);
        window.add(labelName2);
        window.add(labelHeight2);
        window.add(labelWeight2);
        window.add(labelStrength2);
    }

    private void setupTextFields() {
        fieldName1 = new JTextField();
        fieldHeight1 = new JTextField();
        fieldWeight1 = new JTextField();
        fieldStrength1 = new JTextField();

        fieldName1.setBounds(100, 40, 100, 20);
        fieldHeight1.setBounds(100, 80, 100, 20);
        fieldWeight1.setBounds(100, 120, 100, 20);
        fieldStrength1.setBounds(100, 160, 100, 20);

        fieldName2 = new JTextField();
        fieldHeight2 = new JTextField();
        fieldWeight2 = new JTextField();
        fieldStrength2 = new JTextField();

        fieldName2.setBounds(350, 40, 100, 20);
        fieldHeight2.setBounds(350, 80, 100, 20);
        fieldWeight2.setBounds(350, 120, 100, 20);
        fieldStrength2.setBounds(350, 160, 100, 20);

        Container window = getContentPane();

        window.add(fieldName1);
        window.add(fieldHeight1);
        window.add(fieldWeight1);
        window.add(fieldStrength1);

        window.add(fieldName2);
        window.add(fieldHeight2);
        window.add(fieldWeight2);
        window.add(fieldStrength2);
    }

    private void setupBattleButton() {
        buttonBattle = new JButton("Batalhar");
        buttonBattle.setBounds(200, 190, 100, 30);

        Container window = getContentPane();

        window.add(buttonBattle);
    }

    private void startListeners() {
        buttonBattle.addActionListener(actionEvent -> {
            try {
                onBattleClicked();
            } catch (Throwable e) {
                JOptionPane.showMessageDialog(
                        this,
                        "Algo deu errado verifique os campos",
                        "Oopps!!",
                        JOptionPane.ERROR_MESSAGE
                );
            }
        });
    }

    private void onBattleClicked() throws Throwable {
        String name1 = fieldName1.getText();
        double height1 = Double.parseDouble(fieldHeight1.getText());
        double weight1 = Double.parseDouble(fieldWeight1.getText());
        double strength1 = Double.parseDouble(fieldStrength1.getText());

        Pokemon poke1 = new Pokemon(name1, height1, weight1, strength1);

        String name2 = fieldName2.getText();
        double height2 = Double.parseDouble(fieldHeight2.getText());
        double weight2 = Double.parseDouble(fieldWeight2.getText());
        double strength2 = Double.parseDouble(fieldStrength2.getText());

        Pokemon poke2 = new Pokemon(name2, height2, weight2, strength2);

        if (poke1.getPower() == poke2.getPower()) {
            JOptionPane.showMessageDialog(
                    this,
                    "Parece que ninguem ganhou dessa vez.",
                    "É um empate!!!!",
                    JOptionPane.PLAIN_MESSAGE
            );
        } else if (poke1.getPower() > poke2.getPower()) {
            JOptionPane.showMessageDialog(
                    this,
                    "Você venceu!!!!!!!!",
                    "Muitos Parabés " + name1,
                    JOptionPane.PLAIN_MESSAGE
            );
        } else {
            JOptionPane.showMessageDialog(
                    this,
                    "Você venceu!!!!!!!!",
                    "Muitos Parabés " + name2,
                    JOptionPane.PLAIN_MESSAGE
            );
        }
    }

}
