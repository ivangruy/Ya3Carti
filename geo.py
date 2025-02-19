import requests


# Найти объект по координатам.
def reverse_geocode(ll):
    geocoder_request_template = map_request = "https://static-maps.yandex.ru/v1?ll=37.677751,55.757718&spn=0.016457,0.00619&apikey=dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"


    # Выполняем запрос к геокодеру, анализируем ответ.
    geocoder_request = geocoder_request_template.format(**locals())
    response = requests.get(geocoder_request)

    if not response:
        raise RuntimeError(
            """Ошибка выполнения запроса:
            {request}
            Http статус: {status} ({reason})""".format(
                request=geocoder_request, status=response.status_code, reason=response.reason))

    # Преобразуем ответ в json-объект
    json_response = response.json()

    # Получаем первый топоним из ответа геокодера.
    features = json_response["response"]["GeoObjectCollection"]["featureMember"]
    return features[0]["GeoObject"] if features else None
