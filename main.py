#coding:utf-8


"""The News Get And Storage Implementation."""

import time
import html2text
from db import insert
from translate import google
from news import news

def update():
    driver = google.get_driver()
    news_list = news.update()

    for i in news_list:
        date = i[0]
        title = i[1]
        html = i[2]
        text = html2text.html2text(html)
        trhtml = google.translate_to_japanese(text, driver)
        trtext = html2text.html2text(trhtml)

        insert.insert_news(date, title, html, trhtml, text, trtext)


def start(timeout = 60):
    while True:
        update()
        time.sleep(timeout)



if __name__ == "__main__":
    start()

