# Käyttöohje

## Käyttööotto

Sovelluksen voi käynnistää ensin asentamalla riippuvuudet komennolla 
`poetry install`

ja sovellus käynnistyy komennolla
`poetry run python3 src/sovellus.py`

Koodin laadun saa selville komennolla `pylint src`

Testit voi suorittaa komennolla `poetry run pytest src`

Pelkistetyn estikattavuusraportin saa komennolla

`poetry run coverage report -m`

ja visuaallisemman testikattavuusraportin saa luotua komennolla
`poetry run coverage html`

jolloin tiedostoon htmlcov syntyy tiedosto nimeltään index.html ja sen avaamalla saa
visuaalisen testikattavuusrapotin selaimeen.

## Miten sovellusta käytetään?

Sovelluksen käynnistäessa aukeaa etusivunäkymä, jos nappia painamlla voi joko generoida uuden kappaleen ja siirtyä kuuntelemaan sitä toiseen näkymään tai sitten siirtyä näkymään, jossa voi lisätä kappaleen opetusdataan.


Opetusdataan voi lisätä kappaleita, ja ajatuksena on, että kappaleet lisätään peräkkäisinä sävel-nuotti yhdisteinä. 
Esimerkiksi "C4-1/4 D5-1/8 E4-1/2", jossa C4 on C-sävel neljänneltä oktaavilta ja 1/4 tarkoittaa neljännesosanuottia jne.
(1/4=neljäsosanuotti, 1/8=kahdeksasosanuotti, 1/2=puolinuotti, 3/8=pisteellinen neljännesosanuotti,
1=kokonuotti, 1/16=kuudestoistaosanuotti) Nuotit määrittelevät sävelen keston.


Generoidun kappaleen voi kuunnella haluamassaa tempossa. Generoitu kappale on tällä hetkellä
9-20 säveltä/nuottia pitkä ja opetusdataan on lisätty vain Tuiki tuiki tähtönen, Ukko-Nooa ja 
Lady Gagan Bad romancesta pieni osa, joten generoitu kappale ei vielä ole mitenkään tajunnan räjäyttävä ja 
muistuttaa osin näitä opetusdatan kappaleita, ja välillä lopputuloksena on joku näistä opetusdatan kappaleista. 
Generoitu kappale generoidaan nyt trie-rakenteen avulla, ja trierakenteeseen voi lisätä uutta dataa. 
Lisätty data ei kuitenkaan vielä tallennu json-tiedostoon vaan se katoaa sovelluksen sulkemisen yhteydessä.

