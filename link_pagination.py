import requests
from bs4 import BeautifulSoup
from get_page import get_page

link=[]
url = 'https://kotopes64.ru/catalog/47-suhie_korma/?&dop=eyJhY3Rpb24iOiJyZWZyYXNoR29vZHMiLCJmaWx0ZXIiOnsiMSI6eyIxNTYiOiIxIiwiMTciOiIxIiwiMTgiOiIxIiwiMjEiOiIxIiwiMTYiOiIxIiwiMjAiOiIxIn19LCJub25maWx0ZXIiOnsicHJpY2VfbWluIjoiMCIsInByaWNlX21heCI6IjM3MDMifSwibG9jYXRpb24iOiJcL2NhdGFsb2dcLzQ3LXN1aGllX2tvcm1hXC8ifQ&page=1'

def get_pagination(url, link):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    pagination = soup.find('ul', class_='pagination')
    pagination_a = pagination.findAll('a')
    for i in pagination_a:
        h = i.get('href')
        href = 'https://kotopes64.ru' + h
        if href in link:
            pass
        else: link.append(href)
    return link


#print(pagination_a)




for i in get_pagination(url, link):
    get_pagination(i, link)

print(link.__len__())

for http in link:
    get_page(http)