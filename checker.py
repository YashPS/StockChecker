from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver


def send_msg(text):
    token = "5451194926:AAEha4fw17IxW3B-10W8BryW9vTod5DQoow"
    chat_id = "1502268415"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())


def get_page_html(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options, executable_path='E:/code/PycharmProjects/StockChecker/execs'
                                                                '/chromedriver.exe')
    browser.get(url)
    html = browser.page_source

    return html


def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = '"stockstatus":"soldout"' in str(soup.find_all(class_="ps-btn ps-blue"))
    print(out_of_stock_divs)
    return out_of_stock_divs


def check_inventory():
    url1 = "https://www.dell.com/en-in/shop/alienware-34-curved-qd-oled-gaming-monitor-aw3423dw/apd/210-bebh/monitors-monitor-accessories"
    url2 = "https://www.dell.com/en-in/shop/dell-24-video-conferencing-monitor-s2422hz/apd/210-bcbp/monitors-monitor-accessories"
    page_html = get_page_html(url1)
    if not check_item_in_stock(page_html):
        print("In stock")
        send_msg("Dell Alienware QD-OLED is in stock!")
    else:
        print("Out of stock")


while True:
    check_inventory()
    time.sleep(60)
