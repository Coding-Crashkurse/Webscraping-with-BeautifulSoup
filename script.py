import requests
import csv
from bs4 import BeautifulSoup



url = "https://www.transfermarkt.de/1-bundesliga/marktwerte/wettbewerb/L1/ajax/yw1/page/1"
heads = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
response = requests.get(url, headers=heads)
response.text
html = response.text
soup = BeautifulSoup(html, "html.parser")
elem = soup.find(id="yw1")
footballers = elem.find_all("a",{"class":"spielprofil_tooltip"})

footballers[0].text

prices = elem.find_all("td",{"class":"rechts hauptlink"})
float(prices[0].text.split()[0].replace(",", "."))

### Final solution
pages = list(range(1, 5))
footballer_list = []
price_list = []

for page in pages:
    url = "https://www.transfermarkt.de/1-bundesliga/marktwerte/wettbewerb/L1/ajax/yw1/page/" + str(page)
    heads = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    response = requests.get(url, headers=heads)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    elem = soup.find(id="yw1")
    footballers = elem.find_all("a",{"class":"spielprofil_tooltip"})
    prices = elem.find_all("td",{"class":"rechts hauptlink"})
    
    for footballer in footballers:
        footballer_list.append(footballer.text.strip())
        
    for price in prices:
        price_list.append(float(price.text.split()[0].replace(",", ".")))
        
footballer_list
price_list  

result = list(zip(footballer_list, price_list))
result