# Code for Day 48 Project

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = './Day 48 - Intermediate+ - Selenium Webdriver/chromedriver/chromedriver.exe'
URL = 'https://orteil.dashnet.org/cookieclicker/'

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(URL)

cookie = driver.find_element_by_id('bigCookie')
started = time.time()
last_check = started

while True:

    cookie.click()

    if time.time() >= last_check + 1:

        last_check = time.time()
        cookies = int(driver.find_element_by_id('cookies').text.split()[0].replace(',', ''))
        products = driver.find_elements_by_css_selector('#store .price')
        prices = []

        for product in products:
            price = product.text.replace(',', '')
            if price:
                prices.append(int(price))

        while any(prices):

            print(prices, max(prices), cookies, max(prices) <= cookies)

            if max(prices) <= cookies:
                id = prices.index(max(prices))
                driver.find_element_by_id(f'product{id}').click()
                break

            else:
                prices[prices.index(max(prices))] = 0

    if time.time() > started + 300:
        cookie_rate = driver.find_element_by_css_selector('div #cookies').text.split()[-1]
        print(f'Cookies/Second: {cookie_rate}')
        break

driver.quit()
