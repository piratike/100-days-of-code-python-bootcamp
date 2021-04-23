# Code for Day 48 Testing codes

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = './Day 48 - Intermediate+ - Selenium Webdriver/chromedriver/chromedriver.exe'
URL = 'http://secure-retreat-92358.herokuapp.com/'

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(URL)

name_field = driver.find_element_by_name('fName')
last_field = driver.find_element_by_name('lName')
email_field = driver.find_element_by_name('email')
submit = driver.find_element_by_class_name('btn')

name_field.send_keys('Kevin')
last_field.send_keys('Machuca')
email_field.send_keys('test@test.com')

submit.send_keys(Keys.ENTER)
