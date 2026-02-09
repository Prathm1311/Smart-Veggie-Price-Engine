package com.cipher.pythonIntegration.Repository;
import org.springframework.data.mongodb.repository.MongoRepository;
import com.cipher.pythonIntegration.Model.UserModel;

public interface UserRepository extends MongoRepository<UserModel, String> {
    
}
