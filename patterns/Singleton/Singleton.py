# Паттерн Singleton - Одиночка

# Позволяет создавать только один екзепляр обьекта класса
# При создании другого екзпепляра класса новый екзепляр не создаеться, а получает ссылку на самый первый главный и единственный екзепляр класса
# Другие екзепляры обьекта класса, создавать запрещено


# класс создаеть только одну базу данных
class DataBase:

    # __instance хранит ссылку на единственный екзепляр класса
    __instance = None

    def __new__(cls, *args, **kwargs):
        # проверка существует ли уже екзепляр обьекта текущего класса
        if cls.__instance is None:
            # присваиваем ссылку на новосозданый екзеплар обьекта класса, если первый екзепляр еще не был создан
            cls.__instance = super().__new__(cls)

        # возвращаем адрессе нового или ранее созданого екзепляра обьекта класса
        return cls.__instance

    def __del__(self):
        # удаление единственого екзепляра обьекта класса
        # после чего мы можем повторно создать новый екзепляра класса, новую базу данных
        DataBase.__instance = None

    # создание одной базы данных с которой будем работать
    def __init__(self, user, password, port):

        self.user = user
        self.password = password
        self.port = port

    # подключение к базе данных
    def connect(self):
        print(f"Connect with DB {self.user} , {self.password} , {self.port}")

    # отключение от базы данных
    def close(self):
        print("Disconnect from DB")

    # чтение данных из базы данных, берем какието значения
    def read(self):
        return "Data from DB"

    # добавляем данные в базу данных
    def write(self, data):
        print(f"Write data into DB {data}")


my_db1 = DataBase("kondrich1", 1234, 1000)

# значение атрибутов екзеплара класса просто заменяються на новые значения
my_db2 = DataBase("kondrich2", 5678, 2000)

# ето одна и таже база данны, my_db1 и my_db2 ссылаються на одну и туже ячейку в памяти
id(my_db1) == id(my_db2)  # -> True
id(my_db1)  # -> 2152603046624
id(my_db2)  # -> 2152603046624

my_db1.user, my_db1.password, my_db1.port  # -> kondrich2 5678 2000
my_db2.user, my_db2.password, my_db2.port  # -> kondrich2 5678 2000

my_db1.connect()
my_db2.connect()
