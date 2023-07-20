import random
import os.path

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Cookie': 'ASP.NET_SessionId=phx4vtab4rxqyzlkokk1d3qz; bookid=248964; fontFamily=null; fontColor=null; fontSize=null; bg=null; booklist=%257B%2522BookId%2522%253A248964%252C%2522ChapterId%2522%253A999999%252C%2522ChapterName%2522%253A%2522%2522%257D',
    'Host': 'www.365kk.cc',
    'Connection': 'keep-alive'
}


# 等待时长
def sleep_time(c, r):
    t = random.randint(c - r, c + r)
    if t <= 0:
        t = 1
    return t


# 小说主页
main_url = "http://www.365kk.cc/248/248964/"


# 爬取页面数
pageNums = 1e5


# 文件存储路径
dir = "output/"
if not os.path.exists(r"output"):
    os.mkdir("output")
