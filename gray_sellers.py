from bs4 import BeautifulSoup

import time

class WatchFinder:

    def get_prices_links(self, url, browser):
        browser.get(url)

        time.sleep(10)

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
