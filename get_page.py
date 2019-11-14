import requests
from bs4 import BeautifulSoup
import wget
import csv



def get_page(url):
    # ссылка на категорию
    # создаём массив для записи ссылок
    link = []
    r = requests.get(url)
    # получаем страницу
    soup = BeautifulSoup(r.text, 'html.parser')
    layout = soup.find('div', class_='items-row row')
    # print(layout)
    item = layout.findAll('div', class_='item-name-wrapper')

    # print(item)
    # получаем и добавляем ссылки в массив link
    for i in item:
        a = i.find('a').get('href')
        link.append('https://kotopes64.ru' + a)
    # a = item[0].find('a').get('href')
    # b='https://kotopes64.ru'+a
    # print(link)

    for i in link:
        link_product = i
        get_link_product = requests.get(link_product)
        html_product = BeautifulSoup(get_link_product.text, 'html.parser')
        title_product = html_product.find('div', class_='section-title').text
        # print(title_product)
        description = html_product.find('div', class_='full-item-description').text
        # print(description)
        image_link = html_product.find('a', class_='fancybox')
        image_src = image_link.find('img').get('src')
        wget.download('https://kotopes64.ru' + image_src, '/home/dima/PycharmProjects/parser/images/')

        with open('products.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, dialect='excel', delimiter=';')
            writer.writerow([title_product, description])


