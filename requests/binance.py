# Библиотека requests

import requests
import time


# url-адресс api bincance
url = "https://api.binance.com/api/v3/ticker/price"


# получем ответ от binance про стоимость биткоина к долару
response = requests.get(url, params={"symbol": "BTCUSDT"})

# данные в ответе от binance храняться в response.content
content = response.content

# возвращаеться json-строка
content  # -> b'{"symbol":"BTCUSDT","price":"64220.00000000"}'
type(content)  # -> <class 'bytes'>

# форматируем все полученные данные json-формата, кототорые лежат в content в данные типа словаря dict
price = response.json()

price  # -> {'symbol': 'BTCUSDT', 'price': '64243.00000000'}
type(price)  # -> <class 'dict'>


# цены на биткоины за текущие 10 секунд
bitcoin_prices = []

# ловим исключение при ошибке подключиться к указаному сайту
try:
    for i in range(10):
        response = requests.get(url, params={"symbol": "BTCUSDT"})
        # переводим в словарь только значение ключа price
        price = float(response.json()["price"])
        # добавляем елементв в список
        bitcoin_prices.append(price)
        # остановление выполнение кода на 1 секунду
        time.sleep(1)

except requests.exceptions.ConnectionError as error:
    print(
        f"Something goes wrong: {error}"
    )  # -> HTTPSConnectionPool(host='api.binance.com', port=443): Max retries exceeded with url: /api/v3/ticker/price?symbol=BTCUSDT
    print("There is NO internet")


bitcoin_prices  # ->  [64291.23, 64291.22, 64291.22, 64291.23, 64291.22, 64291.22, 64291.23, 64291.23, 64291.22, 64291.23]
type(bitcoin_prices)  # -> <class 'list'>
len(bitcoin_prices)  # -> 10
max(bitcoin_prices)  # -> 64291.23
min(bitcoin_prices)  # -> 64291.22
   