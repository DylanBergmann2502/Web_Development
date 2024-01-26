package aspects;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.*;

import org.springframework.stereotype.Component;


@Aspect
@Component
public class HelloServiceAspect {

//    @Before("execution(* services.HelloService.hello(..))")
//    public void before(){
//        System.out.println("A");
//    }
//
//    // After: executed no matter what,
//    // afterReturning: only if there's no exceptions
//    // afterThrowing: only if there's exceptions
//    @After("execution(* services.HelloService.hello(..))")
//    public void after(){
//        System.out.println("B");
//    }
//
//    @AfterReturning("execution(* services.HelloService.hello(..))")
//    public void afterReturning(){
//        System.out.println("C");
//    }
//
//    @AfterThrowing("execution(* services.HelloService.hello(..))")
//    public void afterThrowing(){
//        System.out.println("D");
//    }

    @Around("execution(* services.HelloService.hello(..))")
    public Object around(ProceedingJoinPoint joinPoint) throws Throwable {
        System.out.println("A");
        Object result = null;
        try {
//            result = joinPoint.proceed();
            result = joinPoint.proceed(new Object[] {"Bill"});
            System.out.println("B");
        } catch (Throwable throwable){
            throwable.printStackTrace();
        }
        return result;
    }
}
