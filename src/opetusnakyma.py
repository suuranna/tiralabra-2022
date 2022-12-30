from tkinter import ttk, Text
from viestinakyma import Viestinakyma
from opetusdataan_datan_lisaaminen import lisaa_opetusdataan_kappale
from nakyma import Nakyma

class Opetusnakyma(Nakyma):
    """Luokka, joka kuvaa opetusnäkymään, jossa voi lisätä kirjoittamansa 
    kappaleen opetusdataan, ja jonka yläluokka on luokka Nakyma

    Attributes:
        juuri: juurikomponentti
        kehys: komponentti, jonka avulla tämän näkymän komponentit pysyvät vain tässä näkymässä
        savelet: Trierakenne, joka koostuu opetusdatan sävelsekvensseistä
        nuotit: Trierakenne, joka koostuu opetusdatan nuottisekvensseistä
        takaisin_etusivulle: napin tapahtumakäsittelijä, jolla pääsee takaisin etusivulle
        data = tekstikenttään kirjoitettu kappale
    """
    def __init__(self, juuri, takaisin_etusivulle):
        """Luokan konstruktori, joka luo uuden opetusnäkymän

        Args:
            juuri: juurikomponentti
            takaisin_etusivulle: napin tapahtumakäsittelijä, jolla pääsee takaisin etusivulle
        """
        super().__init__(juuri)
        self.takaisin_etusivulle = takaisin_etusivulle
        self.data = None

        self.alusta()

    def lisaa_kappale_opetusdataan(self):
        """Lisää opetusdataan -napin tapahtumakäsittelijä, joka lisää kirjoitetun
        data.json-tiedostoon ja trierakenteisiin
        """
        viestinakyma = Viestinakyma()
        data = self.data.get("1.0", 'end-1c')

        onnistuiko_lisays = lisaa_opetusdataan_kappale(data)

        if isinstance(onnistuiko_lisays, str):
            viestinakyma.nayta_viesti(onnistuiko_lisays)
            return

        if isinstance(onnistuiko_lisays, int):
            viestinakyma.nayta_viesti("Kappale lisätty opetusdataan onnistuneesti")
            return

    def alusta(self):
        """Alustaa opetusnäkymän ja luo sen visuaaliset komponentit
        """
        self.kehys = ttk.Frame(master=self.juuri)
        otsikko = ttk.Label(
            master=self.kehys,
            text="Lisää opetusdataa")
        self.data = Text(
            master=self.kehys,
            height=6,
            width=58)
        teksti = Text(
            master=self.kehys,
            height=8,
            width=60)
        teksti.insert('1.0', "Tässä voit lisätä kappaleen opetusdataan.\
            Kirjoita kappale muodossa sävel-nuotti Esim. C4-1/4 D4-1/8 E4-1.\
            Nuotteja vastaavat merkinnät ovat: 1/4=neljäsosanuotti, 1/8=kahdeksasosanuotti,\
            1/2=puolinuotti, 3/8=pisteellinen neljännesosanuotti, 1=kokonuotti,\
            1/16=kuudestoistaosanuotti. Nuotit määrittelevät sävelen keston.\
            Sävelen jälkeinen numero kertoo miltä korkeudelta sävel soitetaan.\
            Käytätähän isoja kirjaimia :)")
        teksti['state'] = 'disabled'
        self.data.insert('1.0', "Kirjoita tähän kappaleen sävelet ja nuotit")
        lisaa = ttk.Button(
            master=self.kehys,
            text="Lisää opetusdataan",
            command=self.lisaa_kappale_opetusdataan)
        etusivulle = ttk.Button(
            master=self.kehys,
            text="Etusivulle",
            command=self.takaisin_etusivulle)
        otsikko.pack()
        teksti.pack()
        self.data.pack()
        lisaa.pack()
        etusivulle.pack()
