import json

def avaaJson():
    with open('data.json', 'r') as data:
        arvo = json.loads(data.read())#["testi"]
        return arvo

def tallennaJson(tallennettava):
    with open('data.json', 'w') as data:
        arvo = json.dumps(tallennettava)#({"testi":tallennettava.get()})
        data.write(arvo)
