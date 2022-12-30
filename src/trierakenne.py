from json_funktiot import avaa_json
from solmu import Solmu

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
        """Metodi, jolla lisätään Trie-rakenteenseen
        data.json-tiedostossa olevat opetusdatan kappaleet
        halutulla asteella
        """
        data = avaa_json()
        if self.savelet_vai_nuotit == "sävelet":
            for savelet in data["savelet"]:
                self.lisaa_kappale(aste, savelet)
        else:
            for nuotit in data["nuotit"]:
                self.lisaa_kappale(aste, nuotit)

    def lisaa_kappale(self, aste, kappale):
        """Metodi, joka lisää trieen annetusta kappaleesta
        aste + 1 -mittaisia sekvenssejä

        Args:
            aste: määrittää, minkä mittaisia sekvenssejä
                trieen lisätään
            kappale: lista säveliä/nuotteja

        Returns:
            None, jos aste +1 on suurempi kuin kappaleen pituus
        """
        if aste + 1 > len(kappale):
            return None
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
        """Metodi, joka etsii triestä halutun sekvenssin
        seuraajat

        Args:
            sekvenssi: lista sävelistä/nuoteista, jonka seuraajia
                etsitään

        Returns:
            string, jos annetulla sekvenssillä ei ole seuraajia
            tuple, (jossa on seuraajat listana ja niiden määrät listana),
                jos sekvenssille löytyy seuraajia
        """
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
