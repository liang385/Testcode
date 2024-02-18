import csv
import json
# 导入需要的库
# json保存的数据字典类型
data = [{'name': 'Alice', 'age': 25, 'city': 'New York'},
        {'name': 'Bob', 'age': 30, 'city': 'Paris'},
        {'name': 'Charlie', 'age': 35, 'city': 'London'}]

# 使用 dump 方法将 Python 数据类型转换为 JSON 格式，并将其写入到文件中。
# 其中，参数 indent 可以指定缩进的空格数，可以让输出的 JSON 文件更加易读。
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
    f.close()
with open('data.json', 'r',encoding='utf-8') as f1:
    datas=json.load(f1)
    for data in datas:
        print(data['name'])





"""
# csv以列表类型的数据为例：
data = [["name", "age", "city"],
        ["Alice", 25, "New York"],
        ["Bob", 30, "Paris"],
        ["Charlie", 35, "London"]]

# 使用 writer 方法将 Python 数据类型转换为 CSV 格式，并将其写入到文件中。
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
# 注意，这里需要指定 newline=''，否则在写入 CSV 文件时会出现空行。

"""