from tkinter import ttk, constants, Text

class Aloitusnakyma:
    """Luokka, joka kuvaa aloitusnäkymää eli etusivua, joka aukeaa ensimmäisenä, kun sovelluksen käynnistää

    Attributes:
        juuri: juurikomponentti
        kehys: komponentti, jonka avulla tämän näkymän komponentit pysyvät vain tässä näkymässä
        nayta_generoitu_kappale: generoi-napin tapahtumakäsittelijä, 
            jolla voi generoida uuden kappaleen ja siirtyä kappalenäkymään
        lisaa_opetusdataa: lisaa opetusdataa -napin tapahtumakäsittelijä, jolla voi siirtyä opetusnäkymään
    
    """
    def __init__(self, juuri, nayta_generoitu_kappale, lisaa_opetusdataa):
        """Luoka konstruktori, jolla voi luoda uuden aloitusnäkymän

        Args:
            juuri: juurikomponetti
            nayta_generoitu_kappale: generoi-napin tapahtumakäsittelijä, 
                jolla voi generoida uuden kappaleen ja siirtyä kappalenäkymään
            lisaa_opetusdataa: lisaa opetusdataa -napin tapahtumakäsittelijä, jolla voi siirtyä opetusnäkymään
        
        """
        self.juuri = juuri
        self.kehys = None
        self.nayta_generoitu_kappale = nayta_generoitu_kappale
        self.lisaa_opetusdataa = lisaa_opetusdataa

        self.alusta()

    def pakkaa(self):
        """Metodi, joka pakkaa näkymän visuaaliset komponentit 
        
        """
        self.kehys.pack(fill=constants.X)

    def tuhoa(self):
        """Tuhoaa aloitusnäkymän, jotta toinen näkymän voidaan laittaa tilalle
        
        """
        self.kehys.destroy()

    def alusta(self):
        """Alustaa aloitusnäkymän ja luo tarvittavat visuaaliset komponentit
        
        """
        self.kehys = ttk.Frame(master = self.juuri)
        otsikko = ttk.Label(master=self.kehys, text="Etusivu")
        teksti = Text(master=self.kehys, height=4, width=60)
        teksti.insert('1.0', "Tervetuloa sovellukseen! :) Generoi uusi kappale ja siirry kuuntelemaan sitä tai lisää tietämiäsi kappaleita opetusdataan")
        teksti['state'] = 'disabled'
        opetusdataan = ttk.Button(master=self.kehys, text="lisää opetusdataa", command=self.lisaa_opetusdataa)
        generoi = ttk.Button(master=self.kehys, text="generoi uusi kappale ja siirry uuteen näkymään", command=self.nayta_generoitu_kappale)
        otsikko.pack()
        teksti.pack()
        generoi.pack()
        opetusdataan.pack()

