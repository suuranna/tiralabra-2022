from tkinter import ttk, Text
from kappaleen_soittaminen import soita_kappale
from kappaleen_generoiminen import generoi_kappale
from viestinakyma import Viestinakyma
from nakyma import Nakyma

class Kappalenakyma(Nakyma):
    """Luokka, joka kuvaa näkymää, jossa voi kuunnella generoidun kappaleen haluamssaan
    tempossa ja generoida uuden kappaleen. Tämän luokan yläluokka on luokka Nakyma

    Attributes:
        juuri: juurikomponentti
        kehys: komponentti, jonka avulla tämän näkymän komponentit pysyvät vain tässä näkymässä
        takaisin_etusivulle: napin tapahtumakäsittelijä, jolla pääsee takaisin etusivulle
        tempo: tekstikenttään kirjoitettu tempo
        kappale: generoidun kappaleen sävelet ja nuotit tuplena
    """
    def __init__(self, juuri, takaisin_etusivulle):
        """Luokan konstruktori, joka luo uuden kappalenäkymän

        Args:
            juuri: juurikomponentti
            takaisin_etusivulle: napin tapahtumakäsittelijä, jolla pääsee takaisin etusivulle
        """
        super().__init__(juuri)
        self.takaisin_etusivulle = takaisin_etusivulle
        self.tempo = None
        self.aste = None
        self.kappaleen_pituus = None
        self.kappale = None

        self.alusta()

    def soita_generoitu_kappale(self):
        """Soita generoitu kappale -napin tapahtumakäsittelijä, joka soittaa generoidun kappaleen
        halutussa tempossa
        """
        viestinakyma = Viestinakyma()

        if self.kappale is None:
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
        kappaleen_pituus = self.kappaleen_pituus.get()

        savelet = generoi_kappale(aste, kappaleen_pituus, "sävelet")
        nuotit = generoi_kappale(aste, kappaleen_pituus, "nuotit")

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
            height=8,
            width=60)
        teksti.insert('1.0', "Tässä voit kuunnella juuri generoidun kappaleen" + "\n" +
                      "haluamassasi tempossa tai sitten generoida uuden kappaleen." + "\n" +
                      "Generoidaksesi uuden kappaleen sinun tulee valita aste ja" + "\n" +
                      "kappaleen pituus. Kirjoita aste ja pituus numeromuodossa." + "\n" +
                      "Generoituasi kappaleen voit kuunnella generoidun kappaleen" + "\n" +
                      "haluamassasi tempossa." + "\n" +
                      "Kirjoita haluamasi tempo numeromuodossa." + "\n" +
                      "Mitä suurempi tempo, sitä nopeampaa kappale soitetaan")
        teksti['state'] = 'disabled'
        aste_teksti = Text(
            master=self.kehys,
            height=1,
            width=23)
        aste_teksti.insert('1.0', " Valitse aste, esim. 8")
        aste_teksti['state'] = 'disabled'
        self.aste = ttk.Entry(master=self.kehys)
        self.aste.insert(0, "10")
        pituus_teksti = Text(
            master=self.kehys,
            height=1,
            width=49)
        pituus_teksti.insert('1.0', " Valitse generoitavan kappaleen pituus, esim. 20")
        pituus_teksti['state'] = 'disabled'
        self.kappaleen_pituus = ttk.Entry(master=self.kehys)
        self.kappaleen_pituus.insert(0, "20")
        generoi_uusi = ttk.Button(
            master=self.kehys,
            text="Generoi uusi kappale",
            command=self.generoi_uusi_kappale)
        tempo_teksti = Text(
            master=self.kehys,
            height=1,
            width=25)
        tempo_teksti.insert('1.0', " Valitse tempo, esim. 60")
        tempo_teksti['state'] = 'disabled'
        self.tempo = ttk.Entry(master=self.kehys)
        self.tempo.insert(0, "120")

        soita = ttk.Button(
            master=self.kehys,
            text="Soita generoitu kappale",
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
        aste_teksti.pack()
        self.aste.pack()
        pituus_teksti.pack()
        self.kappaleen_pituus.pack()
        generoi_uusi.pack()
        tempo_teksti.pack()
        self.tempo.pack()
        soita.pack()
        etusivulle.pack()
