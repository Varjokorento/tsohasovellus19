# Työn rajoitteet, omat kokemukset sekä puuttuvat ominaisuudet

## Rajoitteet

Tällä hetkellä sovelluksessa on useita rajoitteita, jotka se tarvitsisi, jos sen haluaisi aidosti laittaa maailmalle. 

### Lähdekoodin laatu

Lähde koodi tulisi refaktoroida niin, että kaikkea toiminnallisuutta ei tehtäisi views.py -tiedostoissa. Jonkinlainen tietokantakäsittelyluokka 
tulisi implementoida. Tässä versiossa sitä ei ole johtuen enimmäkseen python-kokemukseni vähyydestä.

### Käyttäjän kurssitietojen parempi tallentaminen 

Tällä hetkellä sovellus tallentaa käyttäjälle vain hänen käymänsä kurssin yleiset tiedot, ei käyttäjäkohtaisia tietoja. Tämä olisi yksi kohta, jossa
olisi voinut tehdä enemmän toiminnallisuutta. 

### Tietokantakyselyiden ja -rakenteen yksinkertaisuus

Tietokantakyselyt ovat kohtuullisen yksinkertaisia eikä sovelluksessa ole kuin yksi monesta moneen suhde. Ne tosin toteuttavat halutut toiminnallisuudet.

### Rajattomat tykkäykset -ongelma

Tällä hetkellä ei ole mitään rajoituksia sille, että kursseista voisi tykätä miljoonia kertoja. Tämän olisi voinut ratkaista niin, että
vain kirjautuneet voisivat tykätä ja tykkäyksestä lisättäisiin tieto tietokantaan. 

### UI-lomakkeet 

Lomakkeiden syöttökentät ovat liian pieniä ja muutenkin rumia. Tätä en saanut korjattua.

## Puuttuvat ominaisuudet

Sovelluksesta ei puutu ominaisuuksia, joita olin pistänyt alkuperäiseen vaatimusmäärittelyyni. Toki toiminnallisuuksia voisi laajentaa ja 
tehdä etenkin käyttäjän kurssitietojen tallentamisesta monipuolisempaa. 

Vaikka sovellus täyttää omat vaatimusmäärittelyni, niin seuraavat ominaisuukset ovat sellaisia, jotka sovelluksesta voidaan katsoa puuttuvan:

* Kurssien haku nimillä 
* Tiettyjen ominaisuuksien disablointi UI:lla, jos käyttäjä on jo tehnyt ne (esimerkiksi kurssin valitseminen omiin tietoihin)
* Kommenttien editoiminen
* Kysymysten editoiminen

## Omat kokemukset

Oma kokemukseni sovelluksen tekemisestä oli opettavainen. Flask ja etenkin Jinja olivat mielestäni hyvin tehokkaita ja helppokäyttöisiä
työkaluja. Opin myös paljon python-ohjelmointikielestä, jota en ole aikaisemmin käyttänyt ainakaan näin paljoa. Kurssi opetti minulle myös
paljon tietokantakehityksestä, etenkin aina silloin, kun tuli vastaan PostGres ja Sqlite -tietokantakielien eroja. 

Voin sanoa, että olen kohtuullisen tyytyväinen lopputulokseen.


