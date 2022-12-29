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
        self.arpoja = Arpoja()

    def alusta(self, aste):
        """Alustaa Trie-rakenteen siten, että lisätään Trie-rakenteenseen
        data.json-tiedostossa olevat opetusdatan kappaleet
        """
        self.alku = Solmu("")

        data = avaa_json()
        if self.savelet_vai_nuotit == "sävelet":
            for savelet in data["savelet"]:
                self.lisaa_kappale(aste, savelet)
        else:
            for nuotit in data["nuotit"]:
                self.lisaa_kappale(aste, nuotit)

    def kay_lapi_kaikki(self, solmu):
        print("tämä solmu on: " + str(solmu.nimi))
        print("ja sen lapsia ovat:")
        for lapsi in solmu.lapset.keys():
            print(lapsi + ", ja sen määrä on: " + str(solmu.lapset[lapsi].maara))
        print("--------")
        for lapsi in solmu.lapset.keys():
            self.kay_lapi_kaikki(solmu.lapset[lapsi])

    def lisaa_kappale(self, aste, kappale):
        if aste + 1 > len(kappale):
            return
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
        print(sekvenssi)
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

        print(seuraajat)

        return (seuraajat, frekvenssit)

    def generoi_kappale(self, aste, pituus):
        try:
            aste = int(aste)
        except ValueError:
            return "Kirjoita aste numeromuodossa esim. 10"

        self.alusta(aste)

        kappale = []
        edelliset = deque([])

        for i in range(aste):
            seuraajat = self.etsi_sekvenssin_seuraajat(edelliset)
            seuraaja = self.arpoja.arvo(seuraajat[0], seuraajat[1])
            kappale.append(seuraaja)
            edelliset.append(seuraaja)

        while len(kappale) < pituus:
            seuraajat = self.etsi_sekvenssin_seuraajat(edelliset)

            if isinstance(seuraajat, str):
                try:
                    kappale.pop()
                    edelliset.popleft()
                    edelliset.append(kappale[len(kappale) - 1])
                    continue
                except IndexError:
                    continue

            seuraaja = self.arpoja.arvo(seuraajat[0], seuraajat[1])

            kappale.append(seuraaja)

            if len(edelliset) == aste:
                edelliset.popleft()
                edelliset.append(seuraaja)
            else:
                edelliset.append(seuraaja)
        return kappale
