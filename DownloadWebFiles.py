# coding:utf-8
import urllib2
import re
from bs4 import BeautifulSoup
from distutils.filelist import findall

id = 0
end = "/"
pat2 = '/(.+?\.gz)'
for num in range(1, 224):
    id = id + 1
    m = "%03d" % id
    # print "第"+str(id)+"页begin::"
    # 根据规律拼接网页地址，循环遍历
    url = 'http://data.ess.tsinghua.edu.cn/pathlinks/path_' + m + '.html'
    # 页面解析
    page = urllib2.urlopen(url)
    contents = page.read()
    soup = BeautifulSoup(contents, "html.parser")
    # 新建数组存储所需的下载地址
    list = []
    # 搜索所有的href链接
    for tag in soup.find_all('a'):
        list.append(tag.get("href"))
    count = 0
    # 三个链接按顺序只选择1、4、7、10...即可，每个页面的最后一个不是下载链接，所以要减掉
    for s in range(0, len(list)-1, 3):
        print list[s]
        count += 1
        # 提取出下载链接最后的文件名
        string1 = list[s]
        string2 = string1[string1.rfind(end):]
        name = re.compile(pat2).findall(string2)
        name = str(name[0])
        # 根据下载链接和文件名存储文件
        f = urllib2.urlopen(string1)
        with open(name, "wb") as code:
            code.write(f.read())
    print "第"+str(id)+"页共下载了"+str(count)+"个文件"


