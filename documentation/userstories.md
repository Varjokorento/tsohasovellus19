# User stories

### Opiskelijana haluan nähdä listauksen kursseista. 

SELECT course.id AS course_id, course.name AS course_name, course.description AS course_description, course.core AS course_core, course.ects AS course_ects, course.likes AS course_likes, course.dislikes AS course_dislikes
FROM course

### Opiskelijana haluan pystyä kommentoimaan kurssien sisältöä.

INSERT INTO comment (text, grade, workload, course_id) VALUES (?, ?, ?, ?)

### Opiskelijana haluan pystyä tykkäämään/ei-tykkäämään kursseista.

UPDATE course SET likes=? WHERE course.id = ?
PDATE course SET dislikes=? WHERE course.id = ?

### Opiskelijana haluan nähdä, mitä mieltä muut ovat kurssien sisällöistä.

SELECT Comment.id, Comment.text, Comment.grade, Comment.workload FROM Comment WHERE (Comment.course_id = ?)

### Opiskelijana haluan nähdä, mitä kursseja pidetään kaikkein työläimpänä.

Työmäärä suhteutettuna opintopisteisii:

Select Course.name, (AVG(Comment.workload)/Course.ects/) from Course JOIN Comment on course.id = Comment.course_id GROUP BY Course.name, Course.ects

Absoluuttinen työmäärä:

SELECT Course.name, AVG(Comment.workload) from Course JOIN Comment on course.id = Comment.course_id GROUP BY Course.name

### Opiskelijana haluan pystyä vertailemaan arvosanojani muihin

SELECT Course.name, AVG(Comment.grade) from Course JOIN Comment on course.id = Comment.course_id GROUP BY Course.name

### Opiskelijana haluan pystyä lisäämään kysyttyjä tenttikysymyksiä kurssin tietoihin

INSERT INTO question (question, answer, difficulty, course_id) VALUES (?, ?, ?, ?)

### Opiskelijana haluan pystyä näkemään, mitä kysymyksiä mihinkin kurssiin tyypillisesti liittyy.

SELECT Question.id, Question.question, Question.answer, Question.difficulty FROM Question WHERE (Question.course_id = :course_id)

### Opiskelijana haluan pystyä näkemään käymäni kurssit

 SELECT Course.name FROM COURSE_STUDENT JOIN COURSE ON Course.id = Course_Student.course_id WHERE student_id = ?

### Ylläpitäjänä haluan pystyä poistamaan kommentteja

DELETE FROM Comment WHERE Comment.course_id = ?

### Ylläpitäjänä haluan pystyä poistamaan kursseja
DELETE FROM Course WHERE Course.id = ?
