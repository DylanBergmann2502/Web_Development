package main;

import java.lang.annotation.Annotation;
import java.util.List;

import beans.Cat;
import beans.MyBean;
import beans.Owner;
import config.ProjectConfig;
import demo.Person;
import model.Product;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import repositories.ProductRepository;
import services.HelloService;
import services.ProductDeliveryService;
import services.ProductService;

public class Main {
    // XML, Annotations
    public static void main (String[] args){
        try (AnnotationConfigApplicationContext context =
                     new AnnotationConfigApplicationContext(ProjectConfig.class)){
            ProductService p = context.getBean(ProductService.class);
            p.addTenProduct();
//            p.addOneProduct();


//            HelloService service = context.getBean(HelloService.class);
//            String message = service.hello("John");
//            System.out.println("Result is " + message);

//            var p = context.getBean(Person.class);
//            p.sayHello("Bill");

//            var productRepository = context.getBean(ProductRepository.class);
//            // Read
//            List<Product> products = productRepository.getProducts();
//            products.forEach(System.out::println);
//            // Create
//            var p = new Product();
//            p.setName("Beer");
//            p.setPrice(10);
//
//            productRepository.addProduct(p);

//            // by name, by type
//            MyBean b1 = context.getBean(MyBean.class);
//            MyBean b2 = context.getBean(MyBean.class);
//
//            System.out.println(b1.getText());
//            System.out.println(b2.getText());

//            ProductDeliveryService service = context.getBean(ProductDeliveryService.class);
//            service.addSomeProducts();

//            Cat x = context.getBean(Cat.class);
//            Owner o = context.getBean(Owner.class);
//
//            x.setName("Leo");
//            System.out.println(x);
//            System.out.println(o);
        }
    }
}
