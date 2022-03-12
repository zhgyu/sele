import json
data = {"name":"李四","age":19}
with open('./write.json','w',encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False)