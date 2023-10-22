import requests


class NewLocation():
    """Работа с новой локацией"""

    def create_new_location(self):
        """Создание новой локации"""

        base_url = 'https://rahulshettyacademy.com'  # Базовый url
        path = '/maps/api/place/add/json'  # Параметр для всех запросов
        params = '?key=qaclick123'  # Параметры метода POST

        json_for_create_new_location = {
            "location": {

                "lat": -38.383494,

                "lng": 33.427362

            }, "accuracy": 50,

            "name": "Frontline house",

            "phone_number": "(+91) 983 893 3937",

            "address": "29, side layout, cohen 09",

            "types": [

                "shoe park",

                "shop"

            ],

            "website": "http://google.com",

            "language": "French-IN"
        }

        response_post = requests.post(base_url + path + params, json=json_for_create_new_location)
        assert 200 == response_post.status_code
        if response_post.status_code == 200:
            print('Успех! Локация создана')
        else:
            print('Провал!! Запрос ошибочный')

        check_post = response_post.json()
        check_info_post = check_post.get('status')
        assert check_info_post == "OK"
        place_id = check_post.get('place_id')

        """Проверка создание новой локации"""

        path = '/maps/api/place/get/json'  # Параметр для получения данных

        response_get = requests.get(base_url + path + params + '&place_id=' + place_id)
        a = base_url + path + params + '&place_id=' + place_id
        print(a)
        assert 200 == response_get.status_code
        if response_get.status_code == 200:
            print('Проверка создания новой локация, прошла успешна')
        else:
            print('Провал!! Запрос ошибочный')

        """Изменение новой локации"""

        path = '/maps/api/place/update/json'  # Параметр для получения данных
        json_for_update_new_location = {

            "place_id": place_id,

            "address": "100 Lenina street, RU",

            "key": "qaclick123"

        }
        response_put = requests.put(base_url + path + params, json=json_for_update_new_location)

        assert 200 == response_put.status_code
        if response_put.status_code == 200:
            print('Локация изменена')
        else:
            print('Провал!! Запрос ошибочный')
        print(response_put.text)
        check_put = response_put.json()
        check_put_info = check_put.get('msg')
        print(f'Сообщение {check_put_info}')
        assert check_put_info == 'Address successfully updated', 'Сообщение пришло другое!!!'

        """Проверка изменений новой локации"""
        path = '/maps/api/place/get/json'
        response_get = requests.get(base_url + path + params + '&place_id=' + place_id)
        assert 200 == response_get.status_code
        if response_get.status_code == 200:
            print('Проверка изменения новой локация, прошла успешна')
        else:
            print('Провал!! Запрос ошибочный')

        check_addres = response_get.json()
        check_addres_info = check_addres.get('address')
        print(f'Сообщение {check_addres_info}')
        assert check_addres_info == '100 Lenina street, RU', 'Сообщение пришло другое!!!'

        """Удаление новой локации """
        path = '/maps/api/place/delete/json'
        json_for_delete_new_location = {
            "place_id": place_id
        }
        response_delete = requests.delete(base_url + path + params, json=json_for_delete_new_location)
        print(f'Статус код: {response_delete.status_code}')
        assert 200 == response_delete.status_code
        if response_get.status_code == 200:
            print('Успех! Удаление новой локации прошло успешно')
        else:
            print('Провал!! Запрос ошибочный')

        check_status = response_delete.json()
        check_status_info = check_status.get('status')
        print(f'Сообщение {check_status_info}')
        assert check_status_info == 'OK'



new_place = NewLocation()
new_place.create_new_location()
