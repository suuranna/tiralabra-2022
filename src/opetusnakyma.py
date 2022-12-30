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
            height=15,
            width=58)
        teksti = Text(
            master=self.kehys,
            height=20,
            width=60)
        teksti.insert('1.0', "Tässä voit lisätä kappaleen opetusdataan." + "\n" +
                      "Kirjoita kappale muodossa sävel-nuotti" + "\n" +
                      "Esim. C4-1/4 D4-1/8 E4-1 F4#-1/16 G4b-1/2 C5-1" + "\n" +
                      "Sovelluksessa on käytössä seitsemän eri nuottia" + "\n" +
                      "ja ne kirjoitetaan murtolukuina." + "\n" +
                      "Nuotteja vastaavat merkinnät ovat:" + "\n" + "1=kokonuotti" + "\n" +
                      "1/2=puolinuotti" + "\n" + "1/4=neljäsosanuotti" + "\n" +
                      "1/8=kahdeksasosanuotti" + "\n" +"3/8=pisteellinen neljässosanuotti" + "\n" +
                      "1/16=kuudestoistaosanuotti" + "\n" +
                      "3/16=pisteellinen kahdeksasosanuotti" + "\n" +
                      "Nuotit määrittelevät sävelen keston. Sävelen jälkeinen" + "\n" +
                      "numero kertoo miltä korkeudelta sävel soitetaan ja sen." + "\n" +
                      "voi valita väliltä 3-5, 3 ollessa matalin ja 5 korkein" + "\n" +
                      "Alennus- ja ylennysmerkit tulevat tämän numeron jälkeen." + "\n" +
                      "Alennusmerkki on b ja ylennysmerkki on #" + "\n" +
                      "Säveliä ovat: C, D, E, F, G, A, H, B" + "\n" +
                      "Käytätähän isoja kirjaimia :)")
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
