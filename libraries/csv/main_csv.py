# CSV - построчный набор данных разделенный указаным сепараторов, почти всегда ето кома ,
# Ето тип данных служит для преобразование данных в таблицe Exel

import csv

my_rows = [
    ["name", "age", "occupation"],
    ["John", "28", "Engineer"],
    ["Marie", "22", "Designer"],
    ["Mike", "32", "Doctor"],
]

# открываем файл для изменния
my_file = open("libraries/csv/files/persons.csv", "w")

# создание csv класса предназначеного для записи данных в файл
csv_writer = csv.writer(my_file)  # -> <_csv.writer object at 0x000001B79666EF80>

# указываем какие строки будем записывать в наш файл persons.csv
csv_writer.writerows(my_rows)

my_file.close()
