import json

def avaaJson():
    """Avaa tiedoston data.json, joka sisältää kappaleiden säveliä ja nuotteja,
    ja muuttaa sen sisällön pythonin ymmärtämäksi dictionaryksi

    Returns:
        data.json-tiedoston sisältämä dictionary sävelistä ja nuoteista pythonin ymmärtämässä muodossa 
    """
    with open('data.json', 'r') as data:
        arvo = json.loads(data.read())
        return arvo

def tallennaJson(tallennettava):
    """Tallentaa data.json-tiedostoon annetun dictionaryn

    Args:
        tallennettava: python-muodossa oleva dictionary, joka halutaan talettaa data.json-tiedoston sisällöksi
    """
    with open('data.json', 'w') as data:
        arvo = json.dumps(tallennettava)
        data.write(arvo)
