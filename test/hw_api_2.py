import requests

receiving_category = input('Введите категорию: ')

url = 'https://api.chucknorris.io/jokes/categories'
response = requests.get(url)
print(f'Статус код: {response.status_code}')
print(f'Текст: {response.text}')

assert response.status_code == 200, 'Вернулся другой статус код'
if receiving_category in response.text:
    print(f'Категория {receiving_category} есть в ответе')
else:
    print('Вы ввели неправельную категорию')
