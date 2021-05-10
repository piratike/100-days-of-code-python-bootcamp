# Code for Day 53 Capstone Project

from collector import DataCollector

CHROME_DRIVER_PATH = './Day 53 - Intermediate+ - Data Entry Job Automation/chromedriver/chromedriver.exe'
WEBSITE_URL = 'https://www.fotocasa.es/es/alquiler/viviendas/santa-cruz-de-tenerife-provincia/todas-las-zonas/l?latitude=28.4699&longitude=-16.2546&maxPrice=400&combinedLocationIds=724,5,38,0,0,0,0,0,0&gridType=3'
FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLScOkVgooRv8khWV_usEWPhYfvwLLX1n2Mm47wNd3c8HI80X4A/viewform?usp=sf_link'

dc = DataCollector(website_url=WEBSITE_URL, chrome_path=CHROME_DRIVER_PATH, form_url=FORM_URL)
properties = dc.recollect_data()
dc.entry_data(properties)
