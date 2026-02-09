package com.cipher.pythonIntegration.Configuration;

import lombok.AllArgsConstructor;
import lombok.Getter;

@AllArgsConstructor
@Getter
public enum Vegetable {

    TOMATO(40),
    ONION(35),
    POTATO(30),
    CARROT(45),
    CAULIFLOWER(50);

    private final double basePrice;

    public double getBasePrice() {
        return basePrice;
    }

    public static Vegetable fromString(String name) {
        return Vegetable.valueOf(name.toUpperCase());
    }
}
