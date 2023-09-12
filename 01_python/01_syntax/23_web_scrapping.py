from bs4 import BeautifulSoup
import re
import requests

url = "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi"

response = requests.get(url)
doc = BeautifulSoup(response.text, "html.parser")

# find prices of phones using text
prices = doc.find_all(string="₹")
print(prices)
# now we access the parent of that specific rupee text
parent = prices[3].parent
html_string = str(parent)
soup = BeautifulSoup(html_string, "html.parser")

price_div = soup.find("div")
price = re.findall("\d+,?\d*", price_div.text)[0]

print(price)
