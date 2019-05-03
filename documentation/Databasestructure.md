## Tietokantataulut

#### Tietokannanhallintajärjestelmät

Sovellus käyttää SQLITE-tietokannanhallintajärjestelmää paikallisesti ja PostGres-tietokannanhallintajärjestelmää Heroku-palvelussa. 

#### Normalisointi 

Tietokantatauluissa ei ole paljoa toisteista tieto. Tietorakenteissa ei ole kategorioita tai vastaavia, joita olisi pitänyt normalisoida. 

Poikkeuksena tässä kuitenkin Account-taulun role-kenttä. Tämä toistuu käyttäjältä toiselle ja roolit olisi voinut normalisoida omaksi taulukseen. Toisaalta roolin nimi haetaan aina, kun käyttäjäkin haetaan, joten denormalisoitu muoto saattaa olla oikeutettu ratkaisu. 

#### Indeksit

Tietokantatauluihin Course ja Comment on lisätty indeksit niihin kenttiin, joihin viitataan WHERE lauseissa ja yhteenvetokyselyissä.

## Taulujen kuvaus 

## Course-taulu
    id Integer PRIMARY KEY
    name VARCHAR
    description VARCHAR 
    core BOOLEAN
    likes Integer
    dislikes Integer
    ects Integer
    
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
     CREATE INDEX ix_course_ects ON course(ects)
     CREATE INDEX ix_course_id ON course (id)
    


## Comment -taulu
    id Integer PRIMARY KEY
    course_id Integer FOREIGN KEY REFERENCES(Course)
    text VARCHAR
    grade Integer
    workload Integer
    
    CREATE TABLE comment (
        id INTEGER NOT NULL,
        text VARCHAR(1000) NOT NULL,
        grade INTEGER NOT NULL,
        workload INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        PRIMARY KEY (id)
     )
     CREATE INDEX ix_comment_workload ON comment (workload)
     CREATE INDEX ix_comment_course_id ON comment (course_id)


## Question -taulu
    id Integer PRIMARY KEY
    course_id Integer FOREIGN KEY REFERENCES(Course)
    question VARCHAR
    answer VARCHAR
    difficulty Integer
    
    CREATE TABLE question (
        id INTEGER NOT NULL,
        question VARCHAR(1000) NOT NULL,
        answer VARCHAR(1000),
        difficulty INTEGER,
        course_id INTEGER NOT NULL,
        PRIMARY KEY (id)
        )
    
   
## Course_Students -liitostaulu
    id Integer PRIMARY KEY
    Student_id Integer FOREIGN KEY REFERENCES(Student)
    Course_id Integer FOREIGN KEY REFERENCES(Course)
    
    CREATE TABLE course_student (
        id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        student_id INTEGER NOT NULL,
        PRIMARY KEY (id)
        CONSTRAINT _student_course_uc UNIQUE (course_id, student_id)
        )

## Account-taulu
    id Integer PRIMARY KEY
    DateTime date_created
    DateTime date_modified
    name VARCHAR
    username VARCHAR
    password VARCHAR
    role = VARCHAR
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
        
# Tietokantakaavio
<img src="https://raw.githubusercontent.com/Varjokorento/tsohasovellus19/master/documentation/dbstructure.png" width="700">




