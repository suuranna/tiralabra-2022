import musicalbeeps

class Soittaja:
    """Luokka, joka kuvaa soittajaa, joka soittaa halutun sävelen halutulla kestolla

    Attributes:
        soittaja: musicalbeeps-kirjaston Player-olio, joka hoitaa sävelien soittamisen
    """
    def __init__(self):
        """Luokan konstruktori, joka luo uuden soittajan
        """
        self.soittaja = musicalbeeps.Player(
            volume=1,
            mute_output=False)

    def soita(self, savel, kesto):
        """Metodi, joka soittaa annetun sävelen annetulla kestolla

        Args:
            savel: soitettava sävel String-muodossa
            kesto: kesto sekuntteina
        """
        self.soittaja.play_note(savel, kesto)
