import requests
import time
from lxml import etree
from settings import *
from items import *


# 获取下一页链接
def next_url(next_url_element):
    nxturl = main_url
    # rfind('/') 获取最后一个'/'字符的索引
    index = next_url_element.rfind('/') + 1
    nxturl += next_url_element[index:]
    return nxturl


'''
标题路径 //*[@class="title"]/text()
内容路径 //*[@id="content"]/text()
链接路径 //*[@class="section-opt m-bottom-opt"]/a[3]/@href
'''


# 创建文本文档
def create_txt():
    with open(dir + bookTitle + '.txt', 'w', encoding='utf-8') as f:
        f.write('==  《' + bookTitle + '》\r\n')
        f.write('==  ' + author + '\r\n')
        f.write('==  ' + status + '\r\n')
        f.write('==  ' + update + '\r\n')
        f.write("=" * 10)
        f.write('\r\n')
        f.write('==  ' + introduction + '\r\n')
        f.write("=" * 10)
        f.write('\r\n')


def spider(start_url, maxCnt=pageNums, sleeptmp=[3, 2]):
    url = start_url
    lastTitle = ''  # 上一章标题
    cnt = 0
    end_url = main_url + '999999.html'
    while url != end_url:
        cnt += 1
        if cnt > maxCnt:
            break
        resp = requests.get(url, headers=headers)
        text = resp.content.decode('utf-8')
        html = etree.HTML(text)
        next_url_element = html.xpath('//*[@class="section-opt m-bottom-opt"]/a[3]/@href')[0]
        chapter_title = html.xpath('//*[@class="title"]/text()')[0]
        contents = html.xpath('//*[@id="content"]/text()')
        print("正在爬取...  Page {}, {}, url: {}".format(cnt, chapter_title, url))

        with open(dir + bookTitle + '.txt', 'a', encoding='utf-8') as f:
            # 判断是否为新的章节
            if chapter_title != lastTitle:
                f.write(chapter_title)  # 写入新章节标题
                f.write('\r\n')  # 换行

            # 储存章节内容
            for i in range(0, len(contents)):
                if i <= 2 and contents[i] == '\n':
                    continue
                if contents[i].endswith('\u3000\u3000'):
                    contents[i] = ''
                f.write(contents[i])
                if i == len(contents) - 1:
                    f.write('\r\n')
                    continue
                if contents[i] != '\u3000\u3000' and contents[i + 1] != '\u3000\u3000':
                    f.write('\r\n')
                f.write('\r\n')

            # 判断是否为新的章节
            if chapter_title == lastTitle:
                f.write('\r\n')
                f.write('\r\n')
            else:
                lastTitle = chapter_title

            f.close( )

        url = next_url(next_url_element)
        time.sleep(sleep_time(sleeptmp[0], sleeptmp[1]))
