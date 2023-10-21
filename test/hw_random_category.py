import random
import requests

url = 'https://api.chucknorris.io/jokes/categories'

response = requests.get(url)
assert response.status_code == 200, 'Вернулся другой статус код'
print(f'Вернулся текст: {response.text}')
print(f'Статус код: {response.status_code}')

category_key = response.json()
random_category = random.randint(0, len(category_key) - 1)

url = f'https://api.chucknorris.io/jokes/random?category={category_key[random_category]}'

response = requests.get(url)

category_receipt = response.json()
category_list = list[category_receipt]

print(f'Вернулся текст: {response.text}')
print(f'Статус код: {response.status_code}')
assert category_receipt['categories'][0] == category_key[random_category]
assert response.status_code == 200, 'Вернулся другой статус код'
