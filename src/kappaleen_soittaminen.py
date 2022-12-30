from soittaja import Soittaja

def soita_kappale(savelet, nuotit, tempo):
    """Funktio, joka soittaa annetun kappaleen halutussa tempossa, jos
    tempo on positiivinen kokonaisluku

    Args:
        savelet: soitettavan kappaleen sävelet listana järjestyksessä
        nuotit: soitettavan kappaleen nuotit listana järjestyksessä
        tempo: positiivisena kokonaislukuna tempo, jossa soitettava kappale soitetaan

    Returns:
        Palauttaa String-muodossa olevan viestin, jos annettu tempo on virheellinen.
        Jos kappale saadaan onnistuneesti soitettua, palautetaan 0 merkkinä siitä
    """
    soittaja = Soittaja()
    nuottien_kestot = {"1/4": 60, "1/8": 30, "1/2": 120,
                       "3/8": 90, "1/16": 15, "1": 240, "3/16": 45}

    try:
        tempo = int(tempo)
    except ValueError:
        return "Kirjoita tempo numeromuodossa esim. 60"

    if tempo < 0:
        return "Kirjoita jokin nollaa suurempi kokonaisluku numeromuodossa esim. 60"

    for i in range(len(nuotit)):
        savel = savelet[i]
        kesto = nuottien_kestot[nuotit[i]] / tempo
        soittaja.soita(savel, kesto)
    return 0
