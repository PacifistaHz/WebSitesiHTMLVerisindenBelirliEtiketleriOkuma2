from bs4 import BeautifulSoup
import requests

url="https://www.haberturk.com"

istek=requests.get(url)
html=istek.text

soup=BeautifulSoup(html,"html.parser")

print(soup.title)
print(soup.title.text)