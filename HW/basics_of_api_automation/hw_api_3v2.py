import json
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
        place_ids = []
        for i in range(1, 6):
            response_post = requests.post(url=urljoin(BASE_URL_RAHULS, RAHULS.PATH_PLEASE_ADD),

                                          json=json_for_create_new_location)

            if response_post.status_code == 200:
                print('Успех! Локация создана', i)
            else:
                print('Провал!! Локация не создана', i)
                continue
            check_post = response_post.json()

            place_id = check_post.get('place_id')
            place_ids.append(place_id)

            """Проверка создание новой локации"""
            self.checking_location_creation(place_id)
        # self.write_file(place_ids)
        # self.delete_place(place_ids[1])
        # self.delete_place(place_ids[3])


    def checking_location_creation(self, place_id):
        """Проверка локации из файла"""
        query_params = {'key': 'qaclick123', 'place_id': place_id}
        response_get = requests.get(urljoin(BASE_URL_RAHULS, RAHULS.PATH_PLEASE_GET), params=query_params)
        print("Полученные данные place_id: " + response_get.text)

        if response_get.status_code == 200:
            print('Проверка получения локации, прошла успешна')
        else:
            print('Провал!! Запрос ошибочный')

    # @staticmethod
    # def delete_place(place_id):
    #     data = {'place_id': place_id}
    #
    #     response_delete = requests.delete(urljoin(BASE_URL_RAHULS, RAHULS.PATH_PLEASE_DEL), json=data)
    #     print(response_delete.text)
    #     if response_delete.status_code == 200:
    #         print('Проверка удаления place_id:, прошла успешна')
    #     else:
    #         print('Провал!! Запрос ошибочный')
    #
    # @staticmethod
    # def write_file(place_ids):
    #     with open('resource/file.txt', 'w') as file:
    #         json.dump(place_ids, file, indent=4)


new_place = NewLocationHW()
new_place.create_new_location()
