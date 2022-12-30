from tkinter import ttk, Text
from nakyma import Nakyma

class Aloitusnakyma(Nakyma):
    """Luokka, joka kuvaa aloitusnäkymää eli etusivua, joka aukeaa ensimmäisenä,
    kun sovelluksen käynnistää, ja jonka yläluokka on luokka Nakyma

    Attributes:
        juuri: juurikomponentti
        kehys: komponentti, jonka avulla tämän näkymän komponentit pysyvät vain
            tässä näkymässä
        nayta_generoitu_kappale: generoi-napin tapahtumakäsittelijä,
            jolla voi generoida uuden kappaleen ja siirtyä kappalenäkymään
        lisaa_opetusdataa: lisaa opetusdataa -napin tapahtumakäsittelijä,
            jolla voi siirtyä opetusnäkymään
    """
    def __init__(self, juuri, nayta_generoitu_kappale, lisaa_opetusdataa):
        """Luoka konstruktori, jolla voi luoda uuden aloitusnäkymän

        Args:
            juuri: juurikomponetti
            nayta_generoitu_kappale: generoi-napin tapahtumakäsittelijä,
                jolla voi generoida uuden kappaleen ja siirtyä kappalenäkymään
            lisaa_opetusdataa: lisaa opetusdataa -napin tapahtumakäsittelijä,
                jolla voi siirtyä opetusnäkymään
        """
        super().__init__(juuri)
        self.nayta_generoitu_kappale = nayta_generoitu_kappale
        self.lisaa_opetusdataa = lisaa_opetusdataa

        self.alusta()

    def alusta(self):
        """Alustaa aloitusnäkymän ja luo tarvittavat visuaaliset komponentit
        """
        self.kehys = ttk.Frame(master=self.juuri)
        otsikko = ttk.Label(
            master=self.kehys,
            text="Etusivu")
        teksti = Text(
            master=self.kehys,
            height=3,
            width=60)
        teksti.insert('1.0', "Tervetuloa sovellukseen! :) Tässä sovelluksessa voit joko " + "\n" +
                      "generoida uuden kappaleen ja kuunnella sen tai" + "\n" +
                      "lisätä opetusdataan tietämiäsi kappaleita.")
        teksti['state'] = 'disabled'
        opetusdataan = ttk.Button(
            master=self.kehys,
            text="Lisää opetusdataa",
            command=self.lisaa_opetusdataa)
        generoi = ttk.Button(
            master=self.kehys,
            text="Generoi uusi kappale",
            command=self.nayta_generoitu_kappale)
        otsikko.pack()
        teksti.pack()
        generoi.pack()
        opetusdataan.pack()
