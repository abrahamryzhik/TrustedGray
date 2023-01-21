# TrustedGray

TrustedGray is a project designed to help easily track multiple gray market sellers to find the best price as well as see what the average price is and how prices have been changing.

The main goal of this tool is not to track prices or to find the best price, but specifically to find and track best prices from **trustworthy** sellers only. 

Right now the website is only tracking the Rolex 16570, but more watches will be added in the future!

The information gathered is posted [here](https://abrahamryzhik.github.io/TrustedGray/index.html) daily.

## File Organization

There are four main files used to generate our results.
`get_prices.py` uses [Selenium](https://www.selenium.dev/) to pull data from the sellers' websites and store it.
`gray_sellers.py` defines how we pull data from each seller.
`generate_graph.py` makes a graph of the price history (this file will maybe later be merged with `get_prices.py` so that only one script has to be run to get our data).
And finally `index.html` has all the html for the webpage to view all the information we've gathered.

## Future Changes and Goals
1. Add support for more sellers.
2. Add multiple items to track.
3. Give users a page to view all prices sorted in ascending order with links (this may happen earlier than 1 and 2 since it is easy, but it is lower priority).
4. Automate updates rather than having me run a script every day.
5. Make the webpage look better.

## Main Packages Used

For this project i am mostly relying on [Selenium](https://www.selenium.dev/) as described above with [chromedriver](https://chromedriver.chromium.org/downloads) being the browser I am using. I also use [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup) to parse html quickly.
