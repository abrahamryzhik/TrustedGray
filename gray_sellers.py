from bs4 import BeautifulSoup

import time

class WatchFinder:

    def get_prices_links(self, browser):

        url = "https://www.watchfinder.com/Rolex/Explorer%20II/16570/watches?filterDial=White"

        browser.get(url)

        time.sleep(3)

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

    def get_prices_links(self, browser):

        url = "https://aiswatches.com/explorer/"

        browser.get(url)

        time.sleep(3)

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




