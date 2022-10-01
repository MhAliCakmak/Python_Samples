
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top'
response = requests.get(url).content
soup = BeautifulSoup(response, 'html.parser')

liste = soup.find_all('tbody', {'class': 'lister-list'})
for i in liste:
    basliklar = i.find_all('td', {'class': 'titleColumn'})
    for baslik in basliklar:
        baslik = baslik.text
        baslik = baslik.strip()
        baslik = baslik.replace('\n', '')
        print(baslik)
