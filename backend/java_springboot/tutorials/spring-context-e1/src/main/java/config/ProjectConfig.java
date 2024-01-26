package config;

import beans.Cat;
import beans.MyBean;
import beans.Owner;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.*;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.datasource.DataSourceTransactionManager;
import org.springframework.jdbc.datasource.DriverManagerDataSource;
import org.springframework.transaction.PlatformTransactionManager;
import org.springframework.transaction.annotation.EnableTransactionManagement;

import javax.sql.DataSource;
import java.sql.DriverManager;

@Configuration
@EnableTransactionManagement
@ComponentScan(basePackages = {"services", "repositories", "beans", "demo", "aspects"})
@EnableAspectJAutoProxy
public class ProjectConfig {

    @Bean
    public DataSource dataSource (){
        var dataSource = new DriverManagerDataSource();
        dataSource.setUrl("jdbc:mysql://localhost/demo");
        dataSource.setUsername("root");
        dataSource.setPassword("dylan");
        return dataSource;
    }

    @Bean                                       //@Bean
    public JdbcTemplate jdbcTemplate(){         //public JdbcTemplate jdbcTemplate(DataSource dataSource){
        return new JdbcTemplate(dataSource());  //    return new JdbcTemplate(dataSource);}
    }

    @Bean
    public PlatformTransactionManager transactionManager(DataSource dataSource){
        return new DataSourceTransactionManager(dataSource);
    }

//    @Bean
//    @Qualifier("cat1")
//    public Cat cat1(){
//        Cat c = new Cat();
//        c.setName("Tom");
//        return c;
//    }
//
//    @Bean
//    public Cat cat2(){
//        Cat c = new Cat();
//        c.setName("Leo");
//        return c;
//    }

//    @Bean
//    public Cat cat(){
//        Cat c = new Cat();
//        c.setName("Tom");
//        return c;
//    }
//
//    @Bean
//    public Owner owner(Cat cat){
//        Owner o = new Owner();
//        o.setCat(cat);
//        return o;
//    }

//    @Bean("A")
//    @Primary
//    public MyBean myBean(){
//        MyBean b =  new MyBean();
//        b.setText("Hello");
//        return b;
//    }
//
//    @Bean("B")
//    public MyBean myBean2(){
//        MyBean b =  new MyBean();
//        b.setText("World");
//        return b;
//    }


}
