from tkinter import ttk, constants, Text

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
        self._kehys = ttk.Frame(master=self._juuri)
        otsikko = ttk.Label(master=self._kehys, text="Lisää opetusdataa")
        data = Text(master=self._kehys, height=4, width=40)
        teksti = Text(master=self._kehys, height=6, width=50)
        teksti.insert('1.0', "Tässä voit lisätä kappaleen opetusdataan. Kirjoita kappale muodossa sävel-nuotti Esim. C4-1 D4-2 E4-1 jossa 1=neljäsosanuotti, 2=kahdeksasosanuotti, 3=kokonaisnuotti ja 4=pisteellinen nuotti. Sävelen jälkeinen numero kertoo miltä korkeudelta sävel soitetaan. Käytätähän isoja kirjaimia :)")
        teksti['state'] = 'disabled'
        data.insert('1.0', "Kirjoita tähän kappaleen sävelet ja nuotit")
        lisaa = ttk.Button(master=self._kehys, text="Lisää opetusdataan", command=self._lisaa_opetusdataa)
        etusivulle = ttk.Button(master=self._kehys, text="Etusivulle", command=self._takaisin_etusivulle)
        otsikko.pack()
        teksti.pack()
        data.pack()
        lisaa.pack()
        etusivulle.pack()