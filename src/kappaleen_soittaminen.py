from soittaja import Soittaja

def soita_kappale(savelet, nuotit, tempo):
    """Metodi, joka soittaa annetun kappaleen halutussa tempossa, jos tempo on positiivinen kokonaisluku

    Args:
        savelet: soitettavan kappaleen sävelet listana järjestyksessä
        nuotit: soitettavan kappaleen nuotit listana järjestyksessä
        tempo: positiivisena kokonaislukuna tempo, jossa soitettava kappale soitetaan
    
    Returns:
        Palauttaa String-muodossa olevan viestin, jos annettu tempo on virheellinen.
        Jos kappale saadaan onnistuneesti soitettua, palautetaan 0 merkkinä siitä
        
    """
    soittaja = Soittaja()
    nuottien_kestot = {"1": 60, "2": 30, "3": 120, "4": 90, "5": 15, "6": 240, "7": 45}

    try:
        tempo = int(tempo)
    except:
        return "Kirjoita jokin nollaa suurempi kokonaisluku numeromuodossa esim. 60"
    
    if tempo < 0:
        return "Kirjoita jokin nollaa suurempi kokonaisluku numeromuodossa esim. 60"

    for i in range(len(nuotit)):
        savel = savelet[i]
        kesto = nuottien_kestot[nuotit[i]] / tempo
        soittaja.soita(savel, kesto)
    return 0
