import json
"""
字典转换为json字符串
"""
dict_data={
    "name":"张三",
    "age":18
}
json_data = json.dumps(dict_data)
print("转换前",type(dict_data))
print("转换后",type(json_data))

"""
json字符串转换为字典
"""
data  = '{"name":"张三","age":18}'
dict_d = json.loads(data)
print("转换前",type(data))
print("转换后",type(dict_d))

