package com.cipher.pythonIntegration.Services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import com.cipher.pythonIntegration.Configuration.Vegetable;

import com.cipher.pythonIntegration.DTO.OrderItemRequest;
import com.cipher.pythonIntegration.DTO.PythonRequest;
import com.cipher.pythonIntegration.DTO.PythonResponce;

@Service
public class User_Order_Service {

    @Autowired
    private RestTemplate restTemplate;

    public double orderService(OrderItemRequest request) {

        Vegetable vegetable = Vegetable.fromString(request.getVegetable());
        String vegetableName = vegetable.toString();
        double price = vegetable.getBasePrice();

        String demand = getRandomDemand();
        String season = request.getSeason();

        PythonRequest pythonReq = new PythonRequest(vegetableName, season, demand, price);

        PythonResponce pythonRes = restTemplate.postForObject(
                "http://127.0.0.1:8000/predict",
                pythonReq,
                PythonResponce.class);

        double finalPrice = pythonRes.getPredictedFinalPrice();

        return finalPrice;
    }

    public static String getRandomDemand() {
        String[] demandLevels = { "LOW", "MEDIUM", "HIGH" };
        int index = (int) (Math.random() * demandLevels.length);
        return demandLevels[index];
    }
}
