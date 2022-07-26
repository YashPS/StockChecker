from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
import yaml
from collections import deque

with open('./config/config.yaml') as f:
    conf = yaml.safe_load(f)
q = deque([False, False, False], maxlen=3)


def send_msg(text):
    token = conf['token']
    chat_id = conf['chat_id']
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())


def get_page_html(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options, executable_path='./execs/chromedriver.exe')
    browser.get(url)
    html = browser.page_source

    return html


def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = conf['check_phrase'] in str(soup.find_all(class_=conf['class_name']))
    return out_of_stock_divs


def check_inventory():
    url_check = conf['request_url']
    url_validate = conf['test_url']
    page_html = get_page_html(url_check)
    if not check_item_in_stock(page_html):
        print("In stock")
        q.append(True)
        if False not in q:
            send_msg(f"{conf['item_name']} is in stock!")
    else:
        print("Out of stock")


while True:
    check_inventory()
    time.sleep(15)
