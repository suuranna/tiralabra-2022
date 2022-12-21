class Solmu:
    """Luokka, joka vastaa Trie-rakenteen yhtä solmua

    Attributes:
        nimi: solmun nimi, joka on joko sävel tai nuottia vastaava numero
        kappaleen_loppu: joko True tai False, joka kuvaa sitä, onko solmu loppusolmu
        lapset: dictionary solmun lapsista, eli solmuista, jonne pääsee tästä solmusta
        maara: kuvaa montako kertaa kyseinen solmu on tullut vastaan
    
    """
    def __init__(self, nimi):
        self.nimi = nimi
        self.kappaleen_loppu = False
        self.lapset = {}
        self.maara = 1