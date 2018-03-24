#coding:utf-8


"""The Google Translate Implementation."""


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
# from selenium.common.exceptions import StaleElementReferenceException
import time
import urllib

def get_driver():
    # options = webdriver.ChromeOptions()
    # options.set_headless()
    # driver = webdriver.Chrome(options=options)
    try:
        driver = webdriver.PhantomJS()
        return driver
    except WebDriverException as e:
        print(e)
        pass

    return None

def _pre_url(url):
    _url = urllib.parse.quote(url)
    return _url.replace('/', '%2F')


def translate_to_japanese(text, driver=get_driver()):
    if driver:
        baseurl = 'https://translate.google.com/#auto/zh-CN/'

        url = _pre_url(text)
        # print(baseurl + url)
        driver.get(baseurl + url)

        # driver.implicitly_wait(1)
        time.sleep(2)

        try:
            result_box = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, '//*[@id="result_box"]')))
            result_html = result_box.get_attribute('innerHTML')
            
            for i in range(3):
                if result_html != u"正在翻译...":
                    break
                else:
                    time.sleep(2)
                    print(result_html)

            return result_html
        except NoSuchElementException as e:
            # print(e)
            pass

    return ""
