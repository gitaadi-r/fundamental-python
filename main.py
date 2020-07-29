import requests

print('Hello World')

r = requests.get ('https://google .com')

try:
    if r.status_code == 200:
        print(r.text)
except Exception as e:
    print('Error', e)