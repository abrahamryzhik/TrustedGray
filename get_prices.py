from selenium import webdriver
import os
from lxml import html
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import urllib.request
import time
import csv
import random

from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

import pickle

from bs4 import BeautifulSoup

from datetime import date

from gray_sellers import *



browser = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'))


stores = [WatchFinder(), AISWatches(), BobsWatches(), DavidSW(), WatchBox(), MandB(), CrownAndCaliber()]


print("Pulling from " + str(len(stores)) + " stores")

price_and_link_list = []

for store in stores:
    # print("Processing: " + str(store))
    try:
        new_listings = store.get_prices_links(browser)
        price_and_link_list += new_listings
        print(str(store) + ": " + str(len(new_listings)) + " watches")


    except:
        print("Failed to load " + str(store))


print("Found " + str(len(price_and_link_list)) + " watches")

price_and_link_list.sort(key = lambda x : x[0])


browser.quit()


with open("watches/16570/prices_with_link.txt", "w") as f:
    f.write('\n'.join([str(price_and_link_list[i][0]) + " " + price_and_link_list[i][1] for i in range(len(price_and_link_list))]))
    #f.write('\n'.join([watch_prices[i] + " " + watch_links[i] for i in range(len(watch_links))]))



today_avg = 0



sum_prices = sum([entry[0] for entry in price_and_link_list])

num_prices = len(price_and_link_list)

try:

    today_avg = sum_prices / num_prices

except:
    today_avg = 0




min_entry = min(price_and_link_list, key = lambda x : x[0])

min_price = min_entry[0]
min_link = min_entry[1]



print("The avergae price of a 16570 today is $" + str(round(today_avg, 2)))
print("The cheapest 16570 today is $" + str(min_price))
print("It is available at " + min_link)

with open("watches/16570/price_history.txt", "a") as f:
    f.write('\n')
    f.write(str(date.today()) + "," + str(today_avg)) 

with open("watches/16570/today_summary.txt", "w") as f:
    f.write("The average price of a 16570 today is $" + str(round(today_avg, 2)) + ". <br>")
    f.write("The cheapest 16570 today is $" + str(min_price) + ". <br>")
    f.write("It is available at " + min_link)





