import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Adolf_Hitler"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

links = soup.findAll("a")

for link in links:
    print(link.get('href'))
