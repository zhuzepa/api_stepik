from urllib.parse import urljoin
import requests

from config.config import BASE_URL_CHACK, Categories, RANDOM

receiving_category = input('Введите категорию: ') # Запросили у юзера категорию

response = requests.get(url=urljoin(BASE_URL_CHACK, Categories.JOKES_CATEGORIES)) # Запросили у юзера список категорий
print(f'Статус код: {response.status_code}')
print(f'Текст: {response.text}')
assert response.status_code == 200, 'Вернулся другой статус код'

if receiving_category in response.text: # Проверямем есть ли так категория, которую запросил юзер
    print(f'Категория {receiving_category} есть в ответе')
else:
    print('Вы ввели неправельную категорию')

query_params = {"category": receiving_category}
response = requests.get(url=urljoin(BASE_URL_CHACK, RANDOM.JOKES_RANDOM), params=query_params) # Получаем шутку по категории которую запросил юзер
print(f'Вернулся текст: {response.text}')
print(f'Статус код: {response.status_code}')
assert response.status_code == 200, 'Вернулся другой статус код'
