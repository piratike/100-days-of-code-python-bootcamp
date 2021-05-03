# Code for Day 48 Project

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = './Day 50 - Intermediate+ - Auto Tinder Swiping/chromedriver/chromedriver.exe'
URL = 'https://tinder.com/'
FACEBOOK_EMAIL = 'tutotronik@gmail.com'
FACEBOOK_PASSWORD = '12011996Kevin'

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(URL)

time.sleep(1)
driver.find_element_by_xpath('//*[@id="u-264510806"]/div/div[1]/div/main/div[1]/div/div/div/div/div[3]/div/div[2]/button').click()

time.sleep(1)
driver.find_element_by_xpath('//*[@id="u-1992891882"]/div/div/div[1]/div/div[3]/span/button').click()

time.sleep(1)
driver.find_element_by_xpath('//*[@id="u-1992891882"]/div/div/div[1]/div/div[3]/span/div[3]/button').click()

time.sleep(5)
login_window = driver.window_handles[1]
driver.switch_to.window(login_window)
driver.find_element_by_id('email').send_keys(FACEBOOK_EMAIL)
driver.find_element_by_id('pass').send_keys(FACEBOOK_PASSWORD)
driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

time.sleep(5)
