# Testausdokumentti

## Mitä on testattu?
### Yksikkötestaus

#### Yksikkötestauksen testikattavuusraportti

Lisää kuva tähän

Yksikkötestauksen ulkopuolelle on jätetty käyttöliittymän komponentit eli käyttöliittyma.py ja kaikki eri näkymät eli nakyma.py, aloitusnakyma.py, kappalenakyma.py ja opetusnakyma.py sekä sovelluksen käynnistykseen tarkoitettu sovellus.py-tiedosto ja tests-hakemisto, jossa on kaikki testit.
Toisin sanoen muuten src-hakemiston muu koodi on yksikkötestattu.

#### TrieRakenne-luokka

#### Funktiot

#### Muut luokat

Luokat Solmu, Arpoja ja Soittaja on testattu vain siten



### Suorituskykytestaus

Suorituskykytestauksessa on testattu kappaleen generointia isolla trie-rakenteella ja kappaleiden lisäämistä trie-rakenteeseen, kun kappaleita on paljon ja ne ovat pitkiä.

#### Kappaleen generoinnin suorituskykytestaus

#### Kappaleen lisäämisen suorituskykytestaus

Väliaikaisia huomioita:
- kappaleen pituutena 100 on liian paljon, jos kappaleiden määrä on 10000
- 2000-10000 on liian iso pituus kappaleelle, vaikka kappaleita olisikin vain 10
- 1 000 000 kappaletta on ehkä vähän liikaa vaikka kappaleiden pituus olisi vain 10 (69 sekunttia meni)
- mitä enemmän opetusdataa trie-rakenteessa on sitä kauemmin uuden kappaleen lisääminen kestää
- uuden kappaleen generoiminen kestää myös kauemmin mitä enemmän kappaleita on lisättye trieen



Kappaleen pituus ollessa 20 kappaleita generoidessa generoitiin menevä aika kertaantuu 10:llä määrän kertaantuessa kymmenellä
