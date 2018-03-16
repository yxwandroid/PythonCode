import requests
import re
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

url = 'https://book.douban.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
Chrome/55.0.2883.87 Safari/537.36'}
html = requests.get(url, headers=headers)
html.encoding = 'utf-8'
# 这里我只取了链接与标题
patter = re.compile('<li class.*?cover.*?href="(.*?)".*?alt="(.*?)".*?<p class="author".*?>(.*?)</p>', re.S)
titles = re.findall(patter, html.text)
for each in titles:
    print('书籍链接:{},书籍标题：{},---书籍作者：{}'.format(each[0], each[1], each[2].strip()))
