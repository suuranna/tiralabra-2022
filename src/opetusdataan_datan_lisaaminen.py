from json_funktiot import avaa_json, tallenna_json
from syotetyn_kappaleen_tarkistus import syotetyn_kappaleen_tarkistus

def lisaa_opetusdataan_kappale(kappale):
    """Funktio, joka ensin tarkistaa toisella funktiolla, että annettu kappale
    on oikeassa muodossa, ja lisää sitten sen data.json-tiedostoon

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

    opetusdata = avaa_json()

    for alkio in lista:
        eroteltu = alkio.split("-")
        korjattu_savel = ""
        if eroteltu[0][0] == "H":
            korjattu_savel = "B" + eroteltu[0][1]
            if len(eroteltu[0]) == 3:
                korjattu_savel += eroteltu[0][2]
            savelet.append(korjattu_savel)
        else:
            savelet.append(eroteltu[0])
        nuotit.append(eroteltu[1])

    opetusdata["savelet"].append(savelet)
    opetusdata["nuotit"].append(nuotit)

    tallenna_json(opetusdata)

    return 1
