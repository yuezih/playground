import urllib.parse
import urllib.request
import re
import operator

class Author(object):
    def __init__(self):
        self.name = ''
        self.artNum = 0
        self.artTitle = []

authors = []
authorDict = {}
index = 0

data = ""
author_list = []

def getData(url):
    header_dict={'Host': 'scholar.google.com',
                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
                 'Accept': '*/*',
                 'Accept-Language': 'zh-CN,zh;q=0.9',
                 'Referer': 'https://scholar.google.co.id/citations?hl=zh-CN&user=oqYL6fQAAAAJ',
                 'Connection': 'keep-alive'}
    req = urllib.request.Request(url=url,headers=header_dict)
    response = urllib.request.urlopen(req,timeout=120)

    tempdata = response.read()
    tempdata = tempdata.decode()
    return tempdata

urls = ['https://scholar.google.co.id/citations?hl=zh-CN&user=oqYL6fQAAAAJ',
        'https://scholar.google.co.id/citations?hl=zh-CN&user=oqYL6fQAAAAJ&cstart=20&pagesize=80',
        'https://scholar.google.co.id/citations?hl=zh-CN&user=oqYL6fQAAAAJ&cstart=100&pagesize=100',
        'https://scholar.google.co.id/citations?hl=zh-CN&user=oqYL6fQAAAAJ&cstart=200&pagesize=100']

for each in urls:
    data += getData(each)

title_pattern = re.compile(r'gsc_a_at">.*?<')
author_pattern = re.compile(r'<div class="gs_gray">.*?</div><')
publisher_pattern = re.compile(r'</div><div class="gs_gray">.*?<span')

title = re.findall(title_pattern, data)
author = re.findall(author_pattern, data)
publisher = re.findall(publisher_pattern, data)

for i in range(len(title)):
    title[i] = title[i][10:-1]
for i in range(len(author)):
    author[i] = author[i][21:-7]
    author_list.append(author[i].split(', '))
# for i in range(len(publisher)):
#     publisher[i] = publisher[i][27:-5]

# for i in range(len(title)):
#     print(title[i])
#     print(author[i])
#     print('')

def readAuthor(name):
    global authors
    global authorDict
    global index
    if name not in authorDict:
        newAut = Author()
        newAut.name = name
        authors.append(newAut)
        authorDict[name] = index
        index += 1
    authors[authorDict[name]].artNum += 1

for each_art in author_list:
    for each_author in each_art:
        readAuthor(each_author)

cmpfun = operator.attrgetter('artNum','name')
authors.sort(key = cmpfun,reverse = True)

for author in authors:
    if author.name[-1] == '\n':
        author.name = author.name[:-1]
    print(f'{author.name} 参与了 {author.artNum} 篇论文')