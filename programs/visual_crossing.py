# Берем данные о погоде из сайта Visual Crossing через его API

import requests
from requests.exceptions import RequestException

import time

# секретный ключ-api который взят из сайта
API_KEY = "EGGMLTWF82GFVJZKHXLXXZJ8Y"


# при неуспешной отправке запроса функция повторяет отправку запроса к сайту
# повторяет выполнение переданой внутрь функции
def retry(func):

    def wrapper_retry(*args, **kwargs):

        # повторение попытки запроса через указаное количество секунд (5 секунд, 30 секунд)
        retries = [5, 10]
        for seconds in retries:
            try:
                return func(*args, **kwargs)

            # исключение отправки запроса к api сайта
            except RequestException:
                print(f"Failed to get data. Retrying in {seconds} seconds")
                time.sleep(seconds)

        return func(*args, **kwargs)

    return wrapper_retry


# функция возвращает словарь, который лежит внутри списка
@retry
def get_weather_by_hours_for_day_from_api(*, date: str, city: str) -> list[dict]:
    # url-адресс сайта
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date}/{date}?unitGroup=us&key={API_KEY}"

    # отправляем запрос на наш сайт
    respose = requests.get(url)

    # берем значение в словаре по ключу days
    weather_by_days = respose.json()["days"]
    weather_by_hours = weather_by_days[0]["hours"]

    return weather_by_hours


# функция переводит градусы фаренгейтов в градусы цельсии
def fahrenheit_to_celsius(*, fahrenheit_temperature: float) -> int:
    return round((fahrenheit_temperature - 32) * 5 / 9)


# функция возвращает наиболее небезопасные часи погоды
def get_dangerous_hours(*, weather_by_hours: list[dict]) -> list[dict]:

    # хранит опасные часы погоды в день
    dangerous_hours = []

    for weather in weather_by_hours:

        # берем значение коефициента опасности погоды по названия ключу uvindex
        uvindex = weather["uvindex"]

        time = weather["datetime"]

        # берем значение в фаренгейтах и переводим в цельсии с помощью нашей функции
        celsius_temperature = fahrenheit_to_celsius(
            fahrenheit_temperature=weather["temp"]
        )

        # если uvindex больше или равно 3, тогда ето опасный час в дне
        if uvindex >= 3:
            dangerous_hours.append(
                {"time": time, "uvindex": uvindex, "temperature": celsius_temperature}
            )

    return dangerous_hours


date = "2024-04-05"
city = "London,UK"

weather_by_hours = get_weather_by_hours_for_day_from_api(date=date, city=city)
dangerous_hours = get_dangerous_hours(weather_by_hours=weather_by_hours)


print(weather_by_hours)
print("------------------------------------------------------")
print(dangerous_hours)
