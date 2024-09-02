# Бой Между Двумя Существами


# базовый класс Персонаж от которого будем наследовать наших существ
class Character:

    def __init__(self, *, level: int):
        # уровень персонажа
        self.level = level
        # здоровье персонажа
        self.health_points = self.base_health_points * level
        # урон атаки персонажа
        self.attack_power = self.base_attack_power * level

    # дает возможность текущему существу атаковать указаную цель
    def attack(self, *, target: "Character"):

        # указаная цель получает урон
        target.got_damage(damage=self.attack_power)

    # метод указывает что персонаж получает урон
    def got_damage(self, *, damage: int):

        # указываем получаемый урон по формуле учитывая защиту персонажа
        damage = damage * (100 - self.defense) / 100  # -> float number

        damage = round(damage)  # -> int number

        self.health_points -= damage

    # указывает защиту персонажа
    @property
    def defense(self):
        defense = self.base_defense * self.level
        return defense

    # указывает что наше текущее существо(обьект класса) живое или нет
    def is_alive(self):
        return self.health_points > 0  # -> True/False

    def __str__(self):
        return f"{self.character_name} -> (level:{self.level}) (health_points: {self.health_points})"


class Ork(Character):
    # базовый значение здоровья персонажа
    base_health_points = 100
    # базовое значение урона персонажа
    base_attack_power = 10
    # имя персонажа
    character_name = "Ork"
    # базовое значение брони персонажа
    base_defense = 15

    # пререопредиляем метод брони для нашего орка
    @property
    def defense(self):

        defense = super().defense

        # увичиваем броню если у орка здоровье меньше 50 очков
        if self.health_points < 50:
            defense *= 3


class Elf(Character):

    base_health_points = 50
    base_attack_power = 15
    character_name = "Elf"
    base_defense = 10


# реализация боя между двумя существами (кто виживет?)
def fight(*, character_1: Character, character_2: Character):
    while character_1.is_alive() and character_2.is_alive():
        character_1.attack(target=character_2)
        if character_2.is_alive():
            character_2.attack(target=character_1)

    print(f"Character_1 -> {character_1} , is_alive -> {character_1.is_alive()}")
    print(f"Character_2 -> {character_2} , is_alive -> {character_2.is_alive()}")
