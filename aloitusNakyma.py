from tkinter import ttk, constants

class AloitusNakyma:
    def __init__(self, juuri, nayta_generoitu_kappale, lisaa_opetusdataa):
        self._juuri = juuri
        self._kehys = None
        self._nayta_generoitu_kappale = nayta_generoitu_kappale
        self._lisaa_opetusdataa = lisaa_opetusdataa

        self._alusta()

    def pakkaa(self):
        self._kehys.pack(fill=constants.X)

    def tuhoa(self):
        self._kehys.destroy()

    def _alusta(self):
        self._kehys = ttk.Frame(master = self._juuri)
        otsikko = ttk.Label(master=self._kehys, text="Etusivu")
        opetusdataan = ttk.Button(master=self._kehys, text="lisää opetusdataa", command=self._lisaa_opetusdataa)
        generoi = ttk.Button(master=self._kehys, text="generoi uusi kappale ja siirry uuteen näkymään", command=self._nayta_generoitu_kappale)
        otsikko.pack()
        generoi.pack()
        opetusdataan.pack()


