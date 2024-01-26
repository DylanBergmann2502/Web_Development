package com.dylanbergmann.my_spring_boot.blog;



import com.dylanbergmann.my_spring_boot.post.PostRepository;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDate;
import java.time.Month;
import java.util.List;

@RestController
public class HomeController {

    private final PostRepository postRepository;

    public HomeController(PostRepository postRepository){
        this.postRepository = postRepository;
    }

//    public List<Post> getPosts() {
//        return List.of(
//                new Post(
//                        "Dylan",
//                        "White Socks with Oxford Shoes",
//                        "First Post Content",
//                        LocalDate.of(2018, Month.AUGUST,27)
//
//                ),
//                new Post(
//                        "Dylan",
//                        "White Socks with Derby Shoes",
//                        "Second Post Content",
//                        LocalDate.of(2018, Month.SEPTEMBER,28)
//                )
//
//        );
//    }

    @GetMapping("/")
    public String home(Model model){
        model.addAttribute("posts", postRepository.findAll());
        return "home";
    }
}
