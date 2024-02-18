import json
import csv
import requests
import time
from lxml import etree

urls = "http://www.gxcvuedu.com/cyyw/"
headers = {"User_Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
response = requests.get(headers=headers, url=urls)
# 输出headers
print(response.headers)
# 返回文本类型的相应数据
# print(response.text)
# 二进制形式的数据,设置字符集
# print(response.content.decode(encoding="utf8"))

# 使用lxml解析数据,生成待解析对象
etree = etree.HTML(response.content.decode(encoding="utf8"))
# 解析的对象为一个list
titles = etree.xpath('//*[@id="content"]/section[1]/ul/li/h3/a/text()')
date = etree.xpath('//*[@id="content"]/section[1]/ul/li/div/div[2]/strong/text()')
sum = etree.xpath('//*[@id="content"]/section[1]/ul/li/div/div[2]/span/text()')
dates = []
for index, title in enumerate(titles):
    data = {"title": title, "date": date[index], "sum": sum[index]}
    dates.append(data)

# print(dates)
with open("dates.json", "w", encoding='utf8', newline='') as f:
    # json.dumps()将Python对象编码成json字符串
    # print(json.dumps(dates))
    # json.load()将json形式的字符串转换我Python类型
    # indent.格式化保存字典
    # ensure_ascii=False:解决中文乱码
    json.dump(dates, f, indent=4, ensure_ascii=False)

with open("dates.csv", 'w', encoding='utf8', newline='') as f:
    # 字典写入
    head = ['title', 'date', 'sum']
    writer = csv.DictWriter(f, fieldnames=head)
    # 写入表头
    writer.writeheader()
    # 格式[{}],[[]]
    writer.writerows(dates)
