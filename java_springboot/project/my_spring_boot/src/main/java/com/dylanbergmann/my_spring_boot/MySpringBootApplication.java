package com.dylanbergmann.my_spring_boot;

import com.dylanbergmann.my_spring_boot.post.Post;
import com.dylanbergmann.my_spring_boot.post.PostRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import java.time.LocalDate;
import java.time.Month;

@SpringBootApplication
public class MySpringBootApplication {

	public static void main(String[] args) {
		SpringApplication.run(MySpringBootApplication.class, args);
	}

	@Bean
	CommandLineRunner commandLineRunner(PostRepository postRepository){
		return args -> {
		 Post first_post = new Post("Dylan",
				 "White Socks with Oxford Shoes",
				 "First Post Content",
				 LocalDate.of(2018, Month.AUGUST,27)
		 );
		 postRepository.save(first_post);
		};

	}
}
