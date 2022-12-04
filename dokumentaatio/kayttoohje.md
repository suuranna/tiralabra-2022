# Käyttöohje

## Käyttööotto

Sovelluksen voi käynnistää ensin asentamalla riippuvuudet komennolla 
`poetry install`

ja sovellus käynnistyy komennolla
`poetry run python3 src/sovellus.py`

Koodin laadun saa selville komennolla `pylint src`

Testit voi suorittaa komennolla `poetry run pytest src`

## Miten sovellusta käytetään?

Sovelluksen käynnistäessa aukeaa etusivunäkymä, jos nappia painamlla voi joko generoida uuden kappaleen ja siirtyä kuuntelemaan sitä toiseen näkymään tai sitten siirtyä näkymään, jossa voi lisätä kappaleen opetusdataan.


Opetusdataa ei vielä voi lisätä kappaleita, mutta ajatuksen on, että kappaleet lisätään peräkkäisinä sävel-nuotti yhdisteinä. 
Esimerkiksi "C4-1 D5-2 E4-1", jossa C4 on C-sävel neljänneltä oktaavilta ja 1 tarkoittaa neljännesosanuottia jne.
(1=neljäsosanuotti, 2=kahdeksasosanuotti, 3=kokonaisnuotti, 4=pisteellinen nuotti)


Generoidun kappaleen voi kuunnella haluamassaa tempossa. Generoitu kappale on tällä hetkellä
aina 9 säveltä/nuottia pitkä ja opetusdataan on lisätty vain Tuiki tuiki tähtönen, Ukko-Nooa ja Lady Gagan Bad romancesta pieni osa, joten generoitu kappale ei vielä ole mitenkään tajunnan räjäyttävä. Generoitu kappale generoidaan nyt trie-rakenteen avulla, ja trierakenteeseen voi lisätä uutta dataa.

