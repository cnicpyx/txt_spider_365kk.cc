import items
from settings import dir


def cleanBook():

    print("\n==== 数据清洗开始 ====")

    oldName = dir + items.bookTitle + '.txt'
    newName = dir + 'final ' + items.bookTitle + '.txt'

    fo = open(oldName, 'r', encoding='utf-8')
    fn = open(newName, 'w', encoding='utf-8')

    lines = fo.readlines( )
    cnt = 0

    for line in lines:
        if line.startswith('='):
            fn.write(line)
            continue
        if line == "\n":
            cnt += 1
            if cnt >= 2:
                continue
        else:
            cnt = 0
        if line.startswith("\u3000\u3000"):
            line = line[2:]  # 删除段首空格
            fn.write(line)
        elif line.startswith("第"):
            fn.write("\r\n")
            fn.write("-" * 20)
            fn.write("\r\n")
            fn.write(line)
        else:
            # line = "\u3000\u3000" + line
            fn.write(line)
    fo.close()
    fn.close()

    print("==== 数据清洗完成 ====")


