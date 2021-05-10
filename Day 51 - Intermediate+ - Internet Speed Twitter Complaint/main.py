# Code for Day 51 Project

from TwitterBot import InternetSpeedTwitterBot

CHROME_DRIVER_PATH = './Day 51 - Intermediate+ - Auto Tinder Swiping/chromedriver/chromedriver.exe'
TWITTER_URL = 'https://twitter.com/'
TWITTER_USER = 'Piratike2'
TWITTER_PASSWORD = '************'
SPEED_URL = 'https://www.speedtest.net/'
PROMISE_UP = 10
PROMISE_DOWN = 150

bot = InternetSpeedTwitterBot(twitter_url=TWITTER_URL, speed_url=SPEED_URL, user=TWITTER_USER, password=TWITTER_PASSWORD, chrome_path=CHROME_DRIVER_PATH)

speed_status = bot.get_internet_speed()
speed_status = False

if not speed_status:
    bot.tweet_at_provider()

bot.exit()
