import json
def read_json(filename):
    pth = "../data/"+filename
    with open(pth,'r',encoding="utf-8")as f:
        return json.load(f)

if __name__ == '__main__':
    datas = read_json()
    arrs=[]
    for data in datas.values():
        arrs.append((data['a'],data['b'],data['c']))
    print(arrs)