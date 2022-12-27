from json_funktiot import avaa_json
from solmu import Solmu
from arpoja import Arpoja

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

    def alusta(self):
        """Alustaa Trie-rakenteen siten, että lisätään Trie-rakenteenseen
        data.json-tiedostossa olevat opetusdatan kappaleet
        """
        data = avaa_json()
        if self.savelet_vai_nuotit == "sävelet":
            for savelet in data["savelet"]:
                self.lisaa_kappale(savelet)
        else:
            for nuotit in data["nuotit"]:
                self.lisaa_kappale(nuotit)


    def lisaa_kappale(self, kappale):
        """Lisää annetun kappaleen Trie-rakenteeseen

        Args:
            kappale: sävelet tai nuotit listana
        """
        if len(kappale) > self.pisin:
            self.pisin = len(kappale)

        solmu = None
        for indeksi in range(len(kappale)):
            solmu = self.alku
            i = indeksi
            while i < len(kappale):
                try:
                    solmu.lapset[kappale[i]].maara += 1
                    solmu = solmu.lapset[kappale[i]]
                except KeyError:
                    uusi_solmu = Solmu(kappale[i])
                    solmu.lapset[kappale[i]] = uusi_solmu
                    solmu = solmu.lapset[kappale[i]]
                i += 1
            solmu.kappaleen_loppu = True


    def generoi_kappale(self, solmu, kappale, minimi, maksimi):
        """Generoi uuden kappaleen

        Args:
            solmu: solmu, josta aloitetaan/jatketaan
            kappale: lista sävelistä/nuoteista
            minimi: generoitavan kappaleen minimipituus
            maksimi: generoitavan kappaleen maksimipituus

        Returns:
            None, jos minimi ja maksimi on virheellisiä tai jos ei ole mahdollista
                generoida kappaletta.
            -1, jos kappaleen pituus tulee ylittämään maksimin
            -2, jos tullaan loppusolmuun, mutta pituusvaatimukset eivät täyty
            listana sävelet/soinnut, jos on löydetty pituusvaatimuksia vastaava kappale
        """
        if minimi < 1 or maksimi < minimi or maksimi < 0 \
            or maksimi > self.pisin or minimi > self.pisin:
            return None

        if solmu.nimi != "":
            kappale.append(solmu.nimi)

        if len(kappale) == maksimi and not solmu.kappaleen_loppu:
            kappale.pop()
            return -1

        if solmu.kappaleen_loppu:
            if len(kappale) >= minimi and len(kappale) <= maksimi:
                return kappale

        lapset = solmu.lapset.values()
        maarat = []
        nimet = []
        for lapsi in lapset:
            maarat.append(lapsi.maara)
            nimet.append(lapsi.nimi)

        while len(nimet) > 0:
            if len(lapset) == 0:
                kappale.pop()
                break
            arvottu_solmu = self.arpoja.arvo(nimet, maarat)
            for i in range(len(nimet)):
                if nimet[i] == arvottu_solmu:
                    nimet.pop(i)
                    maarat.pop(i)
                    break
            generoitu_kappale = self.generoi_kappale(
                solmu.lapset[arvottu_solmu],
                kappale,
                minimi,
                maksimi)

            if isinstance(generoitu_kappale, int):
                if generoitu_kappale == -1:
                    break
            if isinstance(generoitu_kappale, list):
                return generoitu_kappale
            if len(lapset) == 0:
                kappale.pop()
                break
            kappale.pop()
        return None

    def luo_kappale(self, minimi, maksimi):
        """Metodi, joka generoi kappaletta niin pitkään, kunnes kappale, joka on minimin
        ja maksimin mukainen pituudeltaan, on generoitu

        Args:
            minimi: kappaleen minimipituus
            maksimi: kappaleen amksimipituus

        Returns:
            None, jos annetut min ja max ovat virheellisiä
            Listana säveliä/nuotteja, jos generointi menee niin kuin pitää
        """
        if minimi < 1 or maksimi < minimi or maksimi < 0 \
            or maksimi > self.pisin or minimi > self.pisin:
            return None
        kappale = self.generoi_kappale(self.alku, [], minimi, maksimi)
        return kappale
