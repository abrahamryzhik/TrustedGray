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


#url = "https://www.watchfinder.com/find/Rolex/Explorer%20II/16570/1780"
url = "https://www.watchfinder.com/Rolex/Explorer%20II/16570/watches?filterDial=White"


# innerHTML = requests.get(url).text

browser = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'))



browser.get(url)

time.sleep(10)

innerHTML = browser.execute_script("return document.body.innerHTML")

browser.quit()

soup = BeautifulSoup(innerHTML, 'html.parser')

watches = soup.find_all('div', attrs={'data-testid': 'watchItem'})

watch_links = []
watch_prices = []

for watch in watches:
    link = watch.find('a', attrs={'data-testid': 'watchLink'}).get("href")
    try: 
        price = watch.find('div', attrs={'data-testid': 'watchPrice'}).string
    except:
        price = watch.find('span', attrs={'data-testid': 'watchPrice'}).string

    watch_links.append("https://www.watchfinder.com" + str(link))
    watch_prices.append(price)


print(watch_links)
print(len(watch_links))
print(watch_prices)
print(len(watch_prices))



with open("html_dumpt.txt", 'w') as f:
    f.write(soup.prettify())

with open("prices.txt", "w") as f:
    f.write('\n'.join(watch_prices))

with open("prices_with_link.txt", "w") as f:
    f.write('\n'.join([watch_prices[i] + " " + watch_links[i] for i in range(len(watch_links))]))




prices_list = watch_prices

with open("prices.txt", "w") as f:
    f.write('\n'.join(prices_list))


today_avg = 0

p_list = [watch_prices[i].replace(",", "").replace("$","") for i in range(len(watch_prices))]
#print(p_list)
sum_prices = sum([int(p) for p in p_list])

num_prices = len(watch_prices)

try:

    today_avg = sum_prices / num_prices

except:
    today_avg = 0


min_price = int(watch_prices[0].replace(",", "").replace("$",""))

min_link = watch_links[0]

for i in range(1, len(watch_prices)):
    cur_price = int(watch_prices[i].replace(",", "").replace("$",""))

    if cur_price < min_price:
        min_price = cur_price
        min_link = watch_links[i]

print("The avergae price of a 16570 today is $" + str(today_avg))
print("The cheapest 16570 today is $" + str(min_price))
print("It is available at " + min_link)

with open("price_history.txt", "a") as f:
    f.write('\n')
    f.write(str(date.today()) + "," + str(today_avg)) 

with open("today_summary.txt", "w") as f:
    f.write("The avergae price of a 16570 today is $" + str(today_avg) + "\n")
    f.write("The cheapest 16570 today is $" + str(min_price) + "\n")
    f.write("It is available at " + min_link)





