import json

d = {"name": "Alice", "age": 30, "city": "New York"}

print(str(d))  # 字典的字符串表示

s = json.dumps(d, ensure_ascii=False)  # 将字典转换为JSON字符串
print(s)  # JSON字符串表示

data = [
    {"name": "xxx", "age": 11, "city": "New York"},
    {"name": "yyy", "age": 12, "city": "New York"},
    {"name": "zzz", "age": 13, "city": "New York"},
]


print(json.dumps(data, ensure_ascii=False))  # 将列表转换为JSON字符串

json_str = '{"name": "Alice", "age": 30, "city": "New York"}'


d = json.loads(json_str)
print(d)  # 将JSON字符串转换为字典