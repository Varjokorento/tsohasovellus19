# User stories

### Opiskelijana haluan nähdä listauksen kursseista. 
```sql
SELECT course.id AS course_id, course.name 
AS course_name, course.description AS course_description, 
course.core AS course_core, 
course.ects AS course_ects, 
course.likes AS course_likes, 
course.dislikes AS course_dislikes
FROM course
```

### Opiskelijana haluan pystyä kommentoimaan kurssien sisältöä.
```sql
INSERT INTO comment (text, grade, workload, course_id) VALUES (?, ?, ?, ?)
```
### Opiskelijana haluan pystyä tykkäämään/ei-tykkäämään kursseista.
```sql
UPDATE course SET likes=? WHERE course.id = ?
UPDATE course SET dislikes=? WHERE course.id = ?
```
### Opiskelijana haluan nähdä, mitä mieltä muut ovat kurssien sisällöistä.
```sql
SELECT Comment.id, Comment.text, Comment.grade, Comment.workload FROM Comment WHERE (Comment.course_id = ?)
```
### Opiskelijana haluan nähdä, mitä kursseja pidetään kaikkein työläimpänä.

#### Työmäärä suhteutettuna opintopisteisiin: 

```sql
Select Course.name as name, (AVG(Comment.workload)/Course.ects) 
AS average from Course 
JOIN Comment on course.id = Comment.course_id 
GROUP BY name, Course.ects ORDER BY average DESC
```

#### Absoluuttinen työmäärä:
```sql
  stmt = text("SELECT Course.name as name, AVG(Comment.workload) as average from Course 
  JOIN Comment on course.id = Comment.course_id 
  GROUP BY name 
  ORDER BY average DESC")
```
### Opiskelijana haluan pystyä vertailemaan arvosanojani muihin

```sql
SELECT Course.name, AVG(Comment.grade) from Course JOIN Comment on course.id = Comment.course_id GROUP BY Course.name
```

### Opiskelijana haluan pystyä lisäämään kysyttyjä tenttikysymyksiä kurssin tietoihin

```sql
INSERT INTO question (question, answer, difficulty, course_id) VALUES (?, ?, ?, ?)
```

### Opiskelijana haluan pystyä näkemään, mitä kysymyksiä mihinkin kurssiin tyypillisesti liittyy.
```sql
SELECT Question.id, Question.question, Question.answer, Question.difficulty 
FROM 
Question WHERE (Question.course_id = :course_id)
```

### Opiskelijana haluan pystyä näkemään käymäni kurssit
```sql
 SELECT Course.name FROM COURSE_STUDENT JOIN COURSE ON Course.id = Course_Student.course_id WHERE student_id = ?
```

### Ylläpitäjänä haluan pystyä poistamaan kommentteja

```sql
DELETE FROM Comment WHERE Comment.course_id = ?
```

### Ylläpitäjänä haluan pystyä poistamaan kursseja
```sql
DELETE FROM Course WHERE Course.id = ?
```
