file_dump = []

with open("prices_with_link.txt", "r") as f:
	file_dump = f.readlines()

# print(file_dump)

prices_and_link = [entry.split(" https://") for entry in file_dump]

print(prices_and_link[0])

html_str = "<!DOCTYPE html><html><body>"

html_str += "<h1>All listings sorted in ascending order by price</h1>"

for price, link in prices_and_link:
	new_link = "https://" + link.replace('\n', '')

	html_str += "<div> <a href=\"" + new_link + "\" target=\"_blank\" rel=\"noopener noreferrer\">" + "$" + str(price) + "</a> </div>"

html_str += "</body></html>"

with open("all-prices/16570.html", "w") as f:
	f.write(html_str)

