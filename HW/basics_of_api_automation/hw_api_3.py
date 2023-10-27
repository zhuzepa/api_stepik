from urllib.parse import urljoin
import requests

from config.config import BASE_URL_RAHULS, RAHULS


class NewLocationHW:
    """Работа с новой локацией"""

    def create_new_location(self):
        """Создание новой локации"""

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
        places_id = []
        for i in range(1, 6):
            response_post = requests.post(url=urljoin(BASE_URL_RAHULS, RAHULS.PATH_PLEASE_ADD),
                                          params=RAHULS.PARAMS_KEY,
                                          json=json_for_create_new_location)
            check_post = response_post.json()
            place_id = check_post.get('place_id')
            places_id.append(place_id)  #

            if response_post.status_code == 200:
                print('Успех! Локация создана', i)
            else:
                print('Провал!! Запрос ошибочный')

        with open('resource/file.txt', 'w') as file:
            for place_id in places_id:
                file.write(place_id + "\n")
            """Проверка создание новой локации"""
        with open('resource/file.txt', 'r') as file:
            for line in file:
                place_id = line.strip()

        query_params = {"key": 'qaclick123', 'place_id': place_id}
        response_get = requests.get(urljoin(BASE_URL_RAHULS, RAHULS.PATH_PLEASE_GET), params=query_params)
        print("Полученные данные place_id: " + response_get.text)

        if response_get.status_code == 200:
            print('Проверка получения локации, прошла успешна')
        else:
            print('Провал!! Запрос ошибочный')



new_place = NewLocationHW()
new_place.create_new_location()
