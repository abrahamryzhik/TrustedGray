import pandas as pd
import matplotlib.pyplot as plt

lines = []

with open("price_history.txt", "r") as f:
	lines = f.readlines()


date_time = []

prices = []

for entry in lines:
	entry_split = entry.split(',')
	date_time.append(entry_split[0])
	prices.append(float(entry_split[1]))


#date_time = ["2021-01-01", "2021-01-02", "2021-01-03"]
date_time = pd.to_datetime(date_time)
#data = [1, 2, 3]

DF = pd.DataFrame()
DF['value'] = prices
DF = DF.set_index(date_time)
plt.plot(DF)
plt.gcf().autofmt_xdate()
plt.title("16570 Price History")
plt.ylabel("Average Price ($)")
plt.savefig("16570_price_graph.png", dpi=400)