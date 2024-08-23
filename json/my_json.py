# JSON (Java Script Object Notation)
# JSON -> текстовый формат обмена данный с помощью словарей(dict) - {"name":"Max" , "age":222}

import json


book = {
    "title": "1984",
    "author": "George Orwell",
    "isbn": "823812323",
    "id": "777",
}

# запаковываем словарь в json строку
json_string = json.dumps(book)

json_string  # -> {"title": "1984", "author": "George Orwell", "isbn": "823812323", "id": "777"}
type(json_string)  # -> <class 'str'>


# розпаковываем json строку в словарь
book = json.loads(json_string)

book  # -> {'title': '1984', 'author': 'George Orwell', 'isbn': '823812323', 'id': '777'}
type(book)  # -> <class 'dict'>
