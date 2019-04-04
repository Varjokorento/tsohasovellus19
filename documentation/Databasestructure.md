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
    


## Comment -taulu

Comment:
    id Integer PRIMARY KEY
    course_id Integer FOREIGN KEY REFERENCES(Course)
    comment_text VARCHAR
    comment_grade Integer
    comment_workload Integer

## Question -taulu
    id Integer PRIMARY KEY
    course_id Integer FOREIGN KEY REFERENCES(Course)
    question VARCHAR
    answer VARCHAR
    difficulty Integer
    
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
