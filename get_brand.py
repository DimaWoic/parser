import requests
from bs4 import BeautifulSoup
from petshop.get_page import get_link, get_product
from petshop.link_pagination import get_pagination
import csv
import os

path = "out"
try :
    os.mkdir(path)
except OSError:
    print ("Создать директорию  не удалось " + path)
else: print("Директория  успешно создана")

fullpath = os.getcwd()+'/'+path
print(fullpath)

url ='https://www.petshop.ru'

link = []
brands_url =[]
brands_list = []


def get_product_brands(url, brands_url, brands_list):
    def soup(url):
        r = requests.get(url)
        page = BeautifulSoup(r.text, 'html.parser')
        return page
    nav_bar_find = soup(url).find('nav', class_='NavBar_left_side__1xw-7 NavBarTheme_left_side__31T3s')
    cats_link = url + nav_bar_find.find('a').get('href')
    cats_brands_in_li = soup(cats_link).findAll('li', class_='highlight')
    for brands_li in cats_brands_in_li:
        href_brand_in_a = brands_li.find('a')
        brand_name = href_brand_in_a.text
        brands_list.append(brand_name)
        href_brand = url + href_brand_in_a.get('href')
        brands_url.append(href_brand)

get_product_brands(url, brands_url, brands_list)

print(brands_list)
print(brands_url)


for u in brands_url:
    index = brands_url.index(u)
    brand = brands_list[index]
    try:
        for p in get_link(u):
            for i in range(4):
                dict_atrib_product = get_product(p, i, brand)
                if dict_atrib_product == None:
                    pass
                else:
                    with open( brand + '.csv'.format(file_path = fullpath), 'a', newline='') as csvfile:
                        writer = csv.writer(csvfile, dialect='excel', delimiter=',')
                        writer.writerow(['', dict_atrib_product['title'], dict_atrib_product['brand'],
                                         dict_atrib_product['description'],
                                         dict_atrib_product['weight'], dict_atrib_product['price'], '',
                                         dict_atrib_product['image']])


    except: pass




