# класс принимает количесвто секунд от пользователя и возвращает дату в нормальном формате
class Clock:

    # хранит число секунд в одном дне
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Second must be integer number")

        self.seconds = seconds % self.__DAY

    def get_time(self):
        seconds = self.seconds % 60
        minutes = (self.seconds // 60) % 60
        hours = (self.seconds // 3600) % 24
        return f"{self.__get_formated(hours)} : {self.__get_formated(minutes)} : {self.__get_formated(seconds)}"

    @classmethod
    def __get_formated(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Right number must be integer number or type Clock")

        sc = other
        # если other являеться обьектов класса Clock
        if isinstance(other, Clock):
            # тогда будем прибавлять не сам other, а атрибут other.seconds
            sc = other.seconds
        return Clock(self.seconds + sc)


c1 = Clock(1000)
c2 = Clock(2000)
c3 = Clock(3000)
с4 = c1 + c2 + c3
print(с4.get_time())
