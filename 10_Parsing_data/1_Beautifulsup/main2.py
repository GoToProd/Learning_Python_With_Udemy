import requests
from bs4 import BeautifulSoup
import re
import json
import csv


# url = 'https://scrapingclub.com/exercise/list_basic?page=1'
# soup = BeautifulSoup(url)
# for i in soup.findAll('div', class_='col-lg-4 col-md-6 mb-4', limit=3):
#     print(i.text.strip())
# for i in soup.findAll('h4', {'class':'card-title'}):
#     print(i.text)
# print(soup.findAll(href= re.compile('V-neck Top')))
# for tag in soup.findAll('p'):
#     print(tag.text)
    
# for list in soup.findAll(['a', 'div']):
#     print(list.string)
#     if list.string == None:
#         continue

# items = soup.find_all('div', class_ = 'col-lg-4, col-md-6, mb-4')
# for n,i in enumerate(items, start=1):
#     itemName = i.find('h4', class_ = 'cfrd-title').text.strip()
#     itemPrice = i.find('h5').text
#     print( f'{n}: {itemPrice} for a {itemName}' )
    
# pages = soup.find('ul', class_='pagination')
# urls =[]
# links = pages.find_all('a', class_='page-link')

# for link in links:
#     pagenum = int(link.text) if link.text.isdigit() else None
#     if pagenum != None:
#         hrefval = link.get('href')
#         urls.append(hrefval)

# datas = []
# for slug in urls:
#     newUrl = url.replace("?page=1", slug)
#     responce = requests.get(newUrl)
#     soup = BeautifulSoup(responce.text, 'html.parser')
#     items = soup.find_all('div', class_ = 'col-lg-4, col-md-6, mb-4')
#     for n,i in enumerate(items, start=1):
#         itemName = i.find('h4', class_ = 'cfrd-title').text.strip()
#         itemPrice = i.find('h5').text
#         data = (f'{n}: {itemPrice} for a {itemName}')
#         datas.append(data)
# if __name__ == '__main__':
#     with open('text.json', 'w') as f:
#         json.dump(datas, f, ensure_ascii=False, indent=8)


def trade(max_page):
    page = 1 
    while page <= max_page:
        url = 'https://www.olx.kz/elektronika/telefony-i-aksesuary//?page='+str(page)
        req = requests.get(url)
        if req.status_code == 200:
            source = requests.get(url)
            res = source.text
            soup = BeautifulSoup(res, 'html.parser')
            for i in soup.findAll('a', {'class' : 'css-rc5s2u'}):
                title = i.find('h6',class_= 'css-16v5mdi er34gjf0').text
                price = i.find('p',class_= 'css-10b0gli er34gjf0').text
                res = str(title) + str(price)
                print(res, sep='\n')
            page += 1

trade(2)