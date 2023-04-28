package com.example.demo.student;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController //This annotation makes this class serve rest endpoint
@RequestMapping(path = "api/v1/student")
public class StudentController {
    private final StudentService studentService;

    @Autowired
    public StudentController(StudentService studentService) {
        this.studentService = studentService;
    }
    //this = studentService should be auto instantiated and injected into the constructor,
    // but for that to work, studentService has to be a spring bean

    @GetMapping
    public List<Student> getStudents() {
        return studentService.getStudents();
    }

    @PostMapping
    public void registerNewStudent(@RequestBody Student student){
        studentService.addNewStudent(student);
    }

    @PutMapping(path = "update/{studentId}")
    public void updateStudent (
            @PathVariable("studentId") Long studentId,
            @RequestParam(required = false) String name,
            @RequestParam(required = false) String email
    )
    {
        studentService.updateStudent(studentId, name, email);
    }

    @DeleteMapping(path="delete/{studentId}")
    public void deleteStudent(@PathVariable("studentId") Long studentId){

        studentService.deleteStudent(studentId);
    }

}