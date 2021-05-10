# Code for Day 52 Project

from InstagramBot import InstaFollower

CHROME_DRIVER_PATH = './Day 52 - Intermediate+ - Auto Tinder Swiping/chromedriver/chromedriver.exe'
SIMILAR_ACCOUNT = 'tecno.tendencias'
USERNAME = 'kevinmachuca96@hotmail.com'
PASSWORD = '43836046Kevin12011996'

ig_bot = InstaFollower(chrome_path=CHROME_DRIVER_PATH, account=SIMILAR_ACCOUNT, username=USERNAME, password=PASSWORD, ig='https://www.instagram.com/')
ig_bot.login()
ig_bot.find_followers()
ig_bot.follow()
