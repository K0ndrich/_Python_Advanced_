# Модуль datetime для работы с датами и временем в коде

import datetime


# возвращает полное время
current_time = datetime.datetime.now()  # -> 2024-09-19 17:31:02.595345

# теперь точно указываем часовой пояс
utc_time = datetime.datetime.now(datetime.UTC)  # -> 2024-09-19 14:31:19.181961+00:00

# возвращает время в iso формате
current_time.isoformat()  # -> 2024-09-19T17:33:43.543775


# возвращает текущий год, месяц, день, час, минуты, секунды
current_time.year  # -> 2024
current_time.month  # -> 9
current_time.day  # -> 19
current_time.hour  # -> 17
current_time.minute  # -> 36
current_time.second  # -> 4


# хранит внутри себя указанное нами рандомное время
some_time = datetime.datetime(
    year=1996, month=8, day=12, hour=9, minute=27, second=19
)  # -> 1996-08-12 09:27:19


# хранит текущую сегоднешнюю дату
current_date = datetime.date.today()  # -> 2024-09-19


# берем значение даты по другому
current_datetime = datetime.datetime.now()  # -> 2024-09-19 17:41:39.110583
current_date = current_datetime.date()  # -> 2024-09-19


# хранит дату и время указаное количество дней назад
current_datetime = datetime.datetime.now()  # -> 2024-09-19 17:43:28.901097
day_ago = current_datetime - datetime.timedelta(days=1)  # -> 2024-09-18 17:43:16.565779


# выводит дату и время за указаными формат кодами (Format Codes), которые более приятно читаемые
current_datetime = datetime.datetime.now()  # -> 2024-09-19 17:43:28.901097
current_datetime = current_datetime.strftime(
    "%A, %d, %B, %Y"
)  # -> Thursday, 19, September, 2024


# превращает дату и время в iso формате в стандарный формат
iso_fomat = "2024-09-19T17:33:43.543775"
my_datetime = datetime.datetime.fromisoformat(
    iso_fomat
)  # -> 2024-09-19 17:33:43.543775
