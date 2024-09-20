# Дабавление новых данных у уже существующий csv-файл

import csv

persons = [
    {"name": "Jack", "age": 26, "occupation": "Artist"},
    {"name": "Emma", "age": 32, "occupation": "Programmer"},
]

# "a" означает добавленние данных в файл
my_file = open("libraries/csv/files/persons.csv", "a")

my_fields = ["name", "age", "occupation"]

# создание класса предназначеного для записи новых данных в уже существующий csv-файл
csv_dict_writer = csv.DictWriter(my_file, fieldnames=my_fields)

# передаем наш словарь для преобразование в csv
csv_dict_writer.writerows(persons)

my_file.close()
