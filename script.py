import requests
import csv
from bs4 import BeautifulSoup


pages = list(range(1, 5))
footballer_list = []

for page in pages:
    print(page)
    url = "https://www.transfermarkt.de/1-bundesliga/marktwerte/wettbewerb/L1/ajax/yw1/page/" + str(page)
    heads = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    response = requests.get(url, headers=heads)
    html_icerigi = response.text
    soup = BeautifulSoup(html_icerigi, "html.parser")
    elem = soup.find(id="yw1")
    footballers = elem.find_all("a",{"class":"spielprofil_tooltip"})
    for footballer in footballers:
        footballer_list.append({"Futbolcu" : footballer.text.strip()})
        
        
        