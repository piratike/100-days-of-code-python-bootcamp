# Code for Day 48 Testing codes

from selenium import webdriver

CHROME_DRIVER_PATH = './Day 48 - Intermediate+ - Selenium Webdriver/chromedriver/chromedriver.exe'
URL = 'https://www.python.org/'

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(URL)
dates = [date.text for date in driver.find_elements_by_css_selector('.event-widget time')]
links = [link.text for link in driver.find_elements_by_css_selector('.event-widget li a')]
driver.quit()

events = {}

for n in range(len(dates)):

    events[n] = {
        'date': dates[n],
        'name': links[n]
    }

print(events)
