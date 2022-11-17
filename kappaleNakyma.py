from tkinter import ttk, constants

class KappaleNakyma:
    def __init__(self, juuri, soita_generoitu_kappale, takaisin_etusivulle):
        self._juuri = juuri
        self._kehys = None
        self._soita_generoitu_kappale = soita_generoitu_kappale
        self._takaisin_etusivulle = takaisin_etusivulle

        self._alusta()

    def pakkaa(self):
        self._kehys.pack(fill=constants.X)

    def tuhoa(self):
        self._kehys.destroy()

    def _alusta(self):
        self._kehys = ttk.Frame(master=self._juuri)
        otsikko = ttk.Label(master=self._kehys, text="Generoitu kappale on tässä")
        tempo = ttk.Entry(master=self._kehys)
        tempo.insert(0, "60")

        soita = ttk.Button(master=self._kehys, text="soita generoitu kappale", command=self._soita_generoitu_kappale)
        etusivulle = ttk.Button(master=self._kehys, text="etusivulle", command=self._takaisin_etusivulle)
        otsikko.pack()
        tempo.pack()
        soita.pack()
        etusivulle.pack()



