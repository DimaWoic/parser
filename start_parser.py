from petshop.link_pagination import get_pagination
from petshop.get_page import get_link, get_product
import csv

link = []
url ='https://www.petshop.ru/catalog/cats/syxkor/#p2=129,133,69,5,110,12,54'





for m in get_pagination(url, link):
    get_pagination(m, link)




p = get_link(url)
print(p)
for l in p:
    for k in range(4):
        t=get_product(l, k)
        if t==None:
            pass
        else:
            with open('products.csv', 'a', newline='') as csvfile:
                        writer = csv.writer(csvfile, dialect='excel', delimiter=',')
                        writer.writerow(['', t['title'], t['description'], t['weight'], t['price'], '', t['image']])


print('Парсинг окончен')