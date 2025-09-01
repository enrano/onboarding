import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.scrapethissite.com/pages/simple/")
soup = BeautifulSoup(r.text, 'html.parser')

list = soup.find_all("div", class_="country")

for x in list:
    name = x.find("h3", class_="country-name").get_text(strip=True)
    population = x.find("span", class_="country-population").get_text(strip=True)
    print(f"Country: {name}, Population: {population}")
#print(soup.prettify())