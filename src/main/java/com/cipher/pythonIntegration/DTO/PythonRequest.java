package com.cipher.pythonIntegration.DTO;



import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@AllArgsConstructor
@Getter
@Setter
public class PythonRequest {
    private String vegetable;
    private String season;
    private String demand;
    private double base_price;
}