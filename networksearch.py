import requests
from lxml import etree


#网站地址
url = 'http://www.netbian.com/'

#获取网页
r = requests.get(url)
r.encoding = r.apparent_encoding
#解析网页
dom = etree.HTML(r.text)

#获取图片 img标签
#先获取图片所在的 img标签在分别获取图片链接和名字
img_path = '//a[@title]/img'

url_path = '//a[@href]'
imgs = dom.xpath(img_path)
urls = dom.xpath(url_path)
print(urls)

