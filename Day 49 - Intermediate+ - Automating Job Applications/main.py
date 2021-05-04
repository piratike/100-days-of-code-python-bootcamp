# Code for Day 49 Project

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = './Day 49 - Intermediate+ - Automating Job Applications/chromedriver/chromedriver.exe'
URL = 'https://www.linkedin.com/jobs/search/?f_AL=true&f_WRA=true&geoId=105646813&keywords=python&location=Espa%C3%B1a&sortBy=R'
LINKEDIN_KEY = 'kevinmachuca96@hotmail.com'
LINKEDIN_PASSWORD = '**************'

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(URL)

time.sleep(2)
driver.find_element_by_css_selector('body > div.cta-modal.show > a.cta-modal__primary-btn').click()

time.sleep(1)
driver.find_element_by_name('session_key').send_keys(LINKEDIN_KEY)
driver.find_element_by_name('session_password').send_keys(LINKEDIN_PASSWORD)
driver.find_element_by_class_name('btn__primary--large').send_keys(Keys.ENTER)

time.sleep(3)
jobs_list = driver.find_elements_by_class_name('job-card-list__title')

for job in jobs_list:

    job.click()
    time.sleep(2)
    driver.find_element_by_class_name('jobs-save-button').send_keys(Keys.ENTER)
    time.sleep(1)
