import json

def avaaJson():
    with open('data.json', 'r') as data:
        arvo = json.loads(data.read())
        return arvo

def tallennaJson(tallennettava):
    with open('data.json', 'w') as data:
        arvo = json.dumps(tallennettava)
        data.write(arvo)
