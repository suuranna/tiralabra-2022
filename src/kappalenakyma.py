from tkinter import ttk, constants, Text
from kappaleen_soittaminen import soita_kappale
from viestinakyma import Viestinakyma

class Kappalenakyma:
    """Luokka, joka kuvaa näkymää, jossa voi kuunnella generoidun kappaleen haluamssaan 
    tempossa ja generoida uuden kappaleen

    Attributes:
        juuri: juurikomponentti
        kehys: komponentti, jonka avulla tämän näkymän komponentit pysyvät vain tässä näkymässä
        takaisin_etusivulle: napin tapahtumakäsittelijä, jolla pääsee takaisin etusivulle
        savelet: Trierakenne, joka koostuu opetusdatan sävelsekvensseistä 
        nuotit: Trierakenne, joka koostuu opetusdatan nuottisekvensseistä
        tempo: tekstikenttään kirjoitettu tempo
        kappale: generoidun kappaleen sävelet ja nuotit tuplena
    
    """

    def __init__(self, juuri, takaisin_etusivulle, nuotit, savelet):
        """Luokan konstruktori, joka luo uuden kappalenäkymän

        Args:
            juuri: juurikomponentti
            takaisin_etusivulle: napin tapahtumakäsittelijä, jolla pääsee takaisin etusivulle
            savelet: Trierakenne, joka koostuu opetusdatan sävelsekvensseistä 
            nuotit: Trierakenne, joka koostuu opetusdatan nuottisekvensseistä

        """ 
        self.juuri = juuri
        self.kehys = None
        self.takaisin_etusivulle = takaisin_etusivulle
        self.savelet = savelet 
        self.nuotit = nuotit 
        self.tempo = None
        self.kappale = None

        self.alusta()

    def pakkaa(self):
        """Metodi, joka pakkaa näkymän visuaaliset komponentit 
        
        """
        self.kehys.pack(fill=constants.X)

    def tuhoa(self):
        """Tuhoaa kappalenäkymän, jotta toinen näkymän voidaan laittaa tilalle
        
        """
        self.kehys.destroy()

    def soita_generoitu_kappale(self):
        """Soita generoitu kappale -napin tapahtumakäsittelijä, joka soittaa generoidun kappaleen 
        halutussa tempossa
        
        """
        viestinakyma = Viestinakyma()
        tempo = self.tempo.get()
        
        soita = soita_kappale(self.kappale[0], self.kappale[1], tempo)
        if isinstance(soita, str):
            viestinakyma.nayta_viesti(soita)
            return

        viestinakyma.tuhoa()

    def generoi_uusi_kappale(self):
        """Generoi uusi kappale -napin tapahtumakäsittelijä, joka generoi uuden kappaleen
        
        """
        viestinakyma = Viestinakyma()

        savelet = self.savelet.luo_kappale(10,20)
        nuotit = self.nuotit.luo_kappale(len(savelet), len(savelet))
        self.kappale = (savelet, nuotit)

        viestinakyma.nayta_viesti("Uusi kappale on onnistuneesti generoitu! Kuuntele se painamalla 'soita generoitu kappale'-nappia")    

            
    def alusta(self):
        """Alustaa kappalenäkymän ja luo tarvittavat visuaaliset komponentit
        
        """
        self.kehys = ttk.Frame(master=self.juuri)
        otsikko = ttk.Label(master=self.kehys, text="Generoitu kappale on tässä")
        teksti = Text(master=self.kehys, height=5, width=60)
        teksti.insert('1.0', "Tässä voit kuunnella juuri generoidun kappaleen haluamassasi tempossa tai sitten generoida uuden kappaleen. Kirjoita haluamasi tempo numeromuodossa. Mitä suurempi tempo, sitä nopeampaa kappale soitetaan")
        teksti['state'] = 'disabled'
        self.tempo = ttk.Entry(master=self.kehys)
        self.tempo.insert(0, "120")

        savelet = self.savelet.luo_kappale(10,20)
        nuotit = self.nuotit.luo_kappale(len(savelet), len(savelet))
        self.kappale = (savelet, nuotit)

        soita = ttk.Button(master=self.kehys, text="soita generoitu kappale", command=self.soita_generoitu_kappale)
        generoi_uusi = ttk.Button(master=self.kehys, text="generoi uusi kappale", command=self.generoi_uusi_kappale)
        etusivulle = ttk.Button(master=self.kehys, text="siirry takaisin etusivulle", command=self.takaisin_etusivulle)
        otsikko.pack()
        teksti.pack()
        self.tempo.pack()
        soita.pack()
        generoi_uusi.pack()
        etusivulle.pack()



