import requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup

url = "https://www.transfermarkt.de/1-bundesliga/marktwerte/wettbewerb/L1/ajax/ywi/page/1"
heads = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}


response = requests.get(url, headers=heads)
html = response.text
soup = BeautifulSoup(html, "html.parser")

table = soup.find(id="yw1")
footballers = table.find_all("a", {"class": "spielprofil_tooltip"})

footballers[0].text

all_players = [player.text for player in footballers]


prices = table.find_all("td", {"class": "rechts hauptlink"})
[float(price.text.split()[0].replace(",", ".")) for price in prices]

##########################
heads = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

pages = list(range(1, 5))
pages

footballer_list = []
price_list = []

for page in pages:
    url = "https://www.transfermarkt.de/1-bundesliga/marktwerte/wettbewerb/L1/ajax/ywi/page/" + str(page)
    response = requests.get(url, headers=heads)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find(id="yw1")
    footballers = table.find_all("a", {"class": "spielprofil_tooltip"})
    all_players = [player.text for player in footballers]
    footballer_list.extend(all_players)
    
    prices = table.find_all("td", {"class": "rechts hauptlink"})
    all_prices = [float(price.text.split()[0].replace(",", ".")) for price in prices]
    price_list.extend(all_prices)
    
footballer_list   

list(zip(footballer_list, price_list))
    
    
