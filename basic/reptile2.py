html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class='title'><b>The Dormouse's story </b></p>
<p class= 'story'>Once upon a time there were three little sisters: and their names were 
<a href='http://example.com/elsie' class='sister' id='Link1'>Elsie</a>
<a href='http://example.com/lacie/ class='sister' id='link2'>Lacie</a> and
<a href='http://example.com/tillie' class='sister' id='link3'>Title</a>
<p class='story'>...</p>
"""
# 使用
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'lxml')
print(soup.prettify())
print(soup.title)  # 获得<title>标签及其内容
print(soup.title.string)  # 获得<title> 里面的内容
