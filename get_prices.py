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


url = "https://www.watchfinder.com/find/Rolex/Explorer%20II/16570/1780"


innerHTML = requests.get(url).text



soup = BeautifulSoup(innerHTML, 'html.parser')

products_html = soup.find(id="prod_cat-stock")

with open("products_html.txt", "w") as f:
    f.write(str(products_html.prettify()))


product_prices = soup.find(id="prod_cat-stock").find_all("span", "prods_price")

prices_list = []

for product_price_tag in product_prices:
    prices_list.append(product_price_tag.string)

#print(prices_list)

with open("prices.txt", "w") as f:
    f.write('\n'.join(prices_list))

products = soup.find_all("div", "prods_item prods_item-stock")

price_link_list = []

with open("individual_product_html.txt", "w") as f:
    f.write(str(products[0].prettify()))

for product in products:
    price = product.find("span", "prods_price").string
    link = product.find("a").get("href")

    price_link_list.append((price, "https://www.watchfinder.com" + str(link)))
    # print(price)
    # print("https://www.watchfinder.com" + str(link))

with open("prices_with_link.txt", "w") as f:
    f.write('\n'.join([stock_example[0] + " " + stock_example[1] for stock_example in price_link_list]))

today_avg = 0
p_list = [price_link_list[i][0].replace(",", "").replace("$","") for i in range(len(price_link_list))]
#print(p_list)
sum_prices = sum([int(p) for p in p_list])

num_prices = len(price_link_list)

try:

    today_avg = sum_prices / num_prices

except:
    today_avg = 0

# print(date.today())
# print(today_avg)

min_price = int(price_link_list[0][0].replace(",", "").replace("$",""))

min_link = price_link_list[0][1]

for i in range(1, len(price_link_list)):
    cur_price = int(price_link_list[i][0].replace(",", "").replace("$",""))

    if cur_price < min_price:
        min_price = cur_price
        min_link = price_link_list[i][1]

print("The avergae price of a 16570 today is $" + str(today_avg))
print("The cheapest 16570 today is $" + str(min_price))
print("It is available at " + min_link)

with open("price_history.txt", "a") as f:
    f.write('\n')
    f.write(str(date.today()) + "," + str(today_avg)) 




# s = str(innerHTML)

# with open("html_dumpt.txt", 'w') as f:
#     f.write(s)

