# Class for code for Day 51

from platform import win32_edition
from typing import final
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = './Day 50 - Intermediate+ - Auto Tinder Swiping/chromedriver/chromedriver.exe'

class InstaFollower:

    def __init__(self, account, username, password, ig, chrome_path=''):

        self.chrome_path = chrome_path
        self.similar_account = account
        self.ig_username = username
        self.ig_password = password
        self.ig_url = ig

        self.driver = webdriver.Chrome(executable_path=self.chrome_path)

    def login(self):

        self.driver.get(self.ig_url)
        time.sleep(2)

        try:

            self.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN._4Yzd2 > div > div > button.aOOlW.bIiDR').click()
            time.sleep(5)

        except NoSuchElementException:

            pass

        finally:

            self.driver.find_element_by_name('username').send_keys(self.ig_username)
            self.driver.find_element_by_name('password').send_keys(self.ig_password)
            time.sleep(0.5)
            self.driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button').click()
            time.sleep(5)

            try:

                self.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm').click()

            except NoSuchElementException:

                pass

            finally:

                time.sleep(2)

    def find_followers(self):

        self.driver.get(f'{self.ig_url}{self.similar_account}')
        time.sleep(5)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(5)

        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

        for n in range(10):

            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', modal)
            time.sleep(2)

    def follow(self):

        follow_buttons = self.driver.find_elements_by_css_selector('li button')

        for button in follow_buttons:

            if button.text != 'Seguir':
                pass

            else:
                button.click()
                time.sleep(1)
