import requests

headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'

           }
# txt文本格式保存数据
resp = requests.get('https://www.zhonghui.vip/1-plus-x-certificate/5511/', headers=headers)
f = open('test.txt', 'w', encoding='utf-8')
f.write(resp.text)
f.close()
