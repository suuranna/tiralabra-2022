from tkinter import ttk, constants
from kappaleen_luonti import soita_kappale, arvo_nuotteja, arvo_savelia

class KappaleNakyma:
    def __init__(self, juuri, takaisin_etusivulle): #, soita_generoitu_kappale, tempo):
        self._juuri = juuri
        self._kehys = None
        #self._soita_generoitu_kappale = soita_generoitu_kappale
        self._takaisin_etusivulle = takaisin_etusivulle
        self._uudenKappaleenSavelet = None
        self._uudenKappaleenNuotit = None
        self._tempo = None

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
            print("Kirjoita jokin nollaa suurempi kokonaisluku numero muodossa esim. 60")
            return
        if tempo > 0:
            #tempo = int(tempo)
            soita_kappale(self._uudenKappaleenSavelet, self._uudenKappaleenNuotit, tempo)
        else:
            print("Kirjoita jokin nollaa suurempi kokonaisluku numero muodossa esim. 60")

    def _alusta(self):
        self._kehys = ttk.Frame(master=self._juuri)
        otsikko = ttk.Label(master=self._kehys, text="Generoitu kappale on tässä")
        self._tempo = ttk.Entry(master=self._kehys)
        self._tempo.insert(0, "60")

        self._uudenKappaleenSavelet = arvo_savelia()
        self._uudenKappaleenNuotit = arvo_nuotteja()

        #soita = ttk.Button(master=self._kehys, text="soita generoitu kappale", command=self._soita_generoitu_kappale)
        soita = ttk.Button(master=self._kehys, text="soita generoitu kappale", command=self.soita_generoitu_kappale)
        etusivulle = ttk.Button(master=self._kehys, text="etusivulle", command=self._takaisin_etusivulle)
        otsikko.pack()
        self._tempo.pack()
        soita.pack()
        etusivulle.pack()



