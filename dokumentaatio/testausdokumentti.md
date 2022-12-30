# Testausdokumentti

## Mitä on testattu?
### Yksikkötestaus

#### Yksikkötestauksen testikattavuusraportti

Lisää kuva tähän

Yksikkötestauksen ulkopuolelle on jätetty käyttöliittymän komponentit eli käyttöliittyma.py ja kaikki eri näkymät eli nakyma.py, aloitusnakyma.py, kappalenakyma.py ja opetusnakyma.py sekä sovelluksen käynnistykseen tarkoitettu sovellus.py-tiedosto ja tests-hakemisto, jossa on kaikki testit.
Toisin sanoen muuten src-hakemiston muu koodi on yksikkötestattu.

#### TrieRakenne-luokka

TrieRakenne-luokkaa on testattu siten, että voidaan olla varmistuneita siitä, että sen metodit toimivat niin kuin pitää. 
Testimetodi test_etsi_sekvenssin_seuraajat_loytaa_oikeat_seuraajat testaa sitä, että etsi_sekvenssin_seuraajat-metodi toimii oikein. Samalla tulee testattua, että lisaa_kappale-metodi lisää trieen oikean pituisia sekvenssejä.

#### Kappaleen generointi

Kappaleen generointia on testattu muum muassa siten, että kappaletta ei generoida virheellisillä parametreilla, kappale koostuu oikean mittaisista opetusdatan sekvensseistä ja lisäksi tilanteita, jossa kappaleen generointi epäonnistuu. Lisäksi on testattu funktiota, joka muuttaa kappaleen ja edellisten sävelien/nuottien arvot oikein, että arvot todella ovat oikeat.

#### Json-funktiot

Json-funktioita on testattu siten, että on varmistettu, että ne osaavat hakea oikean sisällön data.json-tiedostosta, ja että ne tallentavat oikein uuden sisällön samaan tiedostoon. 

#### Muut funktiot

Muut funktiot, kuten lisaa_opetusdataan_kappale, syotetyn_kappaleen_tarkistus ja soita_kappale, on testattu suurimmaksi osaksi siten, että on tutkittu niiden palautuksia, ja että ne palauttavat tietyn jutun tietyn toimenpiteen seurauksena.

#### Muut luokat

Luokat Solmu, Arpoja ja Soittaja on testattu vain siten, että on tarkistettu, että niiden konstruktori konstruktroi ne oikein, ja että niiden metodi toimii oikein.


### Suorituskykytestaus

Suorituskykytestauksessa on testattu kappaleen generointia isolla trie-rakenteella ja kappaleiden lisäämistä trie-rakenteeseen, kun kappaleita on paljon ja ne ovat pitkiä.

#### Kappaleen generoinnin suorituskykytestaus

#### Kappaleen lisäämisen suorituskykytestaus
