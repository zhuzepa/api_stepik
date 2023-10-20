import requests

url = 'https://api.chucknorris.io/jokes/random'

response = requests.get(url)

response.encoding = 'utf-8'
print(f'Статус код: {response.status_code}')
print(f'Текст: {response.text}'), 'Должен вернуться текст'
assert response.status_code == 200, 'Статус код не 200'