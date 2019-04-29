# Asennusohje

### HUOM: Tutoriaali olettaa, että sinulla on toimiva heroku-tili ja sinulla on asennettuna python3, pip, ja heroku cli. Lisäksi sinun täytyy asettaa heroku cli -työkalulle oikeat tunnukset ja salasanat.

## Lokaali
1. Kloonaa repo (git clone)
3. asenna virtuaaliympäristö virtualenv venv 
4. Aktivoi virtuaaliympäristö source venv/bin/activate
2. Mene kansioon ja aja pip3 install -r requirements.txt
3. Aja python3 run.py komento juuressa 
4. Nyt sovelluksen pitäisi toimia localhost:5000

## Heroku 
Tee ensin lokaali asennus.
1. git init
2. git add .
3. git commit -m <commit viesti>
4. heroku create <sovelluksennimi>
5. git remote add <herokun git url>
6. git push heroku   
  
Nyt sovelluksen pitäisi pyöriä herokussa osoitteessa <sovelluksennimi>.herokuapp.com

Huom: Sovellus käyttää python3-versiota. 

Ylläpitäjäkäyttäjä luodaan luomalla normaalikäyttäjä ja antamalla hänelle kannassa rooli "A". Tämä täytyy tehdä, että voi lisätä uusia kursseja.

Sovelluksen käyttö vaatii sen, että koneella on sqlite-tietokantaohjelmisto.

# Käyttöohje

## Rekisteröityminen

Sovelluksen tietokohteiden muokkaaminen, lisääminen ja poistaminen vaativat rekisteröitymistä. Rekistöröityminen tapahtuu lomakkeella, johon on linkki etusivulla, jos ei ole kirjautunut.

## Kirjautuminen

Kirjautumiseen tarvitsee käyttäjätilin. Käyttäjätili luodaan rekisteröitymällä. Kirjautuminen tapahtuu käyttäjätunnuksen ja salasanan laittamisella kirjautumislomakkeeseen.

Tällä hetkellä kaikilla käyttäjillä on rooli STD. (Eli Standard). Tulevaisuudessa Admin roolit ja Standard-roolit ovat erikseen. 

## Kommentointi

Kurssille voi lisätä kommentin menemällä kurssin Additional Information osioon ja siellä klikkaamalla comment osiota. Kommentin teksti on pakollinen ja täytyy olla yli 10 merkkiä. Jokainen osio lomakkeessa on myös pakollinen.

## Kysymysten lisääminen

Kurssille voi lisätä kysymyksiä menemällä kurssin Additional Information osioon ja siellä klikkaamalla add a question osiota. Ainoa pakollinen tieto on kysymys. Lisäksi kysytään kysymykseen vastausta sekä lisääjän arviota kysymyksen haastavuudesta.

## Omien kurssinen näkeminen

Kurssisivulta voi klikata "I have taken this course", jolloin käyttäjä voi tallentaa kurssin itselleen. Tehtyjä kursseja voi katsoa
klikkaamalla "My courses" -linkkiä.

## Tilastot

Tilastoihin pääsee painamalla course statistic linkkiä. Tilastoja voi vain lukea.
