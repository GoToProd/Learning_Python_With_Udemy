import requests as rq
import json



# url = 'https://reactjs.org'
# r = rq.get(url)
#print(r.status_code, 'Status code')
#print(r.json())
# r.encoding = 'utf8'
# print(r.text)


url = 'https://api.github.com/asd'
r = rq.get(url)
# print(r.status_code)

def jpring(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


# jpring(r.json())

def check_status():
    if(r.status_code == 200):
        print(f'{r.status_code}, Success')
    else:
        print(f'{r.status_code}, Error')


# def check_status2():
#     try:
#         r.raise_for_status()
#     except r.exceptions.HTTPError as error:
#         print('Error', error, r.raise_for_status())


check_status()
# check_status2()