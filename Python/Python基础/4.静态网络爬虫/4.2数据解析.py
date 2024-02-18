import requests
from lxml import html
from bs4 import BeautifulSoup

# 1:设置请求头User-Agent 目的伪装为游览器请求
# 伪装前的Headers由requests自动生成容易被游览器发现为爬虫

# 设置headers:将Network，的Request Header的信息拷贝User-Agent
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
           }

response = requests.get('https://movie.douban.com/', headers=headers)
# 打印伪装后的headers
# print(response.request.headers)

# 2:设置代理服务器Proxy 目的：避免同一个ip较短时间内访问而被封禁
# 设置代理http-协议类型 101.4.136.34-代理ip 81-代理端口
proxy = {'http': 'http:101.4.136.34:81'}

re = requests.get('https://movie.douban.com/', headers=headers, proxies=proxy)
# print(re.text)

# 3:Xpath //匹配当前文档的节点，不考虑他们的位置  @选取属性  //*选取文档中所有元素
# //title[@*]选取所有带有属性的title元素


# 所有lxml解析requests库爬取的html源码
etree = html.etree
tree = html.etree.HTML(re.text)
title = tree.xpath('//title/text()')
m = tree.xpath('//*[@id="screening"]/div[2]/ul/li/ul/li[2]/a/text()')
href = tree.xpath('//*[@id="screening"]/div[2]/ul/li/ul/li[2]/a/@href')
books = dict(zip(m, href))
# print(books)
# 使用beautifulsoup4解析，使用lxml
soup = BeautifulSoup(re.text, 'lxml')
# BeautifulSoup4四大对象类型
# 1:tag是html中的标签
print(type(soup.title))
# 2：NavigableString可以遍历的字符 ,获取标签内容通过soup.title.string
print(type(soup.title.string))
# 3:beautifulsoup对象
print(type(soup))
# 4:Comment特殊的navigableString

# Beautifulsoup4的高级用法
# 遍历
# 1：Tag.contents:获取Tag的所有字节点，返回一个列表
print(soup.head.contents[1])
# 2:children:获取Tag的所有字节点,返回一个生成器
print(soup.head.children)

# 搜索
# 1：find_all(name,attrs,recursive,text)搜索当前Tag的所有子节点，
# 2:该方法可以传入：字符串，列表，正则表达式，方法作为参数
list=soup.find('a')
print(list)

# Css选择器
# 通过标签名
# print(soup.select('a'))
# 通过类名
print(soup.select('.prev-btn'))
# 通过id
print(soup.select('#screening'))
# 组合
print(soup.select('div .wrapper'))
# 属性
print(soup.select('a[class="prev-btn"]'))
# 获取内容
print(soup.select("title")[0].get_text())

