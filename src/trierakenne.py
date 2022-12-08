import random
from jsonFunktiot import *

class Solmu:
    def __init__(self, nimi):
        self.nimi = nimi
        self.kappaleen_loppu = False
        self.lapset = {}
        self.maara = 1

class TrieRakenne(object):
    def __init__(self, savelet_vai_nuotit):
        self.alku = Solmu("")
        self.savelet_vai_nuotit = savelet_vai_nuotit
        self.alusta()

    def alusta(self):
        data = avaaJson()
        if self.savelet_vai_nuotit == "sävelet":
            for s in data["savelet"]:
                self.lisaa_kappale(s)
            #self.lisaa_kappale(["C4","C4","G4","G4","A4","A4","G4","F4","F4","E4","E4","D4","D4","C4"])
            #self.lisaa_kappale(["C4","C4","C4", "E4","D4","D4","D4", "F4","E4","E4","D4","D4","C4"])
            #self.lisaa_kappale(["C4", "D4", "E4", "C4", "F4", "E4", "F4", "E4", "D4", "B3", "C4", "D4", "E4", "E4", "E4", "E4", "D4", "C4"])
        else:
            for n in data["nuotit"]:
                self.lisaa_kappale(n)
            #self.lisaa_kappale(["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "1"])
            #self.lisaa_kappale(["1", "1", "1", "1", "1", "1", "3", "1", "1", "1", "1", "1", "1", "3"])
            #self.lisaa_kappale(["2", "2", "2", "2", "4", "2", "2", "2", "4", "2", "1", "1", "1", "2", "2", "2", "1", "4"])


    def lisaa_kappale(self, kappale):
        solmu = None
        for indeksi in range(len(kappale)):
            solmu = self.alku
            i = indeksi
            while i < len(kappale):
                if kappale[i] in solmu.lapset:
                    solmu.lapset[kappale[i]].maara += 1
                    solmu = solmu.lapset[kappale[i]]
                else:
                    uusi_solmu = Solmu(kappale[i])
                    solmu.lapset[kappale[i]] = uusi_solmu
                    solmu = uusi_solmu
                i += 1
            solmu.kappaleen_loppu = True

    def generoi_kappale(self, solmu, kappale, min, max, savelet_vai_nuotit):
        if min < 0 or max < min or max < 0:
            return None

        if solmu.kappaleen_loppu:
            kappale = kappale + solmu.nimi
            if savelet_vai_nuotit == "sävelet":
                if len(kappale) // 2 >= min and len(kappale) // 2 <= max:
                    return kappale
            elif savelet_vai_nuotit == "nuotit":
                if len(kappale) >= min and len(kappale) <= max:
                    return kappale
            else:
                return None

        if not solmu.kappaleen_loppu:
            if savelet_vai_nuotit == "sävelet":
                if len(kappale) // 2 > max:
                    return None
            if savelet_vai_nuotit == "nuotit":
                if len(kappale) > max:
                    return None
                    
        lapset = solmu.lapset.values()
        maarat = []
        nimet = []
        for lapsi in lapset:
            maarat.append(lapsi.maara)
            nimet.append(lapsi.nimi)
        while len(nimet) > 0:
            arvottu_solmu = random.choices(nimet, weights=maarat)
            for i in range(len(nimet)):
                if nimet[i] == arvottu_solmu[0]:
                    nimet.pop(i)
                    maarat.pop(i)
                    break

            a = self.generoi_kappale(solmu.lapset[arvottu_solmu[0]], kappale + solmu.nimi, min, max, savelet_vai_nuotit)
            if a:
                return a
        return None


    def luo_kappale(self, min, max):
        kappale = self.generoi_kappale(self.alku, "", min, max, self.savelet_vai_nuotit)
        kappale_listana = []

        if self.savelet_vai_nuotit == "sävelet":
            i = 0
            while i < len(kappale):
                savel = ""
                savel = savel + kappale[i] + kappale[i+1]
                if i + 2 < len(kappale):
                    if kappale[i+2] == "#" or kappale[i+2] == "b":
                        savel = savel + kappale[i+2]
                        i = i + 3
                kappale_listana.append(savel)
                i = i + 2
        else:
            kappale_listana = list(kappale)

        return kappale_listana
