import requests


class new_location():
    """Работа с новой локацией"""

    def create_new_location(self):

        """Создание новой локации"""


    base_url = "https://rahulshettyacademy.com"
    key = "?key=qaclick123"

    post_resourse = "/maps/api/place/add/json"
    get_resourse = "/maps/api/place/get/json"

    post_url = base_url + post_resourse + key
    get_url = base_url + get_resourse + key

    json_for_create_new_location = {
        "location": {
            "lat": -38.383494,
            "lng": 33.427362
        },
        "accuracy": 50,
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

    result_post = requests.post(post_url, json=json_for_create_new_location)
    print("Статус-код POST-запроса: " + str(result_post.status_code))
    check_post = result_post.json()
    place_id = check_post.get("place_id")
    print("Place_id: " + place_id)

    place_ids = []

    for i in range(1, 6):
        place_ids.append(place_id)

    with open('post.txt', 'w') as file:
        for place_id in place_ids:
            file.write(place_id + "\n")

    with open('post.txt', 'r') as file:
        for line in file:
            place_id = line.strip()
    result_get = requests.get(get_url + "&place_id=" + place_id)
    print("Полученные данные place_id: " + result_get.text)
    print("Статус-код GET-запроса для place_id " + place_id + ": " + str(result_get.status_code))

test = new_location()
test.create_new_location()
