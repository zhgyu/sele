import json
def read_json(filename):
    pth = "../data/"+filename
    with open(pth,'r',encoding="utf-8") as f:
        return json.load(f)