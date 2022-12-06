from tkinter import ttk, constants
from kappaleen_soittaminen import soita_kappale
from trierakenne import *

class KappaleNakyma:
    def __init__(self, juuri, takaisin_etusivulle, nuotit, savelet): 
        self._juuri = juuri
        self._kehys = None
        self._takaisin_etusivulle = takaisin_etusivulle
        self._savelet = savelet 
        self._nuotit = nuotit 
        self._tempo = None
        self._kappale = None

        self._alusta()

    def pakkaa(self):
        self._kehys.pack(fill=constants.X)

    def tuhoa(self):
        self._kehys.destroy()

    def soita_generoitu_kappale(self):
        tempo = self._tempo.get()
        try:
            tempo = int(tempo)
        except:
            print("Kirjoita jokin nollaa suurempi kokonaisluku numeromuodossa esim. 60")
            return
        if tempo > 0:
            soita_kappale(self._kappale[0], self._kappale[1], tempo)
        else:
            print("Kirjoita jokin nollaa suurempi kokonaisluku numeromuodossa esim. 60")

            
    def _alusta(self):
        self._kehys = ttk.Frame(master=self._juuri)
        otsikko = ttk.Label(master=self._kehys, text="Generoitu kappale on tässä")
        self._tempo = ttk.Entry(master=self._kehys)
        self._tempo.insert(0, "120")

        savelet = self._savelet.luo_kappale(9,20)
        nuotit = self._nuotit.luo_kappale(len(savelet), len(savelet))
        self._kappale = (savelet, nuotit)

        soita = ttk.Button(master=self._kehys, text="soita generoitu kappale", command=self.soita_generoitu_kappale)
        etusivulle = ttk.Button(master=self._kehys, text="etusivulle", command=self._takaisin_etusivulle)
        otsikko.pack()
        self._tempo.pack()
        soita.pack()
        etusivulle.pack()



