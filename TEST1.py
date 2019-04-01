from bs4 import BeautifulSoup
from lxml import html
import xml
import requests

url = "https://gz.centanet.com/ershoufang/"
f = requests.get(url)
soup = BeautifulSoup(f.content, "lxml")
#print(f.content.decode())

for k in soup.find_all('div' ,class_= "item-pricearea fr"):
    a = k.find_all(class_="price-txt tc")
    print(a)

