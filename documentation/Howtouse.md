# Asennusohje

Asennusohje on testattu yliopiston koneella, jossa pyörii Ubuntu. 

#### HUOM: Ohje olettaa, että sinulla on toimiva heroku-tili ja sinulla on asennettuna python3, pip, git, ja heroku cli. Lisäksi sinun täytyy asettaa heroku cli -työkalulle oikeat tunnukset ja salasanat.

## Lokaali
1. Kloonaa repo (git clone)
2. asenna virtuaaliympäristö virtualenv venv 
3. Aktivoi virtuaaliympäristö source venv/bin/activate
4. Mene kansioon ja aja pip3 install -r requirements.txt
5. Aja python3 run.py komento juuressa 
6. Nyt sovelluksen pitäisi toimia localhost:5000

Sovelluksen käyttö lokaalisti vaatii sen, että koneella on sqlite-tietokantaohjelmisto.


### Eroavaisuukset kehitys- ja tuotantoympäristöjen välillä

#### Huom: Kun haluaa kehittää herokuun sovellusta, tulee courses/views.py rivit 80-84 näyttää seuraavilta:

```python 
@app.route("/course/taken<course_id><student_id>", methods=["POST"])
def mark_course_as_taken(course_id, student_id):
    ## heroku:
    stmt = text("INSERT INTO Course_Student(course_id, student_id) VALUES(:course_id, :student_id) ON CONFLICT DO NOTHING").params(course_id=course_id, student_id=student_id)
    ## devmode: 
    ## stmt = text("INSERT OR IGNORE INTO Course_Student(course_id, student_id) VALUES(:course_id, :student_id)").params(course_id=course_id, student_id=student_id)
```

#### Huom: Kun haluaa kehittää paikallisesti sovellusta, tulee courses/views.py rivit 80-84 näyttää seuraavilta:

```python     
@app.route("/course/taken<course_id><student_id>", methods=["POST"])
def mark_course_as_taken(course_id, student_id):
    ## heroku:
    ## stmt = text("INSERT INTO Course_Student(course_id, student_id) VALUES(:course_id, :student_id) ON CONFLICT DO NOTHING").params(course_id=course_id, student_id=student_id)
    ## devmode: 
    stmt = text("INSERT OR IGNORE INTO Course_Student(course_id, student_id) VALUES(:course_id, :student_id)").params(course_id=course_id, student_id=student_id)
```
    
## Heroku 
Tee ensin lokaali asennus.
1. git init
2. git add .
3. git commit -m "commit viesti"
4. heroku create "sovelluksennimi"
5. git remote add "herokun git url"
6. git push heroku   

Nyt sovelluksen pitäisi pyöriä herokussa osoitteessa "sovelluksennimi".herokuapp.com

## Postgres-asennus herokuun

1.  heroku config:set HEROKU=1
2.  tarkista onko sovelluksella jo postgres-tietokanta ( heroku pg:psql)
3.  Jos ei, niin aja heroku addons:add heroku-postgresql:hobby-dev

Nyt herokun hallintapaneelissa pitäisi näkyä tieto siitä, että sovelluksessa pyörii postgres-tietokanta. 
  

Ylläpitäjäkäyttäjä luodaan luomalla normaalikäyttäjä ja antamalla hänelle kannassa rooli "A" ohjelmallisesti. Tämä täytyy tehdä, että voi lisätä uusia kursseja.

# Käyttöohje

<img src="https://raw.githubusercontent.com/Varjokorento/tsohasovellus19/master/documentation/navigation.PNG">

Navigointi sovelluksessa tapahtuu navigointipalkin avulla. Näkymässä pääkäyttäjän näkymä, jossa näkyy myös kurssien lisäämisosio.

## Rekisteröityminen

<img src="https://raw.githubusercontent.com/Varjokorento/tsohasovellus19/master/documentation/signup.PNG">

Sovelluksen kurssikohteiden muokkaaminen, lisääminen ja poistaminen vaativat rekisteröitymistä. Rekistöröityminen tapahtuu lomakkeella, johon on linkki etusivulla, jos ei ole kirjautunut.

Salasanan Bcrypt-hajautusarvo tallennetaan kantaan.

## Kirjautuminen

<img src="https://raw.githubusercontent.com/Varjokorento/tsohasovellus19/master/documentation/login.png">

Kirjautumiseen tarvitsee käyttäjätilin. Kirjautuminen tapahtuu käyttäjätunnuksen ja salasanan laittamisella kirjautumislomakkeeseen.

Adminkäyttäjä pystyy lisäämään kursseja sekä poistamaan kommentteja, kursseja ja kysymyksiä. Tavallinen käyttäjä ei voi poistaa mitään.

## Kurssien tietojen katsominen

<img src="https://raw.githubusercontent.com/Varjokorento/tsohasovellus19/master/documentation/CourseInformation.PNG">

Kursseja voi katsoa menemällä All Courses -osioon ja klikkaamalla Course Information nappulaa.

## Kurssitietosivu

<img src="https://github.com/Varjokorento/tsohasovellus19/blob/master/documentation/showcourse.PNG">

Sivun nappuloita painamalla voi katsoa kommentteja, kysymyksiä sekä kirjautuneena lisätä molempia.

## Kommentointi

<img src="https://raw.githubusercontent.com/Varjokorento/tsohasovellus19/master/documentation/comment.PNG">

Kurssille voi lisätä kommentin menemällä kurssin Additional Information osioon ja siellä klikkaamalla comment osiota. Kommentin teksti on pakollinen ja täytyy olla yli 10 merkkiä. Jokainen osio lomakkeessa on myös pakollinen.

## Kysymysten lisääminen

<img src="https://raw.githubusercontent.com/Varjokorento/tsohasovellus19/master/documentation/question.png">

Kurssille voi lisätä kysymyksiä menemällä kurssin Course information osioon ja siellä klikkaamalla add a question osiota. Kaikki kentät ovat pakollisia.

## Omien kurssien näkeminen

<img src="https://raw.githubusercontent.com/Varjokorento/tsohasovellus19/master/documentation/ihavetaken.PNG">

Kurssisivulta voi klikata "I have taken this course", jolloin käyttäjä voi tallentaa kurssin itselleen. Tehtyjä kursseja voi katsoa
klikkaamalla "My courses" -linkkiä.

## Tilastot

Tilastoihin pääsee painamalla course statistic linkkiä. Tilastoja voi vain lukea.
