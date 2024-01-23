import requests
from bs4 import BeautifulSoup
import csv
from multiprocessing import Pool

def main():
    url = 'https://numizm.at/catalog/banknotes/'
    links = []
    all_links = get_all_links(get_html(url), links)
    with Pool() as p:
        p.map(make_all, all_links)


def get_html(url):
    r = requests.get(url)
    return r.text


def make_all(url):
    html = get_html(url)
    data = get_page_data(html)
    write_csv(data)


def get_all_links(html, links):
    f = open('money.csv', 'w')
    f.close()
    soup = BeautifulSoup(html, 'html.parser')
    href = soup.find_all('div', class_ = 'product-item-wrapper')
    for i in href:
        for link in i.find_all('a'):
            links += [link['href']]
    return links


def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        name = soup.find('li', 'total-page').find('h1').text
    except:
        name = 'Cant find'
    try:
        massive_price = [pn.find('div', class_ = 'product-name').text for pn in soup.find('div', class_ = 'item clearfix').find_all(
            'div', class_ = 'tyt-box', target = False)] + [pr.text for pr in soup.find(
            'div', class_ = 'product-name').find_all()]
        if len(massive_price) == 6:
            massive_price = massive_price[0] + massive_price[3] + massive_price[1] + massive_price [4]
            + massive_price[2] + massive_price[5]
        elif len(massive_price) == 4:
            massive_price = massive_price[0] + massive_price[2] + massive_price[1] + massive_price [3]
    except:
        massive_price = ' Error '
    data = {'name': name, 'price': massive_price}
    return data

def write_csv(data):
    with open('money.csv', 'a') as f:
        write = csv.writer(f)
        write.writerow(data['name'], data['price'])
        f.close()


if __name__ == '__main__':
    main()
