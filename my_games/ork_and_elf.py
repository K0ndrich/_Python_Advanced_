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

    # указывает что наше текущее существо(обьект класса) живое или нет
    def is_alive(self):
        return self.health_points > 0  # -> True/False

    def __str__(self):
        return f"{self.character_name} -> (level:{self.level}) (health_points: {self.health_points})"


class Ork(Character):

    base_health_points = 100
    base_attack_power = 10
    character_name = "Ork"


class Elf(Character):

    base_health_points = 50
    base_attack_power = 15
    character_name = "Elf"


# реализация боя между двумя существами (кто виживет?)
def fight(*, character_1: Character, character_2: Character):
    while character_1.is_alive() and character_2.is_alive():
        character_1.attack(target=character_2)
        if character_2.is_alive():
            character_2.attack(target=character_1)

    print(f"Character_1 -> {character_1} , is_alive -> {character_1.is_alive()}")
    print(f"Character_2 -> {character_2} , is_alive -> {character_2.is_alive()}")


ork = Ork(level=5)
elf = Elf(level=7)


fight(character_1=ork, character_2=elf)
