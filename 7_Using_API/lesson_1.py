import requests as r


response = r.get('https://github.com/')
print(response.status_code)
if response.status_code == 200:
    print('Okay')
else: 
    print('Error: ', response.status_code)