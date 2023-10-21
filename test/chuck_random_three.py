import requests


class NewJoke:
    """Создание новой шутки"""

    def __init__(self):  # Просто заглушка
        pass

    # def test_create_new_random_joke(self):
    #     """Создание случайно шутки"""
    #     url = 'https://api.chucknorris.io/jokes/random'
    #
    #     response = requests.get(url)
    #
    #     response.encoding = 'utf-8'
    #     print(f'Статус код: {response.status_code}')
    #     print(f'Текст: {response.text}'), 'Должен вернуться текст'
    #     assert response.status_code == 200, 'Статус код не 200'
    #     check = response.json()
    #     # check_info = check.get("categories")
    #     # print(check_info)
    #     # assert check_info == []
    #     # print('Категория верна')
    #     check_info_value = check.get('value')
    #     print(check_info_value)
    #     name = 'Chuck Norris'
    #     if name in check_info_value:
    #         print('Chuck hi!')
    #     else:
    #         print('Chuck\'a нет :( ')


    def test_create_new_random_category_joke(self):
        """Создание случайно шутки"""
        params = 'sport'
        url = f'https://api.chucknorris.io/jokes/random?category={params}'

        response = requests.get(url)

        response.encoding = 'utf-8'
        print(f'Статус код: {response.status_code}')
        print(f'Текст: {response.text}'), 'Должен вернуться текст'
        assert response.status_code == 200, 'Статус код не 200'
        check = response.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == ['sport']
        print('Категория верна')
        # check_info_value = check.get('value')
        # print(check_info_value)
        # name = 'Chuck Norris'
        # if name in check_info_value:
        #     print('Chuck hi!')
        # else:
        #     print('Chuck\'a нет :( ')

#random_jock = NewJoke()
#random_jock.test_create_new_random_joke()

sport_jock = NewJoke()
sport_jock.test_create_new_random_category_joke()