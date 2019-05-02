## Tietokantataulut

## Create Table -lausekkeet

CREATE TABLE course (
        id INTEGER NOT NULL,
        name VARCHAR(400) NOT NULL,
        description VARCHAR(1000) NOT NULL,
        core BOOLEAN NOT NULL,
        ects INTEGER,
        likes INTEGER,
        dislikes INTEGER,
        PRIMARY KEY (id),
        CHECK (core IN (0, 1))
)

CREATE TABLE comment (
        id INTEGER NOT NULL,
        text VARCHAR(1000) NOT NULL,
        grade INTEGER NOT NULL,
        workload INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        PRIMARY KEY (id)
)

CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        role VARCHAR(10) NOT NULL,
        PRIMARY KEY (id)
)

CREATE TABLE question (
        id INTEGER NOT NULL,
        question VARCHAR(1000) NOT NULL,
        answer VARCHAR(1000),
        difficulty INTEGER,
        course_id INTEGER NOT NULL,
        PRIMARY KEY (id)
)

CREATE TABLE user_role (
        id INTEGER NOT NULL,
        "roleName" VARCHAR(10) NOT NULL,
        PRIMARY KEY (id)
)

CREATE TABLE course_student (
        id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        student_id INTEGER NOT NULL,
        PRIMARY KEY (id)
)

## Course-taulu
    id Integer PRIMARY KEY
    name VARCHAR
    description VARCHAR 
    core BOOLEAN
    likes Integer
    dislikes Integer
    ects Integer
    


## Comment -taulu
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
    id Integer PRIMARY KEY
    Student_id Integer FOREIGN KEY REFERENCES(Student)
    Course_id Integer FOREIGN KEY REFERENCES(Course)

## User-taulu
    id Integer PRIMARY KEY
    DateTime date_created
    DateTime date_modified
    name VARCHAR
    username VARCHAR
    password VARCHAR
    role = VARCHAR
        
# Tietokantakaavio
<img src="https://raw.githubusercontent.com/Varjokorento/tsohasovellus19/master/documentation/dbstructure.png" width="700">





Course
-
id PK int
name VARCHAR
description VARCHAR
Core boolean
likes int
dislikes int
ects int

Comment
-
id PK int
course_id int FK >- Course.id
comment_text VARCHAR
comment_grade int
comment_workload int

Question
-
id PK int
course_id int FK >- Course.id
question VARCHAR
answer VARCHAR
difficulty int

Course_Students
-
id PK int
Student_id Integer FK >- User.id
Course_id Integer FK >- Course.id

User
-
id PK int
date_created DateTime
date_modified DateTime 
name VARCHAR
username VARCHAR
password VARCHAR
role = VARCHAR
