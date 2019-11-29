from link_pagination import get_pagination
from get_page import get_link, get_product
import csv
import time

link = []
url_category ='https://www.petshop.ru/catalog/cats/syxkor/#p2=129,133,69,5,110,12,54'





for pagination in get_pagination(url_category, link):
    get_pagination(pagination, link)

for url in link:
    time.sleep(3)
    p = get_link(url)
    print(p)
    for l in p:
        for k in range(4):
            t = get_product(l, k)
            if t == None:
                pass
            else:
                with open('products.csv', 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile, dialect='excel', delimiter=',')
                    writer.writerow(['', t['title'], t['description'], t['weight'], t['price'], '', t['image']])





print('Парсинг окончен')