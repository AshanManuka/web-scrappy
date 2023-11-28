from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.daraz.lk/mens-watches/").text

soup = BeautifulSoup(page, 'lxml')

desc_box = soup.find_all('div', class_='box--ujueT')
print(desc_box)

for p in desc_box:
    item = desc_box.find('div', class_='gridItem--Yd0sa')
    print(item)
