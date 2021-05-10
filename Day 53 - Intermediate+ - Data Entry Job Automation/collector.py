# Code for Day 53 Capstone Project

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class DataCollector:

    def __init__(self, website_url, chrome_path, form_url):

        self.form_url = form_url
        self.chrome_path = chrome_path
        self.website_url = website_url

        self.driver = webdriver.Chrome(executable_path=self.chrome_path)
        self.website = self.driver.get(self.website_url)
        time.sleep(2)

        try:

            self.driver.find_element_by_css_selector('#sui-TcfFirstLayerModal > div > div > footer > div > button.sui-AtomButton.sui-AtomButton--primary.sui-AtomButton--solid.sui-AtomButton--center').click()

        except NoSuchElementException:

            pass

        finally:

            website_state = 'loading'

            while website_state != 'complete':
                website_state = self.driver.execute_script('return document.readyState;')
                time.sleep(1)

            website = self.driver.execute_script('return document.documentElement.outerHTML')
            self.soup = BeautifulSoup(website, 'html.parser')

    def recollect_data(self):

        urls = [url.get('href') for url in self.soup.find_all(class_='re-Card-link')]
        prices = [price.getText().split()[0] for price in self.soup.find_all(class_='re-Card-price')]
        addresses = [address.getText() for address in self.soup.find_all(class_='re-Card-title')]

        properties = []
        properties.append(urls)
        properties.append(prices)
        properties.append(addresses)

        return properties

    def entry_data(self, properties):

        self.driver.get(self.form_url)
        num_properties = len(properties[0])
        time.sleep(2)

        for n in range(num_properties):

            self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div').send_keys(properties[0][n])
            self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div').send_keys(properties[1][n])
            self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div').send_keys(properties[2][n])
            self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div').send_keys(Keys.ENTER)
            time.sleep(1)
