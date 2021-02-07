# 网络库 urllib 库 ,http协议常用库。 requests 库，http 协议常用库，BeautifulSoup库，xml格式处理库
# from urllib import request
"""
import urllib.request as request # request 模块用来发起请求
import urllib.parse as parse  # 用来处理数据
url = "http://www.baidu.com/"

response = request.urlopen(url,timeout=1) # get方式，解析ulr，timeout 设置超时时间 1s
print(response.read().decode("utf-8"))
# post 发起请求，先请求发送的数据，再发起请求
# data = bytes(parse.urlencode({'word':'hello_word'},encoding='utf8'))
# response = request.urlopen(url,data=data)
"""
import requests
import re

content = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text
print(content)
pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)
results = re.findall(pattern, content)
print(results)
for result in results:
    url, name = result
    print(url, re.sub(r'\s', '', name))

