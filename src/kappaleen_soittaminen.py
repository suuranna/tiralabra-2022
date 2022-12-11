import musicalbeeps


class Soittaja:
    def __init__(self):
        self.soittaja = musicalbeeps.Player(volume=1, mute_output=False)

    def soita(self, savel, kesto):
        self.soittaja.play_note(savel, kesto)


def soita_kappale(savelet, nuotit, tempo):
    soittaja = Soittaja()
    nuottien_kestot = {"1": 60, "2": 30, "3": 120, "4": 90, "5": 15, "6": 240, "7": 45}
    for i in range(len(nuotit)):
        savel = savelet[i]
        kesto = nuottien_kestot[nuotit[i]] / tempo
        soittaja.soita(savel, kesto)
