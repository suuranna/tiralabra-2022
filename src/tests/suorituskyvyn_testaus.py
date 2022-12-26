import sys
import os
import random
import time
nykyinen = os.path.dirname(os.path.realpath(__file__))
vanhempi = os.path.dirname(nykyinen)
sys.path.append(vanhempi)
from trierakenne import TrieRakenne
from json_funktiot import *


class Suorituskykytestaus:
    def __init__(self):
        self.trie = TrieRakenne("sävelet")
        self.trie2 = TrieRakenne("nuotit")
        #self.trie.alusta()
        #self.trie2.alusta()
        self.alkuperainenData = avaaJson()

    def datan_lisaaminen_trieen(self, kappaleidenMaara, kappaleenPituus):
        data = []
        kappaleet = []
        for i1 in range(kappaleidenMaara):
            kappale = []
            for i2 in range(kappaleenPituus):
                savel = random.choices(["C3", "D3", "E3", "F3", "G3", "A3", "B3", "C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "D5", "E5", "F5", "G5", "A5", "B5"])
                kappale.append(savel[0])
            kappaleet.append(kappale)
        
        aikaAlussa = time.time()

        for kappale in kappaleet:
            self.trie.lisaa_kappale(kappale)

        aikaLopussa = time.time()

        print("Aikaa kului kappaleiden lisäämiseen: " + str(aikaLopussa - aikaAlussa) + " sekunttia, kun kappaleita oli " + str(kappaleidenMaara) + " ja yhden kappaleen pituus oli " + str(kappaleenPituus))

    def kappaleen_generointi_isolla_maaralla_opetusdataa(self, min, max, kappaleiden_maara):
        aikaAlussa = time.time()
        for i in range(kappaleiden_maara):
            kappale = self.trie.luo_kappale(min, max)
            #print(kappale)
        aikaLopussa = time.time()
        print("Aikaa kului kappaleen generoitiin: " + str(aikaLopussa - aikaAlussa) + " sekunttia, kun min oli " + str(min) + " ja max oli " + str(max) + " ja kappaleita generoitiin " + str(kappaleiden_maara))

def main():
    #kappaleen pituutena 100 on liian paljon, jos kappaleiden määrä on 10000
    #2000-10000 on liian iso pituus kappaleelle, vaikka kappaleita olisikin vain 10
    #1 000 000 kappaletta on ehkä vähän liikaa vaikka kappaleiden pituus olisi vain 10 (69 sekunttia)
    #mitä enemmän opetusdataa trie-rakenteessa on sitä kauemmin uuden kappaleen lisääminen kestää
    #uuden kappaleen generoiminen kestää myös kauemmin mitä enemmän kappaleita on lisättye trieen
    skt = Suorituskykytestaus()
    skt.datan_lisaaminen_trieen(1, 3000)
    skt.datan_lisaaminen_trieen(1000, 100)
    skt.datan_lisaaminen_trieen(25, 40)
    skt.kappaleen_generointi_isolla_maaralla_opetusdataa(20, 20, 500000)
    skt.datan_lisaaminen_trieen(1, 100)
    skt.datan_lisaaminen_trieen(1000000, 10)
    skt.datan_lisaaminen_trieen(1, 100)
    skt.datan_lisaaminen_trieen(100000, 10)
    skt.datan_lisaaminen_trieen(100000, 20)
    skt.datan_lisaaminen_trieen(1, 100)
    skt.datan_lisaaminen_trieen(10000, 10)
    skt.datan_lisaaminen_trieen(10000, 20)
    skt.datan_lisaaminen_trieen(10000, 30)
    skt.kappaleen_generointi_isolla_maaralla_opetusdataa(20, 20, 1)
    #skt.datan_lisaaminen_trieen(10000, 40)
    skt.datan_lisaaminen_trieen(1, 100)
    skt.datan_lisaaminen_trieen(1000, 10)
    skt.datan_lisaaminen_trieen(10, 10)
    skt.datan_lisaaminen_trieen(10, 50)
    skt.datan_lisaaminen_trieen(10, 100)
    #tähän tyssäää
    #skt.datan_lisaaminen_trieen(10, 1000)
    skt.datan_lisaaminen_trieen(1, 100)
    skt.datan_lisaaminen_trieen(1, 1000)
    skt.datan_lisaaminen_trieen(1, 2000)
    #tähän tyssää
    #skt.datan_lisaaminen_trieen(1, 3000)
    skt.datan_lisaaminen_trieen(1, 100)
    skt.kappaleen_generointi_isolla_maaralla_opetusdataa(20, 20, 1)
    return

if __name__ == "__main__":
    main()

