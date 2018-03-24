#coding:utf-8


"""The News Update Implementation."""


import random
import requests
from bs4 import BeautifulSoup

def update():
    global _user_agents
    global _last_day
    global _last_news

    baseurl = 'http://www.nogizaka46.com/news/'

    user_agent = random.choice(_user_agents)
    headers = {'User-Agent': user_agent}
    response = requests.get(baseurl, headers=headers) # <Response [200]>

    news_list = []
    if response.ok:
        news_list_page = BeautifulSoup(response.text, 'lxml')
        results = news_list_page.select('div > ul > li > span > span > strong > a')
        for i in results:
            n = _update_news(i.attrs['href'], headers)
            if n:
                if n[1] == _last_news or n[0] < _last_day:
                    break
                print(n[0], n[1])
                news_list.append(n)
    
    if len(news_list) > 0:
        _last_news = news_list[0][1]
    return news_list


def _update_news(url, headers):
    response = requests.get(url, headers=headers)

    if response.ok:
        news_page = BeautifulSoup(response.text, 'lxml')
        detailhead = news_page.select_one('#detailhead')

        h3 = detailhead.find('h3')
        title = h3.text

        date_div = detailhead.find('div')
        date = date_div.text
        date = ''.join(date.split('.'))

        detailbody = news_page.select_one('#detailbody')

        html = str(detailhead) + str(detailbody)

        return (date, title, html)

    return None

_user_agents = [
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)',
            ]

_last_day = "20180322"
_last_news = ""
