from tkinter import ttk, Text
from kappaleen_soittaminen import soita_kappale
from viestinakyma import Viestinakyma
from nakyma import Nakyma

class Kappalenakyma(Nakyma):
    """Luokka, joka kuvaa näkymää, jossa voi kuunnella generoidun kappaleen haluamssaan
    tempossa ja generoida uuden kappaleen. Tämän luokan yläluokka on luokka Nakyma

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
        super().__init__(juuri)
        self.takaisin_etusivulle = takaisin_etusivulle
        self.savelet = savelet
        self.nuotit = nuotit
        self.tempo = None
        self.aste = None
        self.kappale = None

        self.alusta()

    def soita_generoitu_kappale(self):
        """Soita generoitu kappale -napin tapahtumakäsittelijä, joka soittaa generoidun kappaleen
        halutussa tempossa
        """
        viestinakyma = Viestinakyma()

        if self.kappale == None:
            viestinakyma.nayta_viesti("Mitään kappaletta ei ole vielä generoitu.")
            return

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

        aste = self.aste.get()

        savelet = self.savelet.generoi_kappale(aste, 20)
        nuotit = self.nuotit.generoi_kappale(aste, 20)

        if isinstance(savelet, str) or isinstance(nuotit, str):
            viestinakyma.nayta_viesti(savelet)
            return

        self.kappale = (savelet, nuotit)

        viestinakyma.nayta_viesti("Uusi kappale on onnistuneesti generoitu! \
            Kuuntele se painamalla 'soita generoitu kappale'-nappia")

    def alusta(self):
        """Alustaa kappalenäkymän ja luo tarvittavat visuaaliset komponentit
        """
        self.kehys = ttk.Frame(master=self.juuri)
        otsikko = ttk.Label(
            master=self.kehys,
            text="Generoi uusi kappale ja kuuntele se")
        teksti = Text(
            master=self.kehys,
            height=5,
            width=60)
        teksti.insert('1.0', "Tässä voit kuunnella juuri generoidun kappaleen \
            haluamassasi tempossa tai sitten generoida uuden kappaleen. \
            Generoidaksesi uuden kappaleen sinun tulee valita aste \
            Kirjoita aste numeromuodossa \
            Kirjoita haluamasi tempo numeromuodossa. \
            Mitä suurempi tempo, sitä nopeampaa kappale soitetaan")
        teksti['state'] = 'disabled'
        self.aste = ttk.Entry(master=self.kehys)
        self.aste.insert(0, "10")
        generoi_uusi = ttk.Button(
            master=self.kehys,
            text="generoi uusi kappale",
            command=self.generoi_uusi_kappale)
        self.tempo = ttk.Entry(master=self.kehys)
        self.tempo.insert(0, "120")

        soita = ttk.Button(
            master=self.kehys,
            text="soita generoitu kappale",
            command=self.soita_generoitu_kappale)
        generoi_uusi = ttk.Button(
            master=self.kehys,
            text="generoi uusi kappale",
            command=self.generoi_uusi_kappale)
        etusivulle = ttk.Button(
            master=self.kehys,
            text="siirry takaisin etusivulle",
            command=self.takaisin_etusivulle)
        otsikko.pack()
        teksti.pack()
        self.aste.pack()
        generoi_uusi.pack()
        self.tempo.pack()
        soita.pack()
        etusivulle.pack()
