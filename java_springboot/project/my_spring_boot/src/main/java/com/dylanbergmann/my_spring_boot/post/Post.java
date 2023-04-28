package com.dylanbergmann.my_spring_boot.post;

import jakarta.persistence.*;
import org.springframework.data.annotation.CreatedBy;
import org.springframework.data.annotation.CreatedDate;

import java.time.LocalDate;

import static jakarta.persistence.GenerationType.SEQUENCE;

@Entity
@Table
public class Post {
    @jakarta.persistence.Id //specify pk
    @SequenceGenerator(
            name = "post_sequence",
            sequenceName = "post_sequence",
            allocationSize = 1
    )
    @GeneratedValue(
            strategy = SEQUENCE,
            generator = "post_sequence"
    )
    @Column(
            name = "id"
    )
    private Long Id;

    @Column(
            name = "author",
            nullable = false,
            updatable = false
    )
    @CreatedBy
    private String author; //foreign key

    @Column(
            name = "title",
            nullable = false,
            length = 100
    )
    private String title;

    @Column(
            name = "content",
            columnDefinition = "TEXT"
    )
    private String content;

    @Column(
            name = "date_posted",
            nullable = false,
            updatable = false
    )
//    @CreatedDate
    private LocalDate date_posted;

    public Post() {
    }

//    public Post(Long id, String author, String title, String content, LocalDate date_posted) {
//        Id = id;
//        this.author = author;
//        this.title = title;
//        this.content = content;
//        this.date_posted = date_posted;
//    }

    public Post(String author, String title, String content, LocalDate date_posted) {
        this.author = author;
        this.title = title;
        this.content = content;
        this.date_posted = date_posted;
    }

    public Long getId() {
        return Id;
    }

    public void setId(Long id) {
        Id = id;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

//    DateTimeFormatter format = DateTimeFormatter.ofPattern("MMMM, dd yyyy");
    public LocalDate getDate_posted() {
        return date_posted;
    }

    public void setDate_posted(LocalDate date_posted) {
        this.date_posted = date_posted;
    }

    @Override
    public String toString() {
        return "Post{" +
                "Id=" + Id +
                ", author='" + author + '\'' +
                ", title='" + title + '\'' +
                ", content='" + content + '\'' +
                ", date_posted=" + date_posted +
                '}';
    }
}
