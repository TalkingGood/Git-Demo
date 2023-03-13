
import requests
import xlwt
from bs4 import BeautifulSoup
import re

#(1) 利用requests库中的函数，把整个网页爬取下来
url = 'http://music.163.com/#/discover/artist/cat?id=1001' #华语男歌手页面
headers = {'Accept':'text/html, applicatiom/xhtml+xml, application/xml;q=0.9, image/apng, */*;q=0.8',
          'Accept-Encoding':'gzip, deflate, br',
          'Accept-Language':'zh-CH, zh;q=0.9',
          'Connectction':'keep-alive',
          'Cookie':'cookie',   #用户信息
          'Host':'music.163.com',
          'Referer':'http://music.163.com/',
          'Upgrade-Insecure-Requests':'1',
          'User-Agent':'Mozilla/5.0 (Window NT 11.0; Win64; x64)'
                       ' AppleWebKit537.36 (KHTML, like Gecko) '
                       'Chrom/66.0.3359.181 Safari/537.36'} #添加头请求，为了模仿正常浏览器发出请求
r = requests.get(url, headers=headers)
r.raise_for_status()
r.encoding=r.apparent_encoding
html = r.text
print(html)

#(2) 利用beautifulSoup库解析html字符串
soup = BeautifulSoup(html, 'lxml')
top_10 = soup.find_all('div',attrs={'class':'u-cover u-cover-5'})
print(top_10)

#(3)用正则表达式把歌手的信息筛选出来
singers = []
for i in top_10:
    singers.append(re.findall(r'.*?<a class="msk" href="(/artist\?id=\d+) title="(.*?)的音乐"></a.*?',str(i)[0]))

#(4)写入表格
url = 'http://music.163.com'
for singer in singers:
    try:
        new_url = url + str(singer[0])
        print(new_url)
        songs = requests.get(url,headers=headers).text #获取歌曲信息
        soup = BeautifulSoup(songs,'html.parser')
        Info = soup.find_all('textarea', attrs={'style':'display:none;'})[0]
        songs_url_and_name = soup.find_all('ul', attrs={'class':'f-hide'})[0]
        print(songs_url_and_name)
        datas = []
        data1 = re.findall(r'"album".*?"name":"(.*?).*?', str(Info.text))
        data2 = re.findall(r'.*?<li>>a href="(/song\?id=\d+)">(.*)</a></li>.*?', str(songs_url_and_name))

        for i in range(len(data2)):
            datas.append([data2[i][1], data1[i], 'http://music.163.com/#' + str(data2[i][0])])

        print(datas)
        book = xlwt.Workbook()
        sheet1 = book.add_sheet('sheet1', cell_overwrite_ok=True)
        sheet1.col(0).width = (25*256)
        sheet1.col(1).width = (30*256)
        sheet1.col(2).width = (40*256)
        heads = ['歌曲名字','专辑','歌曲链接']
        count = 0
        for head in heads:
            sheet1.write(0,count, head)
        count += 1

        i = 1
        for data in  datas:
            j= 0
            for k in data:
                sheet1.write(i ,j ,k)
                j+=1
            i+=1
        book.save(str(singer[1]+ '.xls')) #括号里写存入的地址
    except:
        continue
