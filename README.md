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
And finally `index.html` has all the html for the webpage to view all the information we've gathered. There are also a bunch of text files which mostly have random nonsense that I use for reference. Hopefully they'll be gone soon.

## Future Changes and Goals
1. Add multiple items to track.
2. Store data in a json file to make life easier and let me add cool things like the time the webpage was updated (I may do this before 1 since it's easier even though it is lower priority).
3. Automate updates rather than having me run a script every day.
4. Make the webpage look better.

## Main Packages Used

For this project i am mostly relying on [Selenium](https://www.selenium.dev/) as described above with [chromedriver](https://chromedriver.chromium.org/downloads) being the browser I am using. I also use [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup) to parse html quickly.
