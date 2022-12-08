from tkinter import ttk, constants, Text
from trierakenne import *
from jsonFunktiot import *

class OpetusNakyma:
    def __init__(self, juuri, takaisin_etusivulle, savelet, nuotit):
        self._juuri = juuri
        self._kehys = None
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
        nuottien_vastaavuudet = {"1/4": "1", "1/8": "2", "1/2": "3", "3/8": "4", "1/16": "5", "1": "6", "3/16": "7"}
        sallitut_savelet = ["C", "D", "E", "F", "G", "A", "H", "B"]
        sallitut_oktaavit = ["3", "4", "5"]
        data = self._data.get("1.0", 'end-1c')
        lista = data.split()
        savelet = []
        nuotit = []

        opetusdata = avaaJson()

        if len(lista) <= 1:
            print("Anna kappale, joka on pidempi kuin yksi nuotti/sävel")
            return 

        for alkio in lista:
            eroteltu = alkio.split("-")
            if len(eroteltu) != 2 or len(eroteltu[0]) < 2 or len(eroteltu[0]) > 3:
                print("Annettu kappale ei ollut kirjoitettu oikeassa muodossa")
                return
            if eroteltu[0][0] not in sallitut_savelet and eroteltu[0][1] not in sallitut_oktaavit:
                print("sävel ei ollut oikeassa muodossa")
                return
            if eroteltu[1] not in nuottien_vastaavuudet.keys():
                print("nuotti ei ollu oikeassa muodossa")
                return
            if len(eroteltu[0]) == 3:
                if eroteltu[0][2] == "#" or eroteltu[0][2] == "b":
                    savelet.append(eroteltu[0])
                    nuotit.append(nuottien_vastaavuudet[eroteltu[1]])
                    continue
                else:    
                    print("Vääränlainen ylennys- tai alennusmerkki")
                    return

            savelet.append(eroteltu[0])
            nuotit.append(nuottien_vastaavuudet[eroteltu[1]])
        self._savelet.lisaa_kappale(savelet)
        self._nuotit.lisaa_kappale(nuotit)
        opetusdata["savelet"].append(savelet)
        opetusdata["nuotit"].append(nuotit)
        tallennaJson(opetusdata)
        print("kappale lisätty opetusdataan")
         


    def alusta(self):
        self._kehys = ttk.Frame(master=self._juuri)
        otsikko = ttk.Label(master=self._kehys, text="Lisää opetusdataa")
        self._data = Text(master=self._kehys, height=4, width=40)
        teksti = Text(master=self._kehys, height=8, width=60)
        teksti.insert('1.0', "Tässä voit lisätä kappaleen opetusdataan. Kirjoita kappale muodossa sävel-nuotti Esim. C4-1/4 D4-1/8 E4-1. Nuotteja vastaavat merkinnät ovat: 1/4=neljäsosanuotti, 1/8=kahdeksasosanuotti, 1/2=puolinuotti, 3/8=pisteellinen neljännesosanuotti, 1=kokonuotti, 1/16=kuudestoistaosanuotti. Nuotit määrittelevät sävelen keston. Sävelen jälkeinen numero kertoo miltä korkeudelta sävel soitetaan. Käytätähän isoja kirjaimia :)")
        teksti['state'] = 'disabled'
        self._data.insert('1.0', "Kirjoita tähän kappaleen sävelet ja nuotit")
        lisaa = ttk.Button(master=self._kehys, text="Lisää opetusdataan", command=self.lisaa_kappale_opetusdataan)
        etusivulle = ttk.Button(master=self._kehys, text="Etusivulle", command=self._takaisin_etusivulle)
        otsikko.pack()
        teksti.pack()
        self._data.pack()
        lisaa.pack()
        etusivulle.pack()
