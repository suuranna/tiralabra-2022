from tkinter import ttk, constants

class OpetusNakyma:
    def __init__(self, juuri, lisaa_opetusdataa, takaisin_etusivulle):
        self._juuri = juuri
        self._kehys = None
        self._lisaa_opetusdataa = lisaa_opetusdataa
        self._takaisin_etusivulle = takaisin_etusivulle

        self._alusta()

    def pakkaa(self):
        self._kehys.pack(fill=constants.X)

    def tuhoa(self):
        self._kehys.destroy()

    def _alusta(self):
        self._kehys = ttk.Frame(master = self._juuri)
        otsikko = ttk.Label(master=self._kehys, text="Lisää opetusdataa")
        data = ttk.Entry(master=self._kehys)
        lisaa = ttk.Button(master=self._kehys, text="Lisää opetusdataan", command=self._lisaa_opetusdataa)
        etusivulle = ttk.Button(master=self._kehys, text="Etusivulle", command=self._takaisin_etusivulle)
        otsikko.pack()
        lisaa.pack()
        etusivulle.pack()


