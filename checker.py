from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
import yaml
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

with open('./config/config.yaml') as f:
    conf = yaml.safe_load(f)


def send_msg(text):
    token = conf['token']
    chat_id = conf['chat_id']
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())


def find_element(url, element_name):

    timeout = 5
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get(url)

    try:
        myElem = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, element_name)))
        driver.quit()
        return False
    except TimeoutException:
        driver.quit()
        return True


def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = conf['check_phrase'] in str(soup.find_all(class_=conf['class_name']))
    return out_of_stock_divs


def check_inventory():
    url_check = conf['request_url']
    url_validate = conf['test_url']
    element_name = conf['element_name']
    element_found = find_element(url_check, element_name)
    if element_found:
        print("In stock")
        send_msg(f"{conf['item_name']} is in stock! Buy now - \n{url_check}")
    else:
        print("Out of stock")


while True:
    check_inventory()
    time.sleep(15)

