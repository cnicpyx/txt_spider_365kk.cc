import requests
from lxml import etree
from settings import *


# 请求小说首页
main_resp = requests.get(main_url, headers=headers)
main_text = main_resp.content.decode('utf-8')
main_html = etree.HTML(main_text)

'''
书名 //div[@class="top"]/h1/text()
作者 //div[@class="top"]//p[1]/text()
状态 //div[@class="top"]//p[3]/text()
最后更新日期 //div[@class="top"]//p[5]/text()
简介 //div[@class="info"]//div[2]/text()
正文第一页 //div[@class="section-box"][2]//li[1]//@href
'''

bookTitle = main_html.xpath('//div[@class="top"]/h1/text()')[0]
author = main_html.xpath('//div[@class="top"]//p[1]/text()')[0]
status = main_html.xpath('//div[@class="top"]//p[3]/text()')[0]
update = main_html.xpath('//div[@class="top"]//p[5]/text()')[0]
introduction = main_html.xpath('//div[@class="info"]//div[2]/text()')[0]
first_page = main_url + main_html.xpath('//div[@class="section-box"][2]//li[1]//@href')[0]


# 清洗
author = author.replace(u'\xa0', '').strip()  # 删除&nbsp
status = status.replace(u'\xa0', '').strip()
introduction = introduction.replace(r'\n', '').strip()


# print("目标书名: ", bkname)
# print(author + ', ' + status + ', ' + update)
# print("简介: ")
# print(introduction)
# print(first_page)
