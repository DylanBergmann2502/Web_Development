package beans;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

@Component
public class Owner {

    @Autowired(required = false)
    @Qualifier("cat2")
    private Cat cat;

//    @Autowired()
//    public Owner(Cat cat){
//        this.cat = cat;
//    }

    public Cat getCat() {
        return cat;
    }

//    @Autowired
//    public void setCat(Cat cat) {
//        // some other stuffs as well
//        this.cat = cat;
//    }

    @Override
    public String toString() {
        return "Owner{" +
                "cat=" + cat +
                '}';
    }
}
