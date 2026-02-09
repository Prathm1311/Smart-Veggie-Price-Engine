package com.cipher.pythonIntegration.Model;

import org.springframework.data.mongodb.core.mapping.Field;

import com.cipher.pythonIntegration.Configuration.Vegetable;

import lombok.Data;
import lombok.Getter;

@Data
@Getter
public class Order {


    @Field("vegetable")
    private Vegetable vegetable; // ENUM value as String (TOMATO, ONION)

    private int quantity;

    private double basePrice;

    private double finalPrice;

}
