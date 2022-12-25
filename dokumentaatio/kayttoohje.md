# Käyttöohje

## Käyttööotto

Sovelluksen voi käynnistää ensin asentamalla riippuvuudet komennolla 
`poetry install`

ja sovellus käynnistyy komennolla
`poetry run python3 src/sovellus.py`

Koodin laadun saa selville komennolla `pylint src`

Testit voi suorittaa komennolla `poetry run pytest src`

Pelkistetyn estikattavuusraportin saa komennolla

`poetry run coverage report`

ja visuaallisemman testikattavuusraportin saa luotua komennolla
`poetry run coverage html`

jolloin tiedostoon htmlcov syntyy tiedosto nimeltään index.html ja sen avaamalla saa
visuaalisen testikattavuusrapotin selaimeen.

## Miten sovellusta käytetään?

Sovelluksen käynnistäessa aukeaa etusivunäkymä, jossa nappia painamlla voi joko generoida uuden kappaleen ja siirtyä kuuntelemaan sitä toiseen näkymään tai sitten siirtyä näkymään, jossa voi lisätä kappaleen opetusdataan.

Sovelluksessa on kolme näkymää: etusivu-, opetus- ja kappalenäkymä, ja käyttäjä voi siirtyä näiden näkymien välillä. 


### Etusivu:

(Lisää kuva etusivusta)

Sovelluksen käynnistyessä aukeaa etusivunäkymä, jossa käyttäjä voi generoida uuden kappaleen ja siirtyä samalla kappalenäkymään kuuntelemaan uutta generoitua kappaletta. Etusivulta käyttäjä voi myös halutessaan siirtyä opetusnäkymään, jossa hän voi lisätä jonkun valmiin kappaleen opetusdataan.


### Opetusnäkymä:

(lisää kuva opetusnäkymästä)

Opetusnäkymässä käyttäjä voi kirjoittaa haluamansa kappaleen nuotit ja sävelet seuraavanlaisessa muodossa:

XY-Z XY-Z XY-Z,

jossa X on jokin sävel (säveliä ovat C, D, E, F, G, A, H, B), Y on oktaavi (eli miltä korkeudelta sävel soitetaan. Sovelluksessa sallittuja oktaaveja ovat 3, 4 ja 5) ja Z on nuotti (sallittuja nuotteja ja niiden kirjoitusasut sovelluksessa ovat: 
1/4=neljäsosanuotti, 1/8=kahdeksasosanuotti, 1/2=puolinuotti, 3/8=pisteellinen neljännesosanuotti,
1=kokonuotti, 1/16=kuudestoistaosanuotti). Nuotti määrittelee kuinka kauaan säveltä soitetaan, ja mitä suurempi aika-arvo nuotitlla on, sitä kauemmin säveltä soitetaan. 

Esimerkiksi: "C4-1/4 D5-1/8 E4-1/2 tai "C4-1/8 D4-1/8 E4-1/8 F4-1/8 G4-1/4 G4-1/4 A4-1/4 A4-1/4 G4-1/2 A4-1/4 A4-1/4 G4-1/2".

Sovellus tukee myös ylennettyjä ja alennettuja säveliä.

Esimerkiksi "C4#-1/4" on ylennetty C-sävel ja "D4b-1/4" on alennettu D-sävel


### Kappalenäkymä:

(lisää kuva opetusnäkymästä)

Kappalenäkymässä generoidun kappaleen voi kuunnella haluamassaa tempossa. Mitä suurempi tempo, sitä nopeampaa generoitu kappale soitetaan. Generoitu kappale on tällä hetkellä
10-20 säveltä/nuottia pitkä. Koska sovelluksessa ei ole määritelty ennalta mitään astetta Markovin ketjulle, ottaa kappaleen generointi kaikki edelliset sävelet/nuotit huomioon generoidessa uutta kappaletta, minkä takia lopputulos muistuttaa usein jotakin opetusdatassa olevaa kappaletta.

ja opetusdataan on lisätty vain Tuiki tuiki tähtönen, Ukko-Nooa ja 
Lady Gagan Bad romancesta pieni osa, joten generoitu kappale ei vielä ole mitenkään tajunnan räjäyttävä ja 
muistuttaa osin näitä opetusdatan kappaleita, ja välillä lopputuloksena on joku näistä opetusdatan kappaleista. 
Generoitu kappale generoidaan nyt trie-rakenteen avulla, ja trierakenteeseen voi lisätä uutta dataa. 
Lisätty data ei kuitenkaan vielä tallennu json-tiedostoon vaan se katoaa sovelluksen sulkemisen yhteydessä.

