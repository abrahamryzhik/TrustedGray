from bs4 import BeautifulSoup

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WatchFinder:

    def __str__(self):

        return "WatchFinder"

    def get_prices_links(self, browser):

        url = "https://www.watchfinder.com/Rolex/Explorer%20II/16570/watches?filterDial=White&filterBracelet=Bracelet"

        browser.get(url)

        #time.sleep(3)

        wait = WebDriverWait(browser, 10)
        #element = wait.until(EC.element_to_be_clickable((By.ID, 'search-app')))

        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid=\'watchPrice\']')))


        
        #time.sleep(1)

        innerHTML = browser.execute_script("return document.body.innerHTML")

        soup = BeautifulSoup(innerHTML, 'html.parser')

        watches = soup.find_all('div', attrs={'data-testid': 'watchItem'})

        price_and_link_list = []


        for watch in watches:
            link = watch.find('a', attrs={'data-testid': 'watchLink'}).get("href")
            try: 
                price = watch.find('div', attrs={'data-testid': 'watchPrice'}).string
            except:
                price = watch.find('span', attrs={'data-testid': 'watchPrice'}).string

            price_int = int(price.replace(",", "").replace("$",""))

            link = "https://www.watchfinder.com" + str(link)

            price_and_link_list.append((price_int, link))

        return price_and_link_list


class AISWatches:

    def __str__(self):
        return "AIS Watches"

    def get_prices_links(self, browser):

        url = "https://aiswatches.com/explorer/"

        browser.get(url)

        # time.sleep(3)

        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.prodImg')))
        #time.sleep(1)

        innerHTML = browser.execute_script("return document.body.innerHTML")

        soup = BeautifulSoup(innerHTML, 'html.parser')

        watches = soup.find_all('li', attrs={'class': 'product'})

        price_and_link_list = []

        for watch in watches:

            title_str = watch.find('div', attrs={'class': 'prodTitle'}).a.string

            if " 16570 " in title_str and "White Dial" in title_str:

                price = float(watch.find('div', attrs={'class': 'wirePrice'}).find("span").string.replace(",", "").replace("$",""))

                link = watch.find('div', attrs={'class': 'prodTitle'}).a.get("href")

                price_and_link_list.append((price, link))

        return price_and_link_list

class BobsWatches:

    def __str__(self):
        return "Bob\'s Watches"

    def get_prices_links(self, browser):
        url = "https://www.bobswatches.com/rolex/explorer_ii-16570-white#/filter:custom_field_4:16570/filter:custom_field_9:White"

        browser.get(url)

        #time.sleep(3)

        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.itemimage')))
        #time.sleep(1)


        innerHTML = browser.execute_script("return document.body.innerHTML")

        soup = BeautifulSoup(innerHTML, 'html.parser')

        watches = soup.find_all('div', attrs={'class': 'itemWrapper ng-scope'})

        price_and_link_list = []

        for watch in watches:

            price = int(watch.find('span', attrs={'class': 'ng-binding', 'itemprop' : 'price'}).string.replace(",", ""))

            link = "https://www.bobswatches.com/" + str(watch.find("a").get("href"))

            price_and_link_list.append((price, link))

        return price_and_link_list

class DavidSW:

    def __str__(self):
        return "DavidSW"

    def get_prices_links(self, browser):
        url = "https://davidsw.com/product-category/watch/rolex/explorer-ii/?filter_case-size=40mm&filter_dial-color=white"

        browser.get(url)

        #time.sleep(3)

        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.attachment-woocommerce_thumbnail.size-woocommerce_thumbnail.lazy-load-active')))
        #time.sleep(1)

        innerHTML = browser.execute_script("return document.body.innerHTML")

        soup = BeautifulSoup(innerHTML, 'html.parser')

        watches = soup.find_all('div', attrs={'class': 'product-small box'})

        price_and_link_list = []

        for watch in watches:

            price = float(watch.find("span",attrs={'class': 'woocommerce-Price-amount amount'}).bdi.text.replace("$", "").replace(",", ""))

            link = watch.a.get("href")

            price_and_link_list.append((price, link))

        return price_and_link_list

class WatchBox:

    def __str__(self):
        return "WatchBox"

    def get_prices_links(self, browser):
        url = "https://www.thewatchbox.com/watches/rolex/rolex-explorer-ii/?srule=Newest&fn1=dialColor&fv1=silverwhite"

        browser.get(url)

        #time.sleep(5)

        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.home-banner-img')))
        #print("here")
        browser.execute_script("window.scrollTo(0, 150)") 
        #print("ok")
        time.sleep(0.5)
        #print("looking")
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.grid__price')))
        browser.execute_script("window.scrollTo(0, 50)") 

        innerHTML = browser.execute_script("return document.body.innerHTML")

        soup = BeautifulSoup(innerHTML, 'html.parser')

        watches = soup.find_all('a', attrs={'class': 'link grid-carousel-link'})

        price_and_link_list = []

        for watch in watches:

            if watch.find('span', attrs={'class': 'grid__id'}).string[:5] == "16570":

                link = "https://www.thewatchbox.com" + watch.get("href")

                price = int(watch.find('div', attrs={'class': 'grid__price'}).text.replace("$", "").replace(",", ""))

                price_and_link_list.append((price, link))

        return price_and_link_list


class MandB:

    def __str__(self):
        return "M&B Watches"

    def get_prices_links(self, browser):
        url = "https://mandbwatches.com/product-category/rolex/rolex-explorer-ii/"

        browser.get(url)

        #time.sleep(3)

        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.prod-inner-wrap')))

        innerHTML = browser.execute_script("return document.body.innerHTML")

        soup = BeautifulSoup(innerHTML, 'html.parser')

        watches = soup.find('ul', attrs={'class': 'products'}).find_all('li')

        price_and_link_list = []

        for watch in watches:

            if " 16570" in watch.h3.text:

                link = watch.a.get('href')

                price = float(watch.find('span', attrs={'class': 'amount'}).string.replace("$", "").replace(",", ""))

                price_and_link_list.append((price, link))

        return price_and_link_list

class CrownAndCaliber:

    def __str__(self):
        return "Crown and Caliber"

    def get_prices_links(self, browser):
        url = "https://www.crownandcaliber.com/collections/rolex-explorer-ii-watches#/filter:mfield_global_case_size:39.5:41.5/filter:mfield_global_dial_color:White"

        browser.get(url)

        # time.sleep(4)

        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.grid-view-item__link')))

        

        innerHTML = browser.execute_script("return document.body.innerHTML")

        soup = BeautifulSoup(innerHTML, 'html.parser')

        watches = soup.find_all('div', attrs={'class': 'popular-watches--card text-center ng-scope'})

        price_and_link_list = []

        for watch in watches:

            link = "https:" + watch.a.get("href")

            price = int(watch.find('span', attrs={'class': 'current-price product-price__price ng-binding'}).string.replace("$", "").replace(",", ""))

            price_and_link_list.append((price, link))

        return price_and_link_list




















