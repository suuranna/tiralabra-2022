from jsonFunktiot import avaaJson, tallennaJson
from syotetyn_kappaleen_tarkistus import syotetyn_kappaleen_tarkistus

def lisaa_opetusdataan_kappale(kappale):
    """Metodi, joka ensin tarkistaa toisella metodilla, että annettu kappale on oikeassa muodossa, ja
    lisää sitten sen data.json-tiedostoon

    Args:
        kappale: String-muodossa opetusnäkymän tekstikenttään kirjoitettu kappale

    Returns:
        Jos annettu kappale on virheellisessä muodossa, palauttaa metodi String-muodossa viestejä.
        Jos kaikki menee niin kuin pitää ja kappale saadaan onnistuneesti lisättyä opetusdataan,
        palautetaan tuple, jossa on listana kirjoitetun kappaleen sävelet ja toisena listana nuotit
    
    """
    tarkistettu_kappale = syotetyn_kappaleen_tarkistus(kappale)

    if isinstance(tarkistettu_kappale, str):
        return tarkistettu_kappale


    lista = kappale.split()
    savelet = []
    nuotit = []

    opetusdata = avaaJson()

    for alkio in lista:
        eroteltu = alkio.split("-")
 
        savelet.append(eroteltu[0])
        nuotit.append(eroteltu[1])

    opetusdata["savelet"].append(savelet)
    opetusdata["nuotit"].append(nuotit)

    tallennaJson(opetusdata)

    return (savelet, nuotit)