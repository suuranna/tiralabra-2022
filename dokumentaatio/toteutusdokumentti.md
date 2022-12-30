# Totetutusdokumentti

Toteutin trie-rakennetta ja Markovin ketjua hyödyntävän musiikintuottajan.

## Ohjelman yleisrakenne

Ohjelman tärkeimmät rakennepalat ovat trie-rakenne ja kappaleen generoiva funktio.

Trie-rakenne on toteutettu yhtenä luokkana, joka hyödyntää Solmu-luokkaa. Trie-rakenteen avulla on helppo 

Sovelluksessa on käytössä graafinen käyttöliittymä, joka koostuu neljästä näkymästä. Aloitus-, opetus- ja kappalenäkymä ovat sovelluksen käynnistyessä aukeavassa ikkunassa kun taas viestinäkymä on uudessa omassa ikkunassaan aukeava näkymä. Kaikki nämä näkymät perivät Nakyma-luokan.


## Saavutetut aika- ja tilavaativuudet

Generoi_kappale-funktion aikavaativuus on rekursiivisen funktion etsi_seuraava aikavaativuus eli O(n²), jossa n on sekvenssin seuraajien määrä, kerrottuna sillä määrällä, mitä etsi_seuraava-funktiota kutsutaan yhteensä eli pahimmassa tapauksessa p*m, jossa p on kappaleen haluttu pituus ja m on triessä olevien solmujen määrä. Näin ollen Generoi_kappale-funktion aikavaativuus on O(pmn²).

Generoi_kappale-funktio hyödyntää p-mittaista listaa, jossa p on funktiolle parametrina annettu pituus, ja k-mittaista listaa, jossa k on aste. Lisäksi se käyttää trie-rakennetta, jonka tilavaativuus on O(m), jossa m on solmujen määrä. Generoi_kappale-funktion tilavaativuus on näin ollen O(m), koska m on todennäköisimmin näistä suurin.

Trie-rakenteella on lisaa_kappale- ja etsi_sekvenssin_seuraajat-metodit. Lisaa_kappale-metodin aikavaativuus on O(nm), jossa n on trieen lisättävien sekvenssien määrä ja m on yhden sekvenssin pituus (eli m=k+1, jossa k on aste). Etsi_sekvenssin_seuraajat-metodin aikavaativuus on O(m) tai O(l), jossa m on annetun sekvenssin pituus ja l on seuraajien määrä, riippuen siitä kumpi on suurempi. 


## Työn mahdolliset puutteet ja parannusehdotukset

Kappaleen generoinnin voisi luultavasti toteuttaa jollakin paremmalla tekniikalla kuin rekursiolla, mutta en keksinyt toista tapaa, jolla olisi voinut välttää "umpikujat" ja varmistaa, että niihin ei eksytä uudestaan. 


