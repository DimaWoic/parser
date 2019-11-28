import requests
from bs4 import BeautifulSoup

def get_link(url):
    link = []
    page = requests.get(url)
    pagesoup = BeautifulSoup(page.text, 'html.parser')
    layout = pagesoup.find('div', id='products-wrapper')
    item = layout.findAll('h3', class_='h4 j_adj_title')
    item_card = pagesoup.findAll('li', class_='product-item j_product j_adj_item')
    for z in item:
        a = z.find('a').get('href')
        link.append('https://www.petshop.ru' + a)
    return link


def get_product(url_from_link, i_in_range4):
    r = requests.get(url_from_link)
    soup = BeautifulSoup(r.text, 'html.parser')
    title_product = soup.find('h1', class_='product-name j_product_name').text
    product_card = soup.find('div', class_='product-detail-page__product-form__items')  # часть страницы с ценами и весом
    try:
        data_block_rows = product_card.findAll('li')[i_in_range4]  # строка с весом и ценами
        weight = data_block_rows.find('div', class_='product-weight').text  # вес
        price = data_block_rows.find('span', class_='j_offer_price product-price').find('span').text  # цена
        try:
            description = soup.find('div', id='product-features').text  # описание
        except:
            description = soup.find('div', class_='char-item').text
        image_link = soup.find('ul', class_='js-preview-img')  # получаем секцию с ссылками на изображение
        image_src = image_link.findAll('a')  # массив ссылок
        img_href = 'https:' + image_src[0].find('img').get('src')  # получаем ссылку
    # создаём словарь и добавляем результаты парсинга
        page_out = dict.fromkeys(['title', 'weight', 'price', 'description', 'image'])
        page_out['title'] = title_product
        page_out['weight'] = weight
        page_out['price'] = price
        page_out['description'] = description
        page_out['image'] = img_href
        print(title_product, weight)
        return page_out
    except: return None



