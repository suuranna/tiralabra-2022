from json_funktiot import avaaJson
from solmu import Solmu
from arpoja import Arpoja

class TrieRakenne(object):
    """Luokka, joka kuvaa Trie-rakennetta

    Attributes:
        alku: Trie-rakenteen juurisolmu
        savelet_vai_nuotit: String-muodossa joko "sävelet" tai "nuotit" kertomassa, 
            onko Trie-rakenteessa nuotteja vai säveliä
        pisin: pitää kirjaa siitä, mikä on opetusdatan pisin kappale ja pisin mahdollinen generoitava kappale
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
        #self.alusta()

    def alusta(self):
        """Alustaa Trie-rakenteen siten, että lisätään Trie-rakenteenseen data.json-tiedostossa olevat
        opetusdatan kappaleet
        
        """
        data = avaaJson()
        if self.savelet_vai_nuotit == "sävelet":
            for s in data["savelet"]:
                self.lisaa_kappale(s)
        else:
            for n in data["nuotit"]:
                self.lisaa_kappale(n)


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
                except:
                    uusi_solmu = Solmu(kappale[i])
                    solmu.lapset[kappale[i]] = uusi_solmu
                    solmu = uusi_solmu
                i += 1
            solmu.kappaleen_loppu = True

    def generoi_kappale(self, solmu, kappale, min, max):
        """Generoi uuden kappaleen 

        Args:
            solmu: solmu, josta aloitetaan/jatketaan
            kappale: lista sävelistä/nuoteista
            min: generoitavan kappaleen minimipituus
            max: generoitavan kappaleen maksimipituus
        
        Returns:
            None, jos min ja max on virheellisiä tai jos ei ole mahdollista generoida kappaletta.
            -1, jos kappaleen pituus tulee ylittämään maksimin
            -2, jos tullaan loppusolmuun, mutta pituusvaatimukset eivät täyty
            listana sävelet/soinnut, jos on löydetty pituusvaatimuksia vastaava kappale

        """
        if min < 1 or max < min or max < 0 or max > self.pisin or min > self.pisin:
            return 

        if solmu.nimi != "":
            kappale.append(solmu.nimi)
        
        if len(kappale) == max and not solmu.kappaleen_loppu:
            kappale.pop()
            return -1 

        if solmu.kappaleen_loppu:
            if len(kappale) >= min and len(kappale) <= max:
                return kappale
            else:
                return -2

        lapset = solmu.lapset.values()
        maarat = []
        nimet = []
        for lapsi in lapset:
            maarat.append(lapsi.maara)
            nimet.append(lapsi.nimi)

        while len(nimet) > 0:
            arvottu_solmu = self.arpoja.arvo(nimet, maarat)
            for i in range(len(nimet)):
                if nimet[i] == arvottu_solmu:
                    nimet.pop(i)
                    maarat.pop(i)
                    break
            generoitu_kappale = self.generoi_kappale(solmu.lapset[arvottu_solmu], kappale, min, max)

            if isinstance(generoitu_kappale, int):
                if generoitu_kappale == -1:
                    break
                if generoitu_kappale == -2:
                    continue
            if isinstance(generoitu_kappale, list):
                return generoitu_kappale
            if len(lapset) == 0:
                kappale.pop()
                break
 
        return 


    def luo_kappale(self, min, max):
        """Metodi, joka generoi kappaletta niin pitkään, kunnes kappale, joka on minimin 
        ja maksimin mukainen pituudeltaan, on generoitu

        Args:
            min: kappaleen minimipituus
            max: kappaleen amksimipituus

        Returns:
            None, jos annetut min ja max ovat virheellisiä
            Listana säveliä/nuotteja, jos generointi menee niin kuin pitää

        
        """
        if min < 1 or max < min or max < 0 or max > self.pisin or min > self.pisin:
            return 
        kappale = []
        while True:
            kappale = self.generoi_kappale(self.alku, [], min, max)
            if kappale:
                break
        return kappale
