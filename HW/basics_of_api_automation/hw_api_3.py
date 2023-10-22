import requests


class NewLocationHW():
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
        print(f'Статус код: {response_post.status_code}')
        assert 200 == response_post.status_code
        if response_post.status_code == 200:
            print('Успех! Локация создана')
        else:
            print('Провал!! Запрос ошибочный')

        check_post = response_post.json()
        place_id = check_post.get('place_id')
        places_id = []
        for i in range(1, 6):
            places_id.append(place_id)

        with open('resource/file.txt', 'w') as file:
            for place_id in places_id:
                file.write(place_id + "\n")

        """Проверка создание новой локации"""
        path = '/maps/api/place/get/json'  # Параметр для получения данных
        with open('resource/file.txt', 'r') as file:
            for line in file:
                place_id = line.strip()

        response_get = requests.get(base_url + path + params + '&place_id=' + place_id)
        print(base_url + path + params + '&place_id=' + place_id)
        print("Полученные данные place_id: " + response_get.text)
        print(f'Статус-код GET-запроса для place_id " + place_id + ": {response_get.status_code}')

        if response_get.status_code == 200:
            print('Проверка создания новой локация, прошла успешна')
        else:
            print('Провал!! Запрос ошибочный')


new_place = NewLocationHW()
new_place.create_new_location()
