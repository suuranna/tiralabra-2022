from json_funktiot import avaa_json
from solmu import Solmu
from arpoja import Arpoja
from collections import deque

class TrieRakenne:
    """Luokka, joka kuvaa Trie-rakennetta

    Attributes:
        alku: Trie-rakenteen juurisolmu
        savelet_vai_nuotit: String-muodossa joko "sävelet" tai "nuotit" kertomassa,
            onko Trie-rakenteessa nuotteja vai säveliä
        pisin: pitää kirjaa siitä, mikä on opetusdatan pisin kappale ja pisin
            mahdollinen generoitava kappale
        arpoja: hoitaa satumanvaraisen valinnan
    """
    def __init__(self, savelet_vai_nuotit):
        """Luokan konstruktori, joka luo uuden Trie-rakenteen

        Args:
            savelet_vai_nuotit: String-muodossa joko "sävelet" tai "nuotit" kertomassa,
                onko Trie-rakenteessa nuotteja vai säveliä
        """
        self.alku = Solmu("")
        self.savelet_vai_nuotit = savelet_vai_nuotit
        self.pisin = 0

    def lisaa_opetusdata_trieen(self, aste):
        """Alustaa Trie-rakenteen siten, että lisätään Trie-rakenteenseen
        data.json-tiedostossa olevat opetusdatan kappaleet
        """
        data = avaa_json()
        if self.savelet_vai_nuotit == "sävelet":
            for savelet in data["savelet"]:
                self.lisaa_kappale(aste, savelet)
        else:
            for nuotit in data["nuotit"]:
                self.lisaa_kappale(aste, nuotit)

    def lisaa_kappale(self, aste, kappale):
        if aste + 1 > len(kappale):
            return
        if len(kappale) > self.pisin:
            self.pisin = len(kappale)
        solmu = self.alku

        for indeksi in range(len(kappale) - aste):
            solmu = self.alku
            i = indeksi
            while i < indeksi + aste + 1:
                try:
                    solmu.lapset[kappale[i]].maara += 1
                    solmu = solmu.lapset[kappale[i]]
                except KeyError:
                    uusi_solmu = Solmu(kappale[i])
                    solmu.lapset[kappale[i]] = uusi_solmu
                    solmu = solmu.lapset[kappale[i]]
                i += 1
            solmu.kappaleen_loppu = True

    def etsi_sekvenssin_seuraajat(self, sekvenssi):
        seuraajat = []
        frekvenssit = []

        solmu = self.alku

        for alkio in sekvenssi:
            try:
                solmu = solmu.lapset[alkio]
            except KeyError:
                return "Tällä sekvenssillä ei ole seuraajia"
        
        for lapsi in solmu.lapset:
            seuraajat.append(lapsi)
            frekvenssit.append(solmu.lapset[lapsi].maara)

        return (seuraajat, frekvenssit)

