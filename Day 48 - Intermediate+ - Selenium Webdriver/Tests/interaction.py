# Code for Day 48 Testing codes

from selenium import webdriver

CHROME_DRIVER_PATH = './Day 48 - Intermediate+ - Selenium Webdriver/chromedriver/chromedriver.exe'
URL = 'https://en.wikipedia.org/wiki/Main_Page'

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(URL)
articles_in_english = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]')
print(articles_in_english.text)
driver.quit()
