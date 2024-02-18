"""
4.1.1掌握HTTP网络协议。
4.1.2能正确使用开发者工具进行页面调试。
4.1.3能正确使用Requests模块爬取静态页面内容
"""

import urllib.request

# 构造请求
url='http://www.gxcvuedu.com/'
headers={ 'User-Agent':
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36 Edg/113.0.1774.57'

}
request = urllib.request.Request(url=url,headers=headers)
# 打开url请求0
response=urllib.request.urlopen(request)
# 使用read()方法读取的数据为b二进制模式
print(type(response.read().decode('utf_8')))
# 使用保存数据
urllib.request.urlretrieve('http://www.gxcvuedu.com/d/file/p/20220914/bfabbe5f365df5d44915292bc25f1a18.jpg',
                           '../3.静态网页开发/data.jpg')

