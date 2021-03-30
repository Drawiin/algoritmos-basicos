package com.company;

public class Pokemon {
    private final String name;
    private final double height;
    private final double weight;
    private final double strength;
    private final double power;

    Pokemon(String name, double height, double weight, double strength) {
        this.name = name;
        this.height = height;
        this.weight = weight;
        this.strength = strength;
        this.power = computePower(height, weight, strength);
    }

    private double computePower(double height, double weight, double strength) {
        return ((height * weight) / 2.0) * strength;
    }

    public double getPower() {
        return power;
    }
}


