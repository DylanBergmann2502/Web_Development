package beans;

import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

import javax.annotation.PostConstruct;

@Component
public class MyBean {
    private String text;

    @PostConstruct
    private void init(){
     this.text = "Hello";
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
}
