from urllib.parse import urljoin

import requests

from config.config import BASE_URL_CHACK, Categories, RANDOM


class GetJokes():
    def __init__(self):
        pass
    def test_get_categories(self):
        """Получение каталога шуток и передачи циклом в другой url"""
        response = requests.get(url=urljoin(BASE_URL_CHACK, Categories.JOKES_CATEGORIES))
        category_list = response.json()

        print(f'Вернулся текст: {response.text}')
        print(f'Статус код: {response.status_code}')
        assert response.status_code == 200, 'Вернулся другой статус код'

        for category in category_list:
            query_params = {"category": category}
            response = requests.get(url=urljoin(BASE_URL_CHACK, RANDOM.JOKES_RANDOM), params=query_params)
            print(f'Вернулся текст: {response.text}')
            print(f'Статус код: {response.status_code}')
            assert response.status_code == 200, 'Вернулся другой статус код'


category_list = GetJokes()
category_list.test_get_categories()