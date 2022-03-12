import json
with open("./write.json",'r',encoding="utf-8") as f:
    data=json.load(f)
    print(data)