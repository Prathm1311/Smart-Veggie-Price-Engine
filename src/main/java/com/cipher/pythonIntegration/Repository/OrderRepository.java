package com.cipher.pythonIntegration.Repository;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.cipher.pythonIntegration.Model.Order;

public interface OrderRepository extends MongoRepository<Order, String> {
    
}
