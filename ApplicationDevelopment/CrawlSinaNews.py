import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas


# (1)用requests库获取网页信息，获取每个分页的url
def get_new_urls(page_url):
    '''获取每个分页的所有新闻的url,并返回'''
    _urls = []
    #浏览器请求头
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
    }
    res= requests.get(page_url,headers=headers)
    if res.status_code != 200:
        print('url acquisition failed!: ' + page_url)
        return None
    res_content = res.json().get('cards')
    if res_content :  #返回数据
        for item in res_content:
            _urls.append('http:' + item['scheme'])
        return _urls
    else:
        print('url parse failed ！：' + page_url)
        return None

#(2) 获取每个新闻的详细信息
def get_one_news(news_url):
    """取得新闻的详细信息"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
    }
    respose = requests.get(news_url, headers=headers)
    if respose.status_code != 200:
        print('url acquistion failed!:' + news_url)
        return None
    respose.encoding = 'uft-8'
    try:
        soup = BeautifulSoup(respose.text, 'xlml')
        title = soup.find(attrs={'class': 'page-header'}).h1.string
        content = ''.join([''.join(list(i.strings)) for i in soup.find(attrs = {'id':'aetibody'}).find_all(attrs={'align':'justify'})])
        ctime = list(soup.find(attrs={'align':'time-source'}).strings)[0].strip()
        source = list(soup.find(attrs={'class': 'time-source'}).strings)[1].strip()
    except:
        return None
    return {'title':title, 'content':content, 'ctime': ctime,'source':source}

#(3)存储爬取的新闻信息
def save_to_csv(all_data):
    pd.DataFrame(all_data).to_csv('temp.csv', encoding='utf-8', index=False)
    print('文件保存完毕！')



if __name__ == '__main__':
    page_num = 5 # 在次修改需要爬取的页数
    base_url = 'http://travel.sina.cn/interface/2018/_feed.d.json? target=3&page{}' #网页内动态新获取闻的url
    headers = []
    all_data = []

    #循环每一页，获取所有新闻的url
    for i in range(1,page_num+1):
        print('========开始爬取第{}页========'.format(i))
        page_url = base_url.format(i)
        news_urls = get_new_urls(page_url)
        if news_urls:
            for news_url in news_urls:
            #all_news_urls += news_urls
                #循环所有新闻的url
                #for news_url in all_news_urls:
                print(news_url)
                data = get_one_news(news_url)
                if data:
                    all_data.append(data)
    print('爬取总共获取新闻', len(all_data),'条！')

    save_to_csv(all_data) #保存到本地csv
