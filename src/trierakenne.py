import random

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
        if self.savelet_vai_nuotit == "sävelet":
            self.lisaa_kappale(["C4","C4","G4","G4","A4","A4","G4","F4","F4","E4","E4","D4","D4","C4"])
            self.lisaa_kappale(["C4","C4","C4", "E4","D4","D4","D4", "F4","E4","E4","D4","D4","C4"])
            self.lisaa_kappale(["C4", "D4", "E4", "C4", "F4", "E4", "F4", "E4", "D4", "B3", "C4", "D4", "E4", "E4", "E4", "E4", "D4", "C4"])
        else:
            self.lisaa_kappale(["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "1"])
            self.lisaa_kappale(["1", "1", "1", "1", "1", "1", "3", "1", "1", "1", "1", "1", "1", "3"])
            self.lisaa_kappale(["2", "2", "2", "2", "4", "2", "2", "2", "4", "2", "1", "1", "1", "2", "2", "2", "1", "4"])


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
            return

        if solmu.kappaleen_loppu:
            kappale = kappale + solmu.nimi
            if savelet_vai_nuotit == "sävelet":
                if len(kappale) // 2 >= min and len(kappale) // 2 <= max:
                    #print(kappale)
                    return kappale
            elif savelet_vai_nuotit == "nuotit":
                if len(kappale) >= min and len(kappale) <= max:
                    #print(kappale)
                    return kappale
            else:
                return kappale
        lapset = solmu.lapset.values()
        maarat = []
        nimet = []
        for lapsi in lapset:
            maarat.append(lapsi.maara)
            nimet.append(lapsi.nimi)
        #print(maarat)
        for lapsi in lapset:
            #print(len(lapset))
            arvottu_solmu = random.choices(nimet, weights=maarat)
            #for i in range(len(nimet)):
            #    if nimet[i] == arvottu_solmu:
            #        nimet.pop(i)
            #        maarat.pop(i)
            
            #print(arvottu_solmu)
            #self.generoi_kappale(lapsi, kappale + solmu.nimi, min, max, savelet_vai_nuotit)
            a = self.generoi_kappale(solmu.lapset[arvottu_solmu[0]], kappale + solmu.nimi, min, max, savelet_vai_nuotit)
            #print(a)
            return a
        #print(kappale)
        #return kappale
        return None

    def luo_kappale(self, min, max):
        while True:
            kappale = self.generoi_kappale(self.alku, "", min, max, self.savelet_vai_nuotit)
            if kappale:
                break
        return kappale
