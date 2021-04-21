# Code for Day 48 Testing codes

from selenium import webdriver

CHROME_DRIVER_PATH = './Day 48 - Intermediate+ - Selenium Webdriver/chromedriver/chromedriver.exe'

URL = 'https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463'

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get(URL)
item_price = driver.find_element_by_id('priceblock_ourprice')
print(item_price.text)

URL = 'https://www.python.org/'

driver.get(URL)
search_bar = driver.find_element_by_name('q')
print(search_bar.get_attribute('placeholder'))

driver.get(URL)
logo = driver.find_element_by_class_name('python-logo')
print(logo.size)

driver.get(URL)
doc_link = driver.find_element_by_css_selector('.documentation-widget a')
print(doc_link.text)

driver.get(URL)
bug_link = driver.find_element_by_xpath('/html/body/div/footer/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# driver.close() # Close the active Tab
driver.quit() # Close all the Tabs
