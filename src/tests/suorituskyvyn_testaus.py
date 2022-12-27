import sys
import os
import random
import time
nykyinen = os.path.dirname(os.path.realpath(__file__))
vanhempi = os.path.dirname(nykyinen)
sys.path.append(vanhempi)
from trierakenne import TrieRakenne
from json_funktiot import avaa_json


class Suorituskykytestaus:
    """Luokka, joka testaa sovelluksen eri komponettien suorituskykyä

    Attributes:
        trie: Trierakenne, joka koostuu sävelsekvensseistä
        alkuperainenData: data.json-tiedoston sisältö ennen 
            suorituskykytestausta
    """
    def __init__(self):
        """Luokan konstruktori, joka luo uuden Suorituskykytestaus-olion
        """
        self.trie = TrieRakenne("sävelet")
        self.trie2 = TrieRakenne("nuotit")
        self.alkuperainenData = avaa_json()

    def datan_lisaaminen_trieen(self, kappaleidenMaara, kappaleenPituus, savelet_vai_nuotit):
        """Metodi, joka luo halutun määrän tietyn pituisia kappaleita, ja
        sitten lisää kaikki luodut kappaleet trierakenteeseen

        Args:
            kappaleidenMaara: metodi luo näin monta kappaletta
            kappaleidenPituus: metodi luo kappaleita, joiden pituus on tämä
            savelet_vai_nuotit: kertoo, luodaanko säveliä vai nuotteja
        """
        data = []
        kappaleet = []
        for i1 in range(kappaleidenMaara):
            kappale = []
            for i2 in range(kappaleenPituus):
                if savelet_vai_nuotit == "sävelet":
                    savel = random.choices(["C3", "D3", "E3", "F3", "G3", "A3", "B3", "C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "D5", "E5", "F5", "G5", "A5", "B5"])
                    kappale.append(savel[0])
                else:
                    nuotti = random.choices(["1/4", "1/8", "1/2", "3/8", "1/16", "1", "3/16"])
                    kappale.append(nuotti[0])
            kappaleet.append(kappale)
        
        aikaAlussa = time.time()

        for kappale in kappaleet:
            if savelet_vai_nuotit == "sävelet":
                self.trie.lisaa_kappale(kappale)
            else:
                self.trie2.lisaa_kappale(kappale)

        aikaLopussa = time.time()
        print("Aikaa kului kappaleiden lisäämiseen: " + str(aikaLopussa - aikaAlussa) + " sekuntia, kun kappaleita oli " + str(kappaleidenMaara) + " ja yhden kappaleen pituus oli " + str(kappaleenPituus))
        return

    def kappaleen_generointi_isolla_maaralla_opetusdataa(self, minimi, maksimi, kappaleiden_maara, savelet_vai_nuotit):
        """Metodi, joka generoi halutun pituusia kappaleita halutun määrän

        Args:
            minimi: generoitavan kappaleen minimipituus
            maksimi: generoitavan kappaleen maksimipituus
            kappaliden_maara: metodi generoi tämän verran kappaleita
        """
        aikaAlussa = time.time()
        for i in range(kappaleiden_maara):
            if savelet_vai_nuotit == "sävelet":
                kappale = self.trie.luo_kappale(minimi, maksimi)
            else:
                kappale = self.trie2.luo_kappale(minimi, maksimi)
                print(kappale)
            #print(kappale)
        aikaLopussa = time.time()
        print("Aikaa kului kappaleen generoitiin: " + str(aikaLopussa - aikaAlussa) + " sekuntia, kun min oli " + str(minimi) + " ja max oli " + str(maksimi) + " ja kappaleita generoitiin " + str(kappaleiden_maara))
        return

def main():
    #kappaleen pituutena 100 on liian paljon, jos kappaleiden määrä on 10000
    #2000-10000 on liian iso pituus kappaleelle, vaikka kappaleita olisikin vain 10
    #1 000 000 kappaletta on ehkä vähän liikaa vaikka kappaleiden pituus olisi vain 10 (69 sekunttia)
    #mitä enemmän opetusdataa trie-rakenteessa on sitä kauemmin uuden kappaleen lisääminen kestää
    #uuden kappaleen generoiminen kestää myös kauemmin mitä enemmän kappaleita on lisättye trieen
    #skt = Suorituskykytestaus()
    """
    skt0 = Suorituskykytestaus()
    skt0.datan_lisaaminen_trieen(100, 20)
    skt = Suorituskykytestaus()
    skt.datan_lisaaminen_trieen(1000, 20)
    skt1 = Suorituskykytestaus()
    skt1.datan_lisaaminen_trieen(10000, 20)
    skt3 = Suorituskykytestaus()
    skt3.datan_lisaaminen_trieen(100000, 20)
    skt4 = Suorituskykytestaus()
    skt4.datan_lisaaminen_trieen(1000000, 20)
    """
    skt = Suorituskykytestaus()
    #skt.datan_lisaaminen_trieen(10000, 50, "nuotit")
    #skt.datan_lisaaminen_trieen(10000, 50, "nuotit")
    #skt.datan_lisaaminen_trieen(10000, 50, "nuotit")
    #skt.datan_lisaaminen_trieen(10000, 50, "nuotit")
    skt.datan_lisaaminen_trieen(210, 50, "nuotit")
    #skt.trie2.alusta()
    #skt.trie2.alusta()
    for i in range(1, 20):
        print("kierros: " + str(i))
        #pituus = 10 * i 
        #skt.datan_lisaaminen_trieen(10000, 10, "nuotit")
        skt.kappaleen_generointi_isolla_maaralla_opetusdataa(i, i, 1, "nuotit")



    return

if __name__ == "__main__":
    main()

