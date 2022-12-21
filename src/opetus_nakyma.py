from tkinter import ttk, constants, Text
from viestinakyma import Viestinakyma
from opetusdataan_datan_lisaaminen import lisaa_opetusdataan_kappale

class OpetusNakyma:
    """Luokka, joka kuvaa opetusnäkymään, jossa voi lisätä kirjoittamansa kappaleen opetusdataan

    Attributes:
        juuri: juurikomponentti
        kehys: komponentti, jonka avulla tämän näkymän komponentit pysyvät vain tässä näkymässä
        savelet: Trierakenne, joka koostuu opetusdatan sävelsekvensseistä 
        nuotit: Trierakenne, joka koostuu opetusdatan nuottisekvensseistä
        takaisin_etusivulle: napin tapahtumakäsittelijä, jolla pääsee takaisin etusivulle
        data = tekstikenttään kirjoitettu kappale
    
    """
    def __init__(self, juuri, takaisin_etusivulle, savelet, nuotit):
        """Luokan konstruktori, joka luo uuden opetusnäkymän

        Args:
            juuri: juurikomponentti
            savelet: Trierakenne, joka koostuu opetusdatan sävelsekvensseistä 
            nuotit: Trierakenne, joka koostuu opetusdatan nuottisekvensseistä
            takaisin_etusivulle: napin tapahtumakäsittelijä, jolla pääsee takaisin etusivulle

        """
        self.juuri = juuri
        self.kehys = None
        self.savelet = savelet
        self.nuotit = nuotit
        self.takaisin_etusivulle = takaisin_etusivulle
        self.data = None

        self.alusta()

    def pakkaa(self):
        """Metodi, joka pakkaa näkymän visuaaliset komponentit 
        
        """
        self.kehys.pack(fill=constants.X)

    def tuhoa(self):
        """Tuhoaa opetusnäkymän, jotta toinen näkymän voidaan laittaa tilalle
        
        """
        self.kehys.destroy()

    def lisaa_kappale_opetusdataan(self):
        """Lisää opetusdataan -napin tapahtumakäsittelijä, joka lisää kirjoitetun data.json-tiedostoon
        ja trierakenteisiin
        
        """
        viestinakyma = Viestinakyma()
        data = self.data.get("1.0", 'end-1c')

        savelet_ja_nuotit = lisaa_opetusdataan_kappale(data)

        if isinstance(savelet_ja_nuotit, str):
            viestinakyma.nayta_viesti(savelet_ja_nuotit)
            return
        
        if isinstance(savelet_ja_nuotit, tuple):
            self.savelet.lisaa_kappale(savelet_ja_nuotit[0])
            self.nuotit.lisaa_kappale(savelet_ja_nuotit[1])

        viestinakyma.nayta_viesti("kappale lisätty opetusdataan")

    def alusta(self):
        """Alustaa opetusnäkymän ja luo sen visuaaliset komponentit
        
        """
        self.kehys = ttk.Frame(master=self.juuri)
        otsikko = ttk.Label(master=self.kehys, text="Lisää opetusdataa")
        self.data = Text(master=self.kehys, height=6, width=58)
        teksti = Text(master=self.kehys, height=8, width=60)
        teksti.insert('1.0', "Tässä voit lisätä kappaleen opetusdataan. Kirjoita kappale muodossa sävel-nuotti Esim. C4-1/4 D4-1/8 E4-1. Nuotteja vastaavat merkinnät ovat: 1/4=neljäsosanuotti, 1/8=kahdeksasosanuotti, 1/2=puolinuotti, 3/8=pisteellinen neljännesosanuotti, 1=kokonuotti, 1/16=kuudestoistaosanuotti. Nuotit määrittelevät sävelen keston. Sävelen jälkeinen numero kertoo miltä korkeudelta sävel soitetaan. Käytätähän isoja kirjaimia :)")
        teksti['state'] = 'disabled'
        self.data.insert('1.0', "Kirjoita tähän kappaleen sävelet ja nuotit")
        lisaa = ttk.Button(master=self.kehys, text="Lisää opetusdataan", command=self.lisaa_kappale_opetusdataan)
        etusivulle = ttk.Button(master=self.kehys, text="Etusivulle", command=self.takaisin_etusivulle)
        otsikko.pack()
        teksti.pack()
        self.data.pack()
        lisaa.pack()
        etusivulle.pack()
