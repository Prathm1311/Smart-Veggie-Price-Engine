package com.cipher.pythonIntegration.Controller;

import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.cipher.pythonIntegration.DTO.OrderItemRequest;
import com.cipher.pythonIntegration.Services.User_Order_Service;

@RestController
public class DataController {

    @Autowired
    private User_Order_Service user_Order_Service;

    @PostMapping("/getPrice")
    public double getPrice(@RequestBody OrderItemRequest request) {
        return user_Order_Service.orderService(request);
    }

}