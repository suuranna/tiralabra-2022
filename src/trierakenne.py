class Solmu:
    def __init__(self, nimi):
        self.nimi = nimi
        self.kappaleen_loppu = False
        self.lapset = {}
        self.maara = 1

class TrieRakenne(object):
    def __init__(self):
        self.alku = Solmu("")

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
                    print(kappale)
            elif savelet_vai_nuotit == "nuotit":
                if len(kappale) >= min and len(kappale) <= max:
                    print(kappale)
            else:
                return
            
        for lapsi in solmu.lapset.values():
            self.kay_lapi_kaikki(lapsi, kappale + solmu.nimi, min, max, savelet_vai_nuotit)
