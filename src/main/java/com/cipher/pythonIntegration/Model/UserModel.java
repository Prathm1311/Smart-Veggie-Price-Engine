package com.cipher.pythonIntegration.Model;

import java.time.Instant;
import java.util.List;

import lombok.Data;

@Data
public class UserModel {

    private String id;

    private String userId; // who placed the order

    private Instant orderTime; // when order was placed

    private double totalPrice; // final price

    private String orderStatus; // CONFIRMED, CANCELLED, etc.

    private boolean apiCounted; // for API count logic

    private List<Order> items;
}
