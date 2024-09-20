# Чтение CSV файлов

import csv


my_file = open("libraries/csv/files/persons.csv", "r")

csv_dict_reader = csv.DictReader(my_file)


for row in csv_dict_reader:
    print(row["name"], row["age"], row["occupation"])


my_file.close()
