from tkinter import ttk, constants, Text
from trierakenne import *

class OpetusNakyma:
    def __init__(self, juuri, takaisin_etusivulle, savelet, nuotit):
        self._juuri = juuri
        self._kehys = None
        #self._lisaa_opetusdataa = lisaa_opetusdataa
        self._savelet = savelet
        self._nuotit = nuotit
        self._takaisin_etusivulle = takaisin_etusivulle
        self._data = None

        self.alusta()

    def pakkaa(self):
        self._kehys.pack(fill=constants.X)

    def tuhoa(self):
        self._kehys.destroy()

    def lisaa_kappale_opetusdataan(self):
        data = self._data.get("1.0", 'end-1c')
        lista = data.split()
        savelet = []
        nuotit = []

        if len(lista) <= 1:
            return "Anna kappale, joka on pidempi kuin yksi nuotti/sävel"

        for alkio in lista:
            eroteltu = alkio.split("-")
            if len(eroteltu) != 2 or len(eroteltu[0]) != 2 or len(eroteltu[1]) != 1:
                print("Annettu kappale ei ollut kirjoitettu oikeassa muodossa")
                break
            #tarkista onko eroteltu[0] oikeassa muodossa oleva sävel
            #jos ei ole niin break
            savelet.append(eroteltu[0])
            nuotit.append(eroteltu[1])
        self._savelet.lisaa_kappale(savelet)
        self._nuotit.lisaa_kappale(savelet)
        print("kappale lisätty opetusdataan")
         


    def alusta(self):
        self._kehys = ttk.Frame(master=self._juuri)
        otsikko = ttk.Label(master=self._kehys, text="Lisää opetusdataa")
        self._data = Text(master=self._kehys, height=4, width=40)
        teksti = Text(master=self._kehys, height=6, width=50)
        teksti.insert('1.0', "Tässä voit lisätä kappaleen opetusdataan. Kirjoita kappale muodossa sävel-nuotti Esim. C4-1 D4-2 E4-1 jossa 1=neljäsosanuotti, 2=kahdeksasosanuotti, 3=kokonaisnuotti ja 4=pisteellinen nuotti. Sävelen jälkeinen numero kertoo miltä korkeudelta sävel soitetaan. Käytätähän isoja kirjaimia :)")
        teksti['state'] = 'disabled'
        self._data.insert('1.0', "Kirjoita tähän kappaleen sävelet ja nuotit")
        lisaa = ttk.Button(master=self._kehys, text="Lisää opetusdataan", command=self.lisaa_kappale_opetusdataan)
        etusivulle = ttk.Button(master=self._kehys, text="Etusivulle", command=self._takaisin_etusivulle)
        otsikko.pack()
        teksti.pack()
        self._data.pack()
        lisaa.pack()
        etusivulle.pack()