package services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;
import repositories.ProductRepository;

@Service
public class ProductDeliveryService {

    private final ProductRepository productRepository;

    @Autowired
    public ProductDeliveryService(ProductRepository productRepository){
        this.productRepository = productRepository;
    }

//    public void addSomeProducts(){
//        productRepository.add();
//        productRepository.add();
//    }
}
