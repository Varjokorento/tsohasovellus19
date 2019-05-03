# Asennusohje

Asennusohje on testattu yliopiston koneella, jossa pyörii Ubuntu. 

#### HUOM: Ohje olettaa, että sinulla on toimiva heroku-tili ja sinulla on asennettuna python3, pip, git, ja heroku cli. Lisäksi sinun täytyy asettaa heroku cli -työkalulle oikeat tunnukset ja salasanat.

## Lokaali
1. Kloonaa repo (git clone)
3. asenna virtuaaliympäristö virtualenv venv 
4. Aktivoi virtuaaliympäristö source venv/bin/activate
2. Mene kansioon ja aja pip3 install -r requirements.txt
3. Aja python3 run.py komento juuressa 
4. Nyt sovelluksen pitäisi toimia localhost:5000

Sovelluksen käyttö lokaalisti vaatii sen, että koneella on sqlite-tietokantaohjelmisto.

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

## Rekisteröityminen

<img src="https://raw.githubusercontent.com/Varjokorento/tsohasovellus19/master/documentation/signup.PNG" height="300" width="200">

Sovelluksen tietokohteiden muokkaaminen, lisääminen ja poistaminen vaativat rekisteröitymistä. Rekistöröityminen tapahtuu lomakkeella, johon on linkki etusivulla, jos ei ole kirjautunut.

## Kirjautuminen

<img src="https://raw.githubusercontent.com/Varjokorento/tsohasovellus19/master/documentation/login.png" height="300" width="200">

Kirjautumiseen tarvitsee käyttäjätilin. Käyttäjätili luodaan rekisteröitymällä. Kirjautuminen tapahtuu käyttäjätunnuksen ja salasanan laittamisella kirjautumislomakkeeseen.

## Kurssien tietojen katsominen

<img src="https://raw.githubusercontent.com/Varjokorento/tsohasovellus19/master/documentation/CourseInformation.PNG" height="300" width="200">
Kursseja voi katsoa menemällä All Courses -osioon ja klikkaamalla Course Information nappulaa.

<img src="https://github.com/Varjokorento/tsohasovellus19/blob/master/documentation/showcourse.PNG" width="700">


## Kommentointi

<img src="https://raw.githubusercontent.com/Varjokorento/tsohasovellus19/master/documentation/comment.PNG" height="300" width="200">

Kurssille voi lisätä kommentin menemällä kurssin Additional Information osioon ja siellä klikkaamalla comment osiota. Kommentin teksti on pakollinen ja täytyy olla yli 10 merkkiä. Jokainen osio lomakkeessa on myös pakollinen.

## Kysymysten lisääminen


<img src="https://raw.githubusercontent.com/Varjokorento/tsohasovellus19/master/documentation/comment.PNG" height="300" width="200">

Kurssille voi lisätä kysymyksiä menemällä kurssin Course information osioon ja siellä klikkaamalla add a question osiota. Kaikki kentät ovat pakollisia.

## Omien kurssien näkeminen

<img src="https://raw.githubusercontent.com/Varjokorento/tsohasovellus19/master/documentation/ihavetaken.PNG" height="300" width="200">

Kurssisivulta voi klikata "I have taken this course", jolloin käyttäjä voi tallentaa kurssin itselleen. Tehtyjä kursseja voi katsoa
klikkaamalla "My courses" -linkkiä.

## Tilastot

Tilastoihin pääsee painamalla course statistic linkkiä. Tilastoja voi vain lukea.
