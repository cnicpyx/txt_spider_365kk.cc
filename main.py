from spider import spider
from spider import create_txt
from items import *
from clean import cleanBook
from settings import *

if __name__ == '__main__':
    # print("=" * 50)
    # print("书名 《{}》".format(bookTitle))
    # print(author)
    # print(status)
    # print(update)
    # print(introduction)
    # print("=" * 50)

    # create_txt()
    # spider(first_page, sleeptmp=[2, 1])
    cleanBook()
