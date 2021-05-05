# Class for code for Day 51

from platform import win32_edition
from typing import final
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

class InternetSpeedTwitterBot:

    def __init__(self, twitter_url, speed_url, user, password, promise_up=0.01, promise_down=0.15, chrome_path=''):

        self.twitter = twitter_url
        self.speedweb = speed_url
        self.user = user
        self.password = password
        self.promise_up = promise_up
        self.promise_down = promise_down
        self.up_speed = 0
        self.down_speed = 0
        self.chrome_path = chrome_path

        self.driver = webdriver.Chrome(executable_path=self.chrome_path)

    def get_internet_speed(self):

        self.driver.get(self.speedweb)
        time.sleep(2)

        try:

            self.driver.find_element_by_id('_evidon-banner-acceptbutton').click()
            time.sleep(0.5)
            self.driver.find_element_by_class_name('start-text').click()

        except NoSuchElementException:

            self.driver.find_element_by_class_name('start-text').click()

        finally:

            time.sleep(60)

            try:

                self.down_speed = float(self.driver.find_element_by_class_name('download-speed').text)
                self.up_speed = float(self.driver.find_element_by_class_name('upload-speed').text)

            except NoSuchElementException:

                self.down_speed = 0
                self.up_speed = 0

            finally:

                if self.up_speed < self.promise_up or self.down_speed < self.promise_down:
                    return False

                return True

    def tweet_at_provider(self):

        self.driver.get(self.twitter)
        time.sleep(2)

        try:

            self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div[1]/div[1]/div/div[3]/a[2]').click()
            time.sleep(1)
            self.driver.find_element_by_name('session[username_or_email]').send_keys(self.user)
            self.driver.find_element_by_name('session[password]').send_keys(self.password)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span').click()
            time.sleep(3)

            msg = f'Hey Internet Provider, why is my internet speed {self.down_speed} down / {self.up_speed} when I pay for 0.15 down / 0.01 up?'
            self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div').send_keys(msg)
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]').click()
            time.sleep(5)

        except NoSuchElementException:

            time.sleep(2)

    def exit(self):

        self.driver.quit()
