package com.example.demo.student;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.time.LocalDate;
import java.time.Month;
import java.util.List;


@Configuration
public class StudentConfig {

    @Bean
    CommandLineRunner commandLineRunner(StudentRepository repository){
        return args -> {
            Student dylan = new Student(
                    "Dylan",
                    "dylan.bergmann@gmail.com",
                    LocalDate.of(2000, Month.JANUARY,5)
            );

             Student alex = new Student(
                    "Alex",
                    "alex@gmail.com",
                    LocalDate.of(2002, Month.JANUARY,5)
            );

            repository.saveAll( //invoke repository => save students into db
                    List.of(dylan, alex) //No default constructor for entity:  : com.example.demo.student.Student] with root cause
            );

        };
    }
}
