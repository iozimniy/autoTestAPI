import configuration
import requests
import data

# функция для создания заказа
def create_order(body):
    return requests.post(configuration.URL_SERVER + configuration.CREATE_ORDER,
                         json=body)
# сохраняем трек в переменную
track = create_order(data.order_body).json()["track"]

# запрашиваем информация по track
# для присоединения track к запросу меняем тип данных на строку
def info_order(track_id):
    return requests.get(configuration.URL_SERVER + configuration.INFO_ORDER + str(track))