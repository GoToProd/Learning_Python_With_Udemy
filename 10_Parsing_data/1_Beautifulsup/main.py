# import requests
# import json

# url = 'https://notes.ayushsharma.in/technology'
# data = requests.get(url)

# if data.status_code == 200:
#     try:
#         if data.text:
#             json_data = data.json()
#             print(json_data)
#         else:
#             print("Empty response.")
#     except json.decoder.JSONDecodeError as e:
#         print(f"Error decoding JSON: {e}")
#         print("Response content:", data.text)
# else:
#     print(f"Error: {data.status_code}")

import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('span', class_ = 'text')
authors = soup.find_all('small', class_ = 'author')
tags = soup.find_all('div', class_='tags')

print(f"The number 1 of qoutes --> {len(quotes)}" )
print(f"The number 2 of qoutes --> {len(authors)}" )
print(f"The number 3 of qoutes --> {len(tags)}" )


for i in range(0, len(quotes)):
    print(f"The number of row {i}")
    print(quotes[i].text)
    print("-----" + authors[i].text)
    tagsfor = tags[i].find_all('a', class_ = 'tag')
    for i in tagsfor:
        print (i.text)
    print('\n')