import requests

URL = 'https://swapi.dev/api/people/4/'
response = requests.get(URL)
assert response.status_code == 200

# URL_FILM_1 = 'https://swapi.dev/api/films/1/'
# URL_FILM_2 = 'https://swapi.dev/api/films/2/'
# URL_FILM_3 = 'https://swapi.dev/api/films/3/'
# URL_FILM_6 = 'https://swapi.dev/api/films/6/'

# Извлекаем данные в формате JSON
data = response.json()

# Получаем список фильмов, в которых снимался персонаж
films = data.get('films', [])

characters = []
for film_url in films:
    film_response = requests.get(film_url)
    assert film_response.status_code == 200

    # Извлекаем данные о фильме
    filmdata = film_response.json()

    # Получаем список персонажей, снимавшихся в фильме
    film_characters = filmdata.get('characters', )

    # Для каждого персонажа проверяем, содержится ли он уже в списке
    # и если нет, добавляем его имя в список
    for character_url in film_characters:
        character_response = requests.get(character_url)

        # Проверяем успешность запроса
        assert character_response.status_code == 200

        # Извлекаем данные о персонаже
        character_data = character_response.json()

        # Получаем имя персонажа
        character_name = character_data.get('name')

        # Проверяем, содержится ли имя персонажа уже в списке
        if character_name not in characters:
            # Если имя персонажа отсутствует, добавляем его в список
            characters.append(character_name)

# Создаем тестовый файл для сохранения имен персонажей
with open('characters.txt', 'w') as file:
    # Записываем имена в файл
    for character in characters:
        file.write(character + '\n')

# Проверяем, что файл создан и заполнен
assert len(characters) > 0

# Выводим информацию о сохранении имен персонажей
print("Имена персонажей сохранены в файл characters.txt")