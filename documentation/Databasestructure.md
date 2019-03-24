## Tietokantataulut

# Course-taulu

Course:
    id Integer PRIMARY KEY
    name VARCHAR
    description VARCHAR 
    core BOOLEAN
    likes Integer
    dislikes Integer
    ects Integer
    
## Course_Comments -liitostaulu

Course_Comments:
    id Integer PRIMARY KEY
    course_id Integer FOREIGN KEY REFERENCES(Course)
    comment_id Integer FOREIGN KEY REFERENCES(Comment)


## Comment -liitostaulu

Comment:
    id Integer PRIMARY KEY
    comment_text VARCHAR
    comment_grade Integer
    comment_workload Integer

    
## Course_Students -liitostaulu

Course_students:
    id Integer PRIMARY KEY
    Student_id Integer FOREIGN KEY REFERENCES(Student)
    Course_id Integer FOREIGN KEY REFERENCES(Course)

## Student-taulu
Student
    id Integer PRIMARY KEY
    nickname VARCHAR
    password VARCHAR
