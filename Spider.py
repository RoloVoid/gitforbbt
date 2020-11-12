import re
import requests
import os
import time


# 大致看了一下那个小说网页，有两层，所以选择用临时文件储存url，最后再统一删除的方法
def getNovelUrl(url):
    storage = open("小说url目录.txt", 'w')
    # 考虑到要批量操作，我在这里选择用文件临时储存url
    # 下面各小说的章节同理

    allurl=requests.get(url)
    allurl.encoding='utf-8'
    
    match = re.findall("(?:<li><a href=\")(http.*/\d*/)(?:\">)(.*)(?:</a></li>)", allurl.text)

    for i in match:
        storage.writelines(i[0]+'\t'+i[1] + '\n')
    
    # 储存为url+小说名的条目便于接下来利用

    storage.close()


def getChaptersUrl(record1):
    novelurl = record1.split()[0]
    novelname = record1.split()[1]
    # 用split()解析条目

    chapterurl = requests.get(novelurl)
    chapterurl.encoding = 'utf-8'

    if not os.path.exists(os.getcwd() + "\\%s" % novelname):
        os.mkdir("%s" % novelname)
    storage2 = open(os.getcwd() + "\\%s" % novelname + '\\' + 'chaptersurl.txt', 'w')
    # 创建以小说名命名的文件夹并创建储存chapter的url，后期的小说文件也保存在这里

    counternumber = 0
    # 章节计数器

    match = re.findall("(?:<dd><a href=')(/.*/.*/.*.html)(?:' >)(.*)(?:</a></dd>)", chapterurl.text)
    for i in match:
        storage2.writelines("http://www.xbiquge.la" + i[0]+'\t'+i[1] + '\n')
        counternumber += 1
    # 和上一个函数一样，把章节名和url写在一起，便于下一步的利用

    storage2.close()
    return [novelname, counternumber]
    # 返回小说名和章节数，用于接下来的输出和建立目录


def downloadTxt(record2):
    finalurl = record2.split()[0]
    chaptername = record2.split()[1]

    realtext = requests.get(finalurl)
    realtext.encoding = 'utf-8'

    chapter = open(os.getcwd() + '\\' + factor[0] + '\\' + '%s.txt' % chaptername, 'w', encoding='utf-8')
    match = re.search('<div.*<p>', realtext.text)
    text = match.group().replace("&nbsp;", '')
    text = text.replace("<div id=\"content\">", '')
    text = text.replace("<br />", '')
    text = text.replace("<p>", '')
    chapter.writelines(text)

    # 写入文本

    chapter.close()

    time.sleep(2)
    # 迫不得已，为了反反爬虫，不得不牺牲速度，这几天上完课有时间还会看看别的方法

    return chaptername
    # 返回章节名，用于输出


# 优化后，以上的代码完全脱离了bs4，全部使用正则表达式进行匹配
# 其实仔细一想我的代码里bs4几乎没有起作用，只用正则反而更易于操作(笑)


print("即将下载笔趣阁页面下的所有小说，请确保脚本当前目录空间充足，是否继续？Y/N")
judge = input()
if judge == 'Y' or judge == 'y':
    getNovelUrl("http://www.xbiquge.la/xiaoshuodaquan/")
    f1 = open("小说url目录.txt", 'r')
    for line in f1:
        factor = getChaptersUrl(line)
        f2 = open(os.getcwd() + '\\' + factor[0] + '\\' + 'chaptersurl.txt', 'r')
        print("正在下载《%s》" % factor[0])
        print("该小说共%s章" % str(factor[1]))
        counter = 0
        for line2 in f2:
            counter += 1
            name2 = downloadTxt(line2)
            print("%s已完成" % name2)
        f2.close()
        os.remove(os.getcwd() + '\\' + factor[0] + '\\' + 'chaptersurl.txt')
        # 用后即删，释放空间
    f1.close()
    os.remove("小说url目录.txt")
    # 最后删除大目录

    print("下载已全部完成")
else:
    print("放弃下载")
    print("按回车键退出程序")
    input()
    quit
