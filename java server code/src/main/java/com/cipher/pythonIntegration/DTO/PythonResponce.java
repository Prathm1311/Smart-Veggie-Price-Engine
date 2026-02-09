package com.cipher.pythonIntegration.DTO;

import com.fasterxml.jackson.annotation.JsonProperty;

public class PythonResponce {

    @JsonProperty("predicted_final_price")
    private double predictedFinalPrice;

    public double getPredictedFinalPrice() {
        return predictedFinalPrice;
    }

    public void setPredictedFinalPrice(double predictedFinalPrice) {
        this.predictedFinalPrice = predictedFinalPrice;
    }
}
