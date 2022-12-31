import sys
import os
import random
import time
nykyinen = os.path.dirname(os.path.realpath(__file__))
vanhempi = os.path.dirname(nykyinen)
sys.path.append(vanhempi)
from trierakenne import TrieRakenne
from kappaleen_generoiminen import *
from json_funktiot import avaa_json, tallenna_json


class Suorituskykytestaus:
    """Luokka, joka testaa sovelluksen eri komponettien suorituskykyä

    Attributes:
        trie: Trierakenne, joka koostuu sävelsekvensseistä
        trie2: Trierakenne, joka koostuu nuottisekvensseistä
        alkuperainenData: data.json-tiedoston sisältö ennen 
            suorituskykytestausta
        uusi_data_nuotit: opetusdataan lisättävät nuotit
        uusi_data_savelet: opetusdataan lisättävät sävelet
    """
    def __init__(self):
        """Luokan konstruktori, joka luo uuden Suorituskykytestaus-olion
        """
        self.trie = TrieRakenne("sävelet")
        self.trie2 = TrieRakenne("nuotit")
        self.alkuperainenData = avaa_json()
        self.uusi_data_nuotit = []
        self.uusi_data_savelet = []

    def datan_lisaaminen_trieen(self, aste, kappaleidenMaara, kappaleenPituus, savelet_vai_nuotit):
        """Metodi, joka luo halutun määrän tietyn pituisia kappaleita, ja
        sitten lisää kaikki luodut kappaleet trieen. Tavoitteena on
        testata, kuinka kauan menee lisätä tietty määrä kappaleita trieen

        Args:
            aste: määrittää, miten isoja sekvenssejä trieen lisätään
            kappaleidenMaara: metodi luo näin monta kappaletta
            kappaleidenPituus: metodi luo kappaleita, joiden pituus on tämä
            savelet_vai_nuotit: kertoo, luodaanko säveliä vai nuotteja
        """
        kappaleet = []
        for i1 in range(kappaleidenMaara):
            kappale = []
            for i2 in range(kappaleenPituus):
                if savelet_vai_nuotit == "sävelet":
                    savel = random.choices(['C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C3#', 'C3b', 'D3#', 'D3b', 'E3#', 'E3b', 'F3#', 'F3b', 'G3#', 'G3b', 'A3#', 'A3b', 'B3#', 'B3b', 'C4#', 'C4b', 'D4#', 'D4b', 'E4#', 'E4b', 'F4#', 'F4b', 'G4#', 'G4b', 'A4#', 'A4b', 'B4#', 'B4b', 'C5#', 'C5b', 'D5#', 'D5b', 'E5#', 'E5b', 'F5#', 'F5b', 'G5#', 'G5b', 'A5#', 'A5b', 'B5#', 'B5b'])
                    kappale.append(savel[0])
                else:
                    nuotti = random.choices(["1/4", "1/8", "1/2", "3/8", "1/16", "1", "3/16"])
                    kappale.append(nuotti[0])
            kappaleet.append(kappale)
        
        aikaAlussa = time.time()

        for kappale in kappaleet:
            if savelet_vai_nuotit == "sävelet":
                self.trie.lisaa_kappale(aste, kappale)
                self.uusi_data_savelet.append(kappale)
            else:
                self.trie2.lisaa_kappale(aste, kappale)
                self.uusi_data_nuotit.append(kappale)

        aikaLopussa = time.time()
        print("Aikaa kului kappaleiden lisäämiseen: " + str(aikaLopussa - aikaAlussa) + " sekuntia, kun kappaleita oli " + str(kappaleidenMaara) + " ja yhden kappaleen pituus oli " + str(kappaleenPituus) + "ja aste on: " + str(aste))
        return

    def kappaleen_generointi_isolla_maaralla_opetusdataa(self, aste, pituus, kappaleiden_maara, savelet_vai_nuotit):
        """Metodi, joka generoi halutun pituusia kappaleita halutun määrän

        Args:
            aste: määrittää, minkä pituisia sekvenssejä trieen lisätään
            pituus: määrittää, kuinka pitkä kappale generoidaan
            kappaliden_maara: metodi generoi tämän verran kappaleita
            savelet_vai_nuotit: kertoo, generoidaanko säveliä vai nuotteja
        """
        aikaAlussa = time.time()
        for i in range(kappaleiden_maara):
            if savelet_vai_nuotit == "sävelet":
                kappale = generoi_kappale(aste, pituus, "sävelet")
            else:
                kappale = generoi_kappale(aste, pituus, "nuotit")
            if isinstance(kappale, str):
                print("EI ONNISTUNUT!!!!!")
        aikaLopussa = time.time()
        print("Aikaa kului kappaleen generoitiin: " + str(aikaLopussa - aikaAlussa) + " sekuntia, kun kappaleen pituus oli " + str(pituus) + " ja aste oli " + str(aste) + " ja kappaleita generoitiin " + str(kappaleiden_maara))
        return

def main():
    #testaus siitä, miten trien koko vaikuttaa lisäykseen

    skt = Suorituskykytestaus()
    maarat = [1, 10, 100, 500, 1000, 2500, 3000]

    for i in maarat:
        skt4 = Suorituskykytestaus()
        skt4.datan_lisaaminen_trieen(20, 1000, 200, "sävelet")
        print("--------")
        skt3 = Suorituskykytestaus()
        print("tyhjään trieen lisääminen :")
        skt3.datan_lisaaminen_trieen(20, i, 200, "sävelet")
        print("isoon trieen lisääminen :")
        skt4.datan_lisaaminen_trieen(20, i, 200, "sävelet")
        print("kasvavaan trieen lisääminen: ")
        skt.datan_lisaaminen_trieen(20, i, 200, "sävelet")
        print("-----------")

    
    #testi siitä, miten aste vaikuttaa lisäämiseen

    skt = Suorituskykytestaus()
    asteet = [1, 5, 10, 25, 50, 75, 100, 125]

    for aste in asteet:
        skt4 = Suorituskykytestaus()
        skt4.datan_lisaaminen_trieen(aste, 100, 505, "sävelet")
        print("--------")
        skt3 = Suorituskykytestaus()
        print("tyhjään trieen lisääminen :")
        skt3.datan_lisaaminen_trieen(aste, 100, 505, "sävelet")
        print("isoon trieen lisääminen :")
        skt4.datan_lisaaminen_trieen(aste, 100, 505, "sävelet")
        print("kasvavaan trieen lisääminen: ")
        skt.datan_lisaaminen_trieen(aste, 100, 505, "sävelet")
        print("-----------")



    #testi siitä, miten minkä kokoisen kappaleen lisäys vaikuttaa sävelien ja nuottien kesken

    print("----------")
    kappaleenKoot = [25, 50, 100, 250, 500, 750, 1000, 1500, 2000, 2500]
    for i in kappaleenKoot:
        skt = Suorituskykytestaus()
        print("Sävelsekvenssien lisääminen: ")
        skt.datan_lisaaminen_trieen(20, 100, i, "sävelet")
        print("Nuottisekvenmssien lisääminen: ")
        skt.datan_lisaaminen_trieen(20, 100, i, "nuotit")
        print("--------")


    #seuraava koodi testaa, miten kappaleiden määrä vaikuttaa generointiin

    skt = Suorituskykytestaus()
    skt.datan_lisaaminen_trieen(20, 100, 100, "sävelet")
    skt.datan_lisaaminen_trieen(20, 100, 100, "nuotit")
    data = {"nuotit": [], "savelet": []}
    data["nuotit"] = skt.uusi_data_nuotit
    data["savelet"] = skt.uusi_data_savelet
    tallenna_json(data)

    maarat = [1, 5, 10, 15, 20, 50, 75, 100, 150]

    print("---------")
    for maara in maarat:
        print("Sävelsekvenssin generointi: ")
        skt.kappaleen_generointi_isolla_maaralla_opetusdataa(20, 60, maara, "sävelet")
        print("nuottisekvenssin generointi :")
        skt.kappaleen_generointi_isolla_maaralla_opetusdataa(20, 60, maara, "nuotit")
        print("-------")

    tallenna_json(skt.alkuperainenData)

    #Seuraava koodi testaa, miten aste vaikuttaa generointiin

    skt = Suorituskykytestaus()
    skt.datan_lisaaminen_trieen(20, 100, 200, "sävelet")
    skt.datan_lisaaminen_trieen(20, 100, 200, "nuotit")
    data = {"nuotit": [], "savelet": []}
    data["nuotit"] = skt.uusi_data_nuotit
    data["savelet"] = skt.uusi_data_savelet
    tallenna_json(data)

    asteet = [1, 5, 10, 15, 25, 50, 75, 100, 125, 150, 199]

    for aste in asteet:
        print("-------------")
        print("Sävelsekvenssin generointi: ")
        skt.kappaleen_generointi_isolla_maaralla_opetusdataa(aste, 200, 1, "sävelet")
        print("nuottisekvenssin generointi :")
        skt.kappaleen_generointi_isolla_maaralla_opetusdataa(aste, 200, 1, "nuotit")
        print("-------")

    tallenna_json(skt.alkuperainenData)

    return

if __name__ == "__main__":
    main()

