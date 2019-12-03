import requests
from bs4 import BeautifulSoup

"""Функция get_pagination возвращает массив линков пагинации, принимает 
аргумент url адрес на список продуктов, и массив link"""

def get_pagination(url, link):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    pagination = soup.find('div', class_='page-navigation')
    pagination_a = pagination.findAll('a')
    for i in pagination_a:
        h = i.get('href')
        href = 'https://www.petshop.ru' + h
        if href in link:
            pass
        else: link.append(href)
    return link










